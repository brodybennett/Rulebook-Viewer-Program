#!/usr/bin/env python3
"""
lint_roll_syntax.py

Read-only linter for standardized roll expressions used in `yaml ability` blocks.

Checks:
- expression grammar and parseability
- unknown namespaces/tokens (especially attr and skill refs)
- alias usage where canonical token is required
- non-canonical spacing/label notation

Examples:
  python tools/lint_roll_syntax.py --repo .
  python tools/lint_roll_syntax.py --repo . --expr "1d20 + @attr.int + @skill.occultism + @bonus"
  python tools/lint_roll_syntax.py --repo . --expr "1d20+@attr.agility+@skill.fighting"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from difflib import get_close_matches
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

DEFAULT_CONTENT_ROOT = "draft"
DEFAULT_SCHEMA_PATH = "meta/ability_schema.yml"
FENCE_START_RE = re.compile(r"^\s*```(?:yaml|yml)\s+ability\s*$", re.IGNORECASE)
FENCE_END_RE = re.compile(r"^\s*```\s*$")
ROLL_KEY_RE = re.compile(r"(?:^|_)roll$", re.IGNORECASE)
LABEL_RE = re.compile(r"^(?P<label>[a-z_]+)\s*:\s*(?P<body>.+)$", re.IGNORECASE)
REF_RE = re.compile(r"^@([a-z]+)\.([a-z0-9_]+)$")
VS_ONLY_RE = re.compile(r"^vs\s+(.+)$", re.IGNORECASE)
VS_SPLIT_RE = re.compile(r"\bvs\b", re.IGNORECASE)
NAMESPACE_KEYS = ("attr", "skill", "def", "res", "mod")


@dataclass(frozen=True)
class RollRegistry:
    tokens: Dict[str, set]
    shorthand_refs: set
    aliases: Dict[str, Dict[str, str]]


@dataclass(frozen=True)
class ParseIssue:
    code: str
    message: str
    col: int
    expected: Optional[str] = None


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    col: int
    field: str
    expression: str
    code: str
    message: str
    expected: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "line": self.line,
            "col": self.col,
            "field": self.field,
            "expression": self.expression,
            "code": self.code,
            "message": self.message,
            "expected": self.expected,
        }


@dataclass(frozen=True)
class AbilityBlock:
    fence_line: int
    content_start_line: int
    lines: List[str]
    text: str


@dataclass(frozen=True)
class Token:
    kind: str
    value: str
    col: int


class ParseError(ValueError):
    def __init__(self, code: str, message: str, col: int, expected: Optional[str] = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.col = max(1, col)
        self.expected = expected


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def resolve_under_repo(repo: Path, raw_path: str) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return repo / p


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(str(path))
    return yaml.safe_load(path.read_text(encoding="utf-8", errors="replace"))


def _token_set(raw: Any, key: str) -> set:
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"roll_registry.{key} must be a non-empty list.")
    return {str(item).strip().lower() for item in raw if str(item).strip()}


def load_roll_registry(schema_data: Dict[str, Any]) -> RollRegistry:
    raw = schema_data.get("roll_registry")
    if not isinstance(raw, dict):
        raise ValueError("ability_schema.yml must contain roll_registry mapping.")

    tokens: Dict[str, set] = {}
    for key in NAMESPACE_KEYS:
        tokens[key] = _token_set(raw.get(key), key)

    shorthand_refs = {
        str(item).strip().lower() for item in raw.get("shorthand_refs", []) if str(item).strip()
    }

    aliases: Dict[str, Dict[str, str]] = {key: {} for key in NAMESPACE_KEYS}
    raw_aliases = raw.get("aliases", {})
    if isinstance(raw_aliases, dict):
        for ns, mapping in raw_aliases.items():
            if ns not in aliases or not isinstance(mapping, dict):
                continue
            aliases[ns] = {
                str(k).strip().lower(): str(v).strip().lower()
                for k, v in mapping.items()
                if str(k).strip() and str(v).strip()
            }

    return RollRegistry(tokens=tokens, shorthand_refs=shorthand_refs, aliases=aliases)


def iter_markdown_files(scan_root: Path) -> Iterable[Path]:
    if not scan_root.exists() or not scan_root.is_dir():
        return []
    return sorted(p for p in scan_root.rglob("*.md") if p.is_file())


def split_semicolon_clauses(snippet: str) -> List[Tuple[str, int]]:
    clauses: List[Tuple[str, int]] = []
    start = 0
    for idx, ch in enumerate(snippet):
        if ch != ";":
            continue
        raw = snippet[start:idx]
        stripped = raw.strip()
        if stripped:
            leading = len(raw) - len(raw.lstrip())
            clauses.append((stripped, start + leading + 1))
        start = idx + 1

    raw = snippet[start:]
    stripped = raw.strip()
    if stripped:
        leading = len(raw) - len(raw.lstrip())
        clauses.append((stripped, start + leading + 1))
    return clauses


def tokenize_expression(expr: str) -> List[Token]:
    tokens: List[Token] = []
    i = 0
    n = len(expr)

    while i < n:
        ch = expr[i]
        if ch.isspace():
            i += 1
            continue

        if ch in "+-":
            tokens.append(Token(kind="OP", value=ch, col=i + 1))
            i += 1
            continue

        if ch == "(":
            tokens.append(Token(kind="LPAREN", value=ch, col=i + 1))
            i += 1
            continue

        if ch == ")":
            tokens.append(Token(kind="RPAREN", value=ch, col=i + 1))
            i += 1
            continue

        if ch == "@":
            j = i + 1
            while j < n and (expr[j].isalnum() or expr[j] in "._"):
                j += 1
            if j == i + 1:
                raise ParseError("invalid_reference", "Reference cannot be '@' only.", i + 1)
            tokens.append(Token(kind="REF", value=expr[i:j], col=i + 1))
            i = j
            continue

        if ch.isdigit():
            j = i
            while j < n and expr[j].isdigit():
                j += 1
            if j < n and expr[j] in "dD":
                k = j + 1
                while k < n and expr[k].isdigit():
                    k += 1
                if k == j + 1:
                    raise ParseError("invalid_dice", "Dice must include a side count (NdM).", j + 2)
                tokens.append(Token(kind="DICE", value=expr[i:k].lower(), col=i + 1))
                i = k
                continue

            tokens.append(Token(kind="INT", value=expr[i:j], col=i + 1))
            i = j
            continue

        raise ParseError("invalid_character", f"Invalid character '{ch}' in expression.", i + 1)

    return tokens


def validate_reference(raw: str, registry: RollRegistry, col: int, expected_ns: Optional[str] = None) -> str:
    lowered = raw.lower()
    if raw != lowered:
        raise ParseError(
            "non_canonical_reference",
            "References must be lowercase.",
            col,
            expected=lowered,
        )

    if lowered in registry.shorthand_refs:
        if expected_ns and expected_ns != "mod":
            raise ParseError(
                "invalid_reference_namespace",
                f"{lowered} cannot be used in this position; expected @{expected_ns}.<token>.",
                col,
            )
        return lowered

    m = REF_RE.fullmatch(lowered)
    if not m:
        raise ParseError(
            "invalid_reference_format",
            "Reference must use @namespace.token format.",
            col,
        )

    namespace, token = m.group(1), m.group(2)
    if namespace not in registry.tokens:
        raise ParseError("unknown_namespace", f"Unknown namespace '@{namespace}'.", col)
    if expected_ns and namespace != expected_ns:
        raise ParseError(
            "invalid_reference_namespace",
            f"Expected @{expected_ns}.<token> but found @{namespace}.{token}.",
            col,
            expected=f"@{expected_ns}.<token>",
        )

    allowed = registry.tokens[namespace]
    if token not in allowed:
        alias_target = registry.aliases.get(namespace, {}).get(token)
        if alias_target:
            raise ParseError(
                "alias_not_allowed",
                f"Use canonical token '@{namespace}.{alias_target}' instead of '@{namespace}.{token}'.",
                col,
                expected=f"@{namespace}.{alias_target}",
            )

        suggestion = get_close_matches(token, sorted(allowed), n=1)
        if suggestion:
            raise ParseError(
                "unknown_token",
                f"Unknown {namespace} token '{token}'.",
                col,
                expected=f"@{namespace}.{suggestion[0]}",
            )
        raise ParseError(
            "unknown_token",
            f"Unknown {namespace} token '{token}'.",
            col,
        )

    return f"@{namespace}.{token}"


class ExpressionParser:
    def __init__(self, tokens: Sequence[Token], registry: RollRegistry):
        self.tokens = list(tokens)
        self.registry = registry
        self.idx = 0

    def parse(self) -> str:
        if not self.tokens:
            raise ParseError("empty_expression", "Expression cannot be empty.", 1)
        out = self._parse_expression()
        if self._peek() is not None:
            tok = self._peek()
            raise ParseError("unexpected_token", f"Unexpected token '{tok.value}'.", tok.col)
        return out

    def _peek(self) -> Optional[Token]:
        if self.idx >= len(self.tokens):
            return None
        return self.tokens[self.idx]

    def _peek_next(self) -> Optional[Token]:
        j = self.idx + 1
        if j >= len(self.tokens):
            return None
        return self.tokens[j]

    def _consume(self) -> Token:
        tok = self._peek()
        if tok is None:
            end_col = 1
            if self.tokens:
                last = self.tokens[-1]
                end_col = last.col + len(last.value)
            raise ParseError("unexpected_eof", "Expression ended unexpectedly.", end_col)
        self.idx += 1
        return tok

    def _parse_expression(self) -> str:
        left = self._parse_term()
        while True:
            tok = self._peek()
            if tok is None or tok.kind != "OP" or tok.value not in {"+", "-"}:
                break
            op = self._consume().value
            right = self._parse_term()
            left = f"{left} {op} {right}"
        return left

    def _parse_term(self) -> str:
        tok = self._peek()
        if tok is None:
            end_col = 1
            if self.tokens:
                last = self.tokens[-1]
                end_col = last.col + len(last.value)
            raise ParseError("expected_term", "Expected a term.", end_col)

        if tok.kind == "LPAREN":
            self._consume()
            inner = self._parse_expression()
            closing = self._peek()
            if closing is None or closing.kind != "RPAREN":
                col = tok.col + 1
                if closing is not None:
                    col = closing.col
                raise ParseError("missing_paren", "Missing closing ')' in expression.", col)
            self._consume()
            return f"({inner})"

        if tok.kind == "DICE":
            self._consume()
            count_raw, sides_raw = tok.value.split("d", 1)
            count = int(count_raw)
            sides = int(sides_raw)
            if count <= 0 or sides <= 0:
                raise ParseError("invalid_dice", "Dice count and sides must be > 0.", tok.col)
            return f"{count}d{sides}"

        if tok.kind == "INT":
            self._consume()
            return str(int(tok.value))

        if tok.kind == "OP" and tok.value == "-":
            nxt = self._peek_next()
            if nxt and nxt.kind == "INT":
                self._consume()
                int_tok = self._consume()
                return str(-int(int_tok.value))
            raise ParseError("invalid_unary_minus", "Unary '-' is only allowed before integers.", tok.col)

        if tok.kind == "REF":
            self._consume()
            return validate_reference(tok.value, self.registry, tok.col)

        raise ParseError("expected_term", f"Expected a term but found '{tok.value}'.", tok.col)


def parse_check_expression(expr: str, registry: RollRegistry) -> str:
    tokens = tokenize_expression(expr)
    parser = ExpressionParser(tokens, registry)
    return parser.parse()


def parse_clause(clause: str, registry: RollRegistry) -> str:
    label_match = LABEL_RE.match(clause)
    if label_match:
        label = label_match.group("label").strip().lower()
        body = label_match.group("body").strip()
        if label in {"roll", "check", "damage", "heal"}:
            return f"{label}: {parse_check_expression(body, registry)}"
        if label == "vs":
            return f"vs {validate_reference(body, registry, col=1, expected_ns='def')}"
        raise ParseError("unsupported_label", f"Unsupported clause label '{label}'.", 1)

    vs_only = VS_ONLY_RE.match(clause)
    if vs_only:
        rhs = vs_only.group(1).strip()
        return f"vs {validate_reference(rhs, registry, col=1, expected_ns='def')}"

    vs_match = VS_SPLIT_RE.search(clause)
    if vs_match:
        left = clause[: vs_match.start()].strip()
        right = clause[vs_match.end() :].strip()
        if not left:
            raise ParseError("missing_left_expr", "Missing check expression before 'vs'.", 1)
        if not right:
            raise ParseError("missing_defense_ref", "Missing defense reference after 'vs'.", 1)
        left_expr = parse_check_expression(left, registry)
        right_ref = validate_reference(right, registry, col=vs_match.start() + 1, expected_ns="def")
        return f"{left_expr} vs {right_ref}"

    return parse_check_expression(clause, registry)


def lint_roll_snippet(snippet: str, registry: RollRegistry, strict_style: bool) -> Tuple[Optional[str], List[ParseIssue]]:
    text = snippet.strip()
    if not text:
        return None, [ParseIssue(code="empty_expression", message="Roll expression cannot be empty.", col=1)]

    clauses = split_semicolon_clauses(text)
    if not clauses:
        return None, [ParseIssue(code="empty_expression", message="Roll expression cannot be empty.", col=1)]

    canonical_clauses: List[str] = []
    for clause, start_col in clauses:
        try:
            canonical = parse_clause(clause, registry)
            canonical_clauses.append(canonical)
        except ParseError as exc:
            return None, [
                ParseIssue(
                    code=exc.code,
                    message=exc.message,
                    col=start_col + exc.col - 1,
                    expected=exc.expected,
                )
            ]

    canonical_snippet = "; ".join(canonical_clauses)
    issues: List[ParseIssue] = []
    if strict_style and normalize_ws(text) != canonical_snippet:
        issues.append(
            ParseIssue(
                code="non_canonical_notation",
                message="Use canonical roll notation (spacing/labels/tokens).",
                col=1,
                expected=canonical_snippet,
            )
        )
    return canonical_snippet, issues


def extract_ability_blocks(rel_path: str, text: str) -> Tuple[List[AbilityBlock], List[Finding]]:
    lines = text.splitlines()
    blocks: List[AbilityBlock] = []
    findings: List[Finding] = []
    i = 0
    while i < len(lines):
        if not FENCE_START_RE.match(lines[i]):
            i += 1
            continue

        fence_line = i + 1
        j = i + 1
        while j < len(lines) and not FENCE_END_RE.match(lines[j]):
            j += 1

        if j >= len(lines):
            findings.append(
                Finding(
                    path=rel_path,
                    line=fence_line,
                    col=1,
                    field="yaml ability",
                    expression="```yaml ability",
                    code="unclosed_ability_block",
                    message="Unclosed `yaml ability` fenced block.",
                )
            )
            break

        content_lines = lines[i + 1 : j]
        blocks.append(
            AbilityBlock(
                fence_line=fence_line,
                content_start_line=i + 2,
                lines=content_lines,
                text="\n".join(content_lines),
            )
        )
        i = j + 1

    return blocks, findings


def collect_roll_fields(node: Any, path: str = "") -> List[Tuple[str, Any]]:
    out: List[Tuple[str, Any]] = []
    if isinstance(node, dict):
        for key, value in node.items():
            key_s = str(key)
            next_path = f"{path}.{key_s}" if path else key_s
            if ROLL_KEY_RE.search(key_s):
                out.append((next_path, value))
            if isinstance(value, (dict, list)):
                out.extend(collect_roll_fields(value, next_path))
    elif isinstance(node, list):
        for idx, value in enumerate(node):
            next_path = f"{path}[{idx}]"
            if isinstance(value, (dict, list)):
                out.extend(collect_roll_fields(value, next_path))
    return out


def locate_field_position(block: AbilityBlock, field_path: str, expression: str) -> Tuple[int, int]:
    key_hint = field_path.split(".")[-1]
    key_hint = re.sub(r"\[\d+\]$", "", key_hint)

    if key_hint:
        key_re = re.compile(rf"^\s*{re.escape(key_hint)}\s*:", re.IGNORECASE)
        for idx, line in enumerate(block.lines):
            if key_re.search(line):
                col = max(1, line.lower().find(key_hint.lower()) + 1)
                return block.content_start_line + idx, col

    expr_first = expression.strip().splitlines()[0] if expression.strip() else ""
    if expr_first:
        for idx, line in enumerate(block.lines):
            needle = expr_first[:40]
            col = line.find(needle)
            if col >= 0:
                return block.content_start_line + idx, col + 1

    return block.fence_line, 1


def scan_markdown(
    repo: Path,
    scan_root: Path,
    registry: RollRegistry,
    strict_style: bool,
) -> Tuple[int, int, int, List[Finding]]:
    files_scanned = 0
    blocks_scanned = 0
    expressions_scanned = 0
    findings: List[Finding] = []

    for md in iter_markdown_files(scan_root):
        files_scanned += 1
        rel_path = md.relative_to(repo).as_posix()
        text = md.read_text(encoding="utf-8", errors="replace")

        blocks, block_findings = extract_ability_blocks(rel_path, text)
        findings.extend(block_findings)
        blocks_scanned += len(blocks)

        for block in blocks:
            if not block.text.strip():
                findings.append(
                    Finding(
                        path=rel_path,
                        line=block.content_start_line,
                        col=1,
                        field="yaml ability",
                        expression="",
                        code="empty_ability_block",
                        message="Empty `yaml ability` block.",
                    )
                )
                continue

            try:
                payload = yaml.safe_load(block.text)
            except yaml.YAMLError as exc:
                line = block.content_start_line
                col = 1
                mark = getattr(exc, "problem_mark", None)
                if mark is not None:
                    line = block.content_start_line + int(mark.line)
                    col = int(mark.column) + 1
                findings.append(
                    Finding(
                        path=rel_path,
                        line=line,
                        col=col,
                        field="yaml ability",
                        expression=block.text.splitlines()[0] if block.text.splitlines() else "",
                        code="invalid_yaml",
                        message=f"Invalid YAML: {exc}",
                    )
                )
                continue

            if payload is None:
                findings.append(
                    Finding(
                        path=rel_path,
                        line=block.content_start_line,
                        col=1,
                        field="yaml ability",
                        expression="",
                        code="empty_ability_block",
                        message="Empty `yaml ability` block.",
                    )
                )
                continue

            if not isinstance(payload, dict):
                findings.append(
                    Finding(
                        path=rel_path,
                        line=block.content_start_line,
                        col=1,
                        field="yaml ability",
                        expression=str(type(payload)),
                        code="invalid_ability_root",
                        message="`yaml ability` block root must be a mapping/object.",
                    )
                )
                continue

            roll_fields = collect_roll_fields(payload)
            for field_path, raw_expr in roll_fields:
                line, col = locate_field_position(block, field_path, str(raw_expr))
                if raw_expr is None:
                    continue
                if not isinstance(raw_expr, str):
                    findings.append(
                        Finding(
                            path=rel_path,
                            line=line,
                            col=col,
                            field=field_path,
                            expression=str(raw_expr),
                            code="roll_not_string",
                            message="Roll fields must be string or null.",
                        )
                    )
                    continue

                expressions_scanned += 1
                canonical, issues = lint_roll_snippet(raw_expr, registry, strict_style)
                if not issues:
                    continue
                for issue in issues:
                    findings.append(
                        Finding(
                            path=rel_path,
                            line=line,
                            col=max(1, col + issue.col - 1),
                            field=field_path,
                            expression=raw_expr,
                            code=issue.code,
                            message=issue.message,
                            expected=issue.expected if canonical is None else issue.expected,
                        )
                    )

    return files_scanned, blocks_scanned, expressions_scanned, findings


def scan_cli_expressions(
    expressions: List[str],
    registry: RollRegistry,
    strict_style: bool,
) -> Tuple[int, List[Finding]]:
    count = 0
    findings: List[Finding] = []
    for idx, expr in enumerate(expressions, start=1):
        count += 1
        canonical, issues = lint_roll_snippet(expr, registry, strict_style)
        if not issues:
            continue
        for issue in issues:
            findings.append(
                Finding(
                    path=f"<expr:{idx}>",
                    line=1,
                    col=issue.col,
                    field="expr",
                    expression=expr,
                    code=issue.code,
                    message=issue.message,
                    expected=issue.expected if canonical is None else issue.expected,
                )
            )
    return count, findings


def print_report(
    *,
    repo: Path,
    scan_root: Path,
    schema_path: Path,
    strict_style: bool,
    files_scanned: int,
    blocks_scanned: int,
    expressions_scanned: int,
    cli_expressions_scanned: int,
    findings: List[Finding],
    max_findings: int,
) -> None:
    print("Roll syntax lint report")
    print(f"repo: {repo}")
    print(f"scan_root: {scan_root}")
    print(f"schema: {schema_path}")
    print(f"strict_style: {strict_style}")
    print(f"files_scanned: {files_scanned}")
    print(f"ability_blocks_scanned: {blocks_scanned}")
    print(f"roll_fields_scanned: {expressions_scanned}")
    print(f"cli_expressions_scanned: {cli_expressions_scanned}")
    print(f"findings: {len(findings)}")
    print("")

    if not findings:
        print("No roll-syntax issues found.")
        return

    print("Detailed findings:")
    for finding in findings[: max(1, max_findings)]:
        print(
            f"{finding.path}:{finding.line}:{finding.col}: "
            f"[{finding.code}] {finding.message} (field={finding.field})"
        )
        print(f"  expression: {finding.expression}")
        if finding.expected:
            print(f"  expected: {finding.expected}")

    if len(findings) > max_findings:
        hidden = len(findings) - max_findings
        print("")
        print(f"... {hidden} additional finding(s) hidden (use --max-findings to increase).")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint standardized roll syntax in yaml ability blocks.")
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory)")
    parser.add_argument(
        "--content-root",
        default=DEFAULT_CONTENT_ROOT,
        help=f"Markdown content root under repo (default: {DEFAULT_CONTENT_ROOT})",
    )
    parser.add_argument(
        "--schema",
        default=DEFAULT_SCHEMA_PATH,
        help=f"Ability schema path (default: {DEFAULT_SCHEMA_PATH})",
    )
    parser.add_argument(
        "--expr",
        action="append",
        default=[],
        help="Inline roll expression/snippet to lint (can be passed multiple times).",
    )
    parser.add_argument(
        "--allow-noncanonical-style",
        action="store_true",
        help="Allow non-canonical spacing/label style (still validates grammar and tokens).",
    )
    parser.add_argument(
        "--max-findings",
        type=int,
        default=200,
        help="Max detailed findings to print (default: 200).",
    )
    parser.add_argument(
        "--json-out",
        default=None,
        help="Optional output path for JSON report.",
    )
    parser.add_argument(
        "--exit-zero",
        action="store_true",
        help="Exit with code 0 even when findings exist.",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    scan_root = resolve_under_repo(repo, args.content_root)
    schema_path = resolve_under_repo(repo, args.schema)
    strict_style = not args.allow_noncanonical_style

    if not schema_path.exists():
        print(f"ERROR: schema file not found: {schema_path}", file=sys.stderr)
        return 2

    try:
        schema_data = load_yaml(schema_path)
        if not isinstance(schema_data, dict):
            raise ValueError("ability schema root must be a mapping/object.")
        registry = load_roll_registry(schema_data)
    except Exception as exc:
        print(f"ERROR: failed to load schema/registry: {exc}", file=sys.stderr)
        return 2

    files_scanned = 0
    blocks_scanned = 0
    expressions_scanned = 0
    findings: List[Finding] = []

    if scan_root.exists() and scan_root.is_dir():
        files_scanned, blocks_scanned, expressions_scanned, scan_findings = scan_markdown(
            repo=repo,
            scan_root=scan_root,
            registry=registry,
            strict_style=strict_style,
        )
        findings.extend(scan_findings)
    elif not args.expr:
        print(f"ERROR: content root not found: {scan_root}", file=sys.stderr)
        return 2

    cli_expr_count, expr_findings = scan_cli_expressions(args.expr, registry, strict_style)
    findings.extend(expr_findings)

    findings = sorted(findings, key=lambda f: (f.path, f.line, f.col, f.field, f.code))
    print_report(
        repo=repo,
        scan_root=scan_root,
        schema_path=schema_path,
        strict_style=strict_style,
        files_scanned=files_scanned,
        blocks_scanned=blocks_scanned,
        expressions_scanned=expressions_scanned,
        cli_expressions_scanned=cli_expr_count,
        findings=findings,
        max_findings=max(1, args.max_findings),
    )

    if args.json_out:
        out_path = resolve_under_repo(repo, args.json_out)
        payload = {
            "repo": str(repo),
            "scan_root": str(scan_root),
            "schema_file": str(schema_path),
            "strict_style": strict_style,
            "files_scanned": files_scanned,
            "ability_blocks_scanned": blocks_scanned,
            "roll_fields_scanned": expressions_scanned,
            "cli_expressions_scanned": cli_expr_count,
            "findings_count": len(findings),
            "findings": [f.to_dict() for f in findings],
        }
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print("")
        print(f"Wrote JSON report: {out_path}")

    if findings and not args.exit_zero:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
