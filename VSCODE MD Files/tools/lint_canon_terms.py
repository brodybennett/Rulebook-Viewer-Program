#!/usr/bin/env python3
"""
lint_canon_terms.py

Read-only linter for canonical LoTM rulebook naming.

Features:
- Loads lint rules from meta/canon_terms.yml
- Scans markdown under a content root (default: draft)
- Reports: found X -> replace with Y
- Supports allowlist filtering for deliberate deviations
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

DEFAULT_CONTENT_ROOT = "draft"
DEFAULT_CANON_PATH = "meta/canon_terms.yml"
DEFAULT_ALLOWLIST_PATH = "meta/canon_allowlist.yml"
FENCE_RE = re.compile(r"^\s*```")


@dataclass(frozen=True)
class Rule:
    rule_id: str
    description: str
    pattern: str
    replace: str
    regex: re.Pattern[str]


@dataclass(frozen=True)
class AllowEntry:
    rule_id: Optional[str]
    path_glob: Optional[str]
    match_regex: Optional[re.Pattern[str]]
    line_regex: Optional[re.Pattern[str]]


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    col: int
    found: str
    replace: str
    rule_id: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "line": self.line,
            "col": self.col,
            "found": self.found,
            "replace": self.replace,
            "rule_id": self.rule_id,
        }


def parse_regex_flags(raw: str) -> int:
    flags = 0
    for flag in (raw or "").strip():
        if flag == "i":
            flags |= re.IGNORECASE
        elif flag == "m":
            flags |= re.MULTILINE
        elif flag == "s":
            flags |= re.DOTALL
        elif flag == "x":
            flags |= re.VERBOSE
        else:
            raise ValueError(f"Unsupported regex flag '{flag}'")
    return flags


def resolve_under_repo(repo: Path, raw_path: str) -> Path:
    p = Path(raw_path)
    if p.is_absolute():
        return p
    return repo / p


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(str(path))
    text = path.read_text(encoding="utf-8", errors="replace")
    return yaml.safe_load(text)


def compile_rules(data: Dict[str, Any]) -> List[Rule]:
    raw_rules = data.get("lint_rules")
    if not isinstance(raw_rules, list) or not raw_rules:
        raise ValueError("canon_terms.yml must contain a non-empty lint_rules list.")

    rules: List[Rule] = []
    for i, raw in enumerate(raw_rules, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"lint_rules[{i}] must be a mapping.")

        rule_id = str(raw.get("id") or f"rule_{i}")
        description = str(raw.get("description") or "")
        pattern = str(raw.get("pattern") or "")
        replace = str(raw.get("replace") or "")
        flags = parse_regex_flags(str(raw.get("flags") or ""))

        if not pattern:
            raise ValueError(f"lint_rules[{i}] ({rule_id}) is missing pattern.")
        if not replace:
            raise ValueError(f"lint_rules[{i}] ({rule_id}) is missing replace.")

        try:
            regex = re.compile(pattern, flags)
        except re.error as exc:
            raise ValueError(f"Invalid regex in lint_rules[{i}] ({rule_id}): {exc}") from exc

        rules.append(
            Rule(
                rule_id=rule_id,
                description=description,
                pattern=pattern,
                replace=replace,
                regex=regex,
            )
        )
    return rules


def compile_allowlist(data: Any) -> List[AllowEntry]:
    if data is None:
        return []

    if isinstance(data, list):
        raw_entries = data
    elif isinstance(data, dict):
        raw_entries = data.get("allow", [])
    else:
        raise ValueError("allowlist YAML must be either a list or a mapping with key 'allow'.")

    if not isinstance(raw_entries, list):
        raise ValueError("allowlist 'allow' value must be a list.")

    entries: List[AllowEntry] = []
    for i, raw in enumerate(raw_entries, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"allow[{i}] must be a mapping.")

        rule_id = raw.get("rule_id")
        path_glob = raw.get("path_glob")
        match_pattern = raw.get("match_regex")
        line_pattern = raw.get("line_regex")

        match_regex = None
        line_regex = None

        if match_pattern:
            try:
                match_regex = re.compile(str(match_pattern))
            except re.error as exc:
                raise ValueError(f"Invalid allow[{i}].match_regex: {exc}") from exc

        if line_pattern:
            try:
                line_regex = re.compile(str(line_pattern))
            except re.error as exc:
                raise ValueError(f"Invalid allow[{i}].line_regex: {exc}") from exc

        entries.append(
            AllowEntry(
                rule_id=str(rule_id) if rule_id else None,
                path_glob=str(path_glob) if path_glob else None,
                match_regex=match_regex,
                line_regex=line_regex,
            )
        )

    return entries


def iter_markdown_files(scan_root: Path) -> Iterable[Path]:
    if not scan_root.exists() or not scan_root.is_dir():
        return []
    return sorted(p for p in scan_root.rglob("*.md") if p.is_file())


def iter_scannable_lines(text: str) -> Iterable[Tuple[int, str]]:
    lines = text.splitlines()
    in_front_matter = bool(lines and lines[0].strip() == "---")
    in_code = False

    for line_no, line in enumerate(lines, start=1):
        if in_front_matter:
            if line_no > 1 and line.strip() == "---":
                in_front_matter = False
            continue

        if FENCE_RE.match(line):
            in_code = not in_code
            continue

        if in_code:
            continue

        yield line_no, line


def is_allowed(
    *,
    allowlist: List[AllowEntry],
    rule_id: str,
    rel_path: str,
    found_text: str,
    line_text: str,
) -> bool:
    for entry in allowlist:
        if entry.rule_id and entry.rule_id != rule_id:
            continue
        if entry.path_glob and not fnmatch(rel_path, entry.path_glob):
            continue
        if entry.match_regex and not entry.match_regex.search(found_text):
            continue
        if entry.line_regex and not entry.line_regex.search(line_text):
            continue
        return True
    return False


def scan(
    *,
    repo: Path,
    scan_root: Path,
    rules: List[Rule],
    allowlist: List[AllowEntry],
) -> Tuple[int, List[Finding]]:
    files_scanned = 0
    findings: List[Finding] = []

    for md_file in iter_markdown_files(scan_root):
        files_scanned += 1
        rel_path = md_file.relative_to(repo).as_posix()
        text = md_file.read_text(encoding="utf-8", errors="replace")

        for line_no, line in iter_scannable_lines(text):
            for rule in rules:
                for match in rule.regex.finditer(line):
                    found_text = match.group(0)
                    if not found_text:
                        continue

                    if is_allowed(
                        allowlist=allowlist,
                        rule_id=rule.rule_id,
                        rel_path=rel_path,
                        found_text=found_text,
                        line_text=line,
                    ):
                        continue

                    findings.append(
                        Finding(
                            path=rel_path,
                            line=line_no,
                            col=match.start() + 1,
                            found=found_text,
                            replace=rule.replace,
                            rule_id=rule.rule_id,
                        )
                    )

    return files_scanned, findings


def build_summary(findings: List[Finding]) -> List[Dict[str, Any]]:
    counter = Counter((f.found, f.replace) for f in findings)
    summary = []
    for (found, replace), count in sorted(
        counter.items(),
        key=lambda item: (-item[1], item[0][0].lower(), item[0][1].lower()),
    ):
        summary.append({"found": found, "replace": replace, "count": count})
    return summary


def print_report(
    *,
    repo: Path,
    scan_root: Path,
    rules: List[Rule],
    files_scanned: int,
    findings: List[Finding],
    max_findings: int,
) -> None:
    print("Canon term lint report")
    print(f"repo: {repo}")
    print(f"scan_root: {scan_root}")
    print(f"rules_loaded: {len(rules)}")
    print(f"files_scanned: {files_scanned}")
    print(f"findings: {len(findings)}")
    print("")

    summary = build_summary(findings)
    if not summary:
        print("No non-canonical term usage found.")
        return

    print("Summary (found X -> replace with Y):")
    for item in summary:
        print(
            f'- found "{item["found"]}" -> replace with "{item["replace"]}": {item["count"]}'
        )

    print("")
    print("Detailed findings:")
    for finding in findings[:max_findings]:
        print(
            f'{finding.path}:{finding.line}:{finding.col}: '
            f'found "{finding.found}" -> replace with "{finding.replace}" '
            f'[{finding.rule_id}]'
        )

    if len(findings) > max_findings:
        hidden = len(findings) - max_findings
        print("")
        print(f"... {hidden} additional finding(s) hidden (use --max-findings to increase).")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint markdown terms against canon_terms.yml")
    parser.add_argument("--repo", default=".", help="Repo root (default: current directory)")
    parser.add_argument(
        "--content-root",
        default=DEFAULT_CONTENT_ROOT,
        help=f"Markdown content folder under repo (default: {DEFAULT_CONTENT_ROOT})",
    )
    parser.add_argument(
        "--canon",
        default=DEFAULT_CANON_PATH,
        help=f"Canon terms YAML path (default: {DEFAULT_CANON_PATH})",
    )
    parser.add_argument(
        "--allowlist",
        default=DEFAULT_ALLOWLIST_PATH,
        help=(
            "Allowlist YAML path (default: meta/canon_allowlist.yml). "
            "Set to an empty string to disable."
        ),
    )
    parser.add_argument(
        "--max-findings",
        type=int,
        default=200,
        help="Max detailed findings to print (default: 200)",
    )
    parser.add_argument(
        "--json-out",
        default=None,
        help="Optional output path for JSON report",
    )
    parser.add_argument(
        "--exit-zero",
        action="store_true",
        help="Exit with code 0 even when findings exist",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    scan_root = resolve_under_repo(repo, args.content_root)
    canon_path = resolve_under_repo(repo, args.canon)
    allowlist_path = resolve_under_repo(repo, args.allowlist) if args.allowlist else None

    if not scan_root.exists():
        print(f"ERROR: content root not found: {scan_root}", file=sys.stderr)
        return 2
    if not canon_path.exists():
        print(f"ERROR: canon file not found: {canon_path}", file=sys.stderr)
        return 2

    try:
        canon_data = load_yaml(canon_path)
        if not isinstance(canon_data, dict):
            raise ValueError("canon_terms.yml root must be a mapping.")
        rules = compile_rules(canon_data)
    except Exception as exc:
        print(f"ERROR: failed to load canon rules: {exc}", file=sys.stderr)
        return 2

    allow_entries: List[AllowEntry] = []
    if allowlist_path and allowlist_path.exists():
        try:
            allow_data = load_yaml(allowlist_path)
            allow_entries = compile_allowlist(allow_data)
        except Exception as exc:
            print(f"ERROR: failed to load allowlist: {exc}", file=sys.stderr)
            return 2

    files_scanned, findings = scan(
        repo=repo,
        scan_root=scan_root,
        rules=rules,
        allowlist=allow_entries,
    )

    print_report(
        repo=repo,
        scan_root=scan_root,
        rules=rules,
        files_scanned=files_scanned,
        findings=findings,
        max_findings=max(1, args.max_findings),
    )

    if args.json_out:
        out_path = resolve_under_repo(repo, args.json_out)
        report = {
            "repo": str(repo),
            "scan_root": str(scan_root),
            "canon_file": str(canon_path),
            "allowlist_file": str(allowlist_path) if allowlist_path else None,
            "rules_loaded": len(rules),
            "files_scanned": files_scanned,
            "findings_count": len(findings),
            "summary": build_summary(findings),
            "findings": [f.to_dict() for f in findings],
        }
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("")
        print(f"Wrote JSON report: {out_path}")

    if findings and not args.exit_zero:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
