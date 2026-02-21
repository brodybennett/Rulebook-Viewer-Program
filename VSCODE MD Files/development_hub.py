#!/usr/bin/env python3
"""
Development Hub

A single local UI to run and review rulebook development tools.

Usage:
  python "VSCODE MD Files/development_hub.py" --repo "VSCODE MD Files"
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import html
import subprocess
import sys
import threading
import time
import urllib.parse
import webbrowser
from pathlib import Path
from typing import Dict, List, Optional

try:
    from flask import Flask, Response, abort, redirect, render_template_string, request, url_for
except ImportError:
    print("[error] Missing dependency: flask\n\nInstall with: pip install flask", file=sys.stderr)
    raise SystemExit(2)


@dataclasses.dataclass(frozen=True)
class ManagedService:
    service_id: str
    title: str
    description: str
    port: int
    script: str
    args: List[str]


@dataclasses.dataclass(frozen=True)
class ToolTask:
    task_id: str
    group: str
    title: str
    description: str
    command: List[str]
    timeout_sec: int = 300


@dataclasses.dataclass
class ServiceState:
    process: Optional[subprocess.Popen] = None
    started_at: Optional[dt.datetime] = None
    log_path: Optional[Path] = None
    log_handle: Optional[object] = None


ROOT: Path = Path(".").resolve()
RUNS_DIR: Path = ROOT / "reports" / "dev_hub_runs"
APP = Flask(__name__)
LOCK = threading.Lock()

RUN_HISTORY: List[dict] = []
SERVICE_STATE: Dict[str, ServiceState] = {}

SERVICES: List[ManagedService] = [
    ManagedService(
        service_id="rulebook-viewer",
        title="Rulebook Viewer",
        description="Launch the markdown viewer UI.",
        port=7860,
        script="rulebook_viewer.py",
        args=["--source", ".", "--content-root", "draft", "--no-browser"],
    ),
    ManagedService(
        service_id="sanity-ui",
        title="Sanity Check UI",
        description="Launch the sanity checker clickthrough UI.",
        port=8787,
        script="lotm_sanity_check.py",
        args=["--root", ".", "--content-root", "draft", "--serve"],
    ),
]

TASKS: List[ToolTask] = [
    ToolTask(
        task_id="extract-compendium",
        group="Build",
        title="Extract Compendium",
        description="Compile markdown ability blocks into dist/compendium.json.",
        command=[sys.executable, "tools/extract_compendium.py", "--repo", "."],
    ),
    ToolTask(
        task_id="lint-compendium",
        group="Lint",
        title="Lint Compendium",
        description="Validate compendium schema and linkage consistency.",
        command=[sys.executable, "tools/lint_compendium.py", "--repo", ".", "--compendium", "dist/compendium.json"],
    ),
    ToolTask(
        task_id="lint-roll-syntax",
        group="Lint",
        title="Lint Roll Syntax",
        description="Validate roll fields against roll expression grammar.",
        command=[sys.executable, "tools/lint_roll_syntax.py", "--repo", "."],
    ),
    ToolTask(
        task_id="lint-canon-terms",
        group="Lint",
        title="Lint Canon Terms",
        description="Scan markdown for non-canon term usage.",
        command=[sys.executable, "tools/lint_canon_terms.py", "--repo", "."],
    ),
    ToolTask(
        task_id="power-audit",
        group="Audit",
        title="Power Audit",
        description="Run sequence power/cost/control balance checks.",
        command=[
            sys.executable,
            "tools/power_audit.py",
            "--repo",
            ".",
            "--compendium",
            "dist/compendium.json",
            "--power-scale",
            "meta/power_scale.yml",
            "--out",
            "meta/power_audit_report.md",
            "--json-out",
            "meta/power_audit_report.json",
        ],
    ),
    ToolTask(
        task_id="congruence-audit",
        group="Audit",
        title="Congruence Audit",
        description="Find unresolved drift, collisions, and incongruence risks.",
        command=[
            sys.executable,
            "tools/congruence_audit.py",
            "--repo",
            ".",
            "--content-root",
            "draft",
            "--out",
            "reports/audit/congruence_report.md",
            "--json",
        ],
    ),
    ToolTask(
        task_id="heading-collisions",
        group="Audit",
        title="Find Heading Collisions",
        description="Identify repeated heading titles that create ambiguous wikilinks.",
        command=[sys.executable, "tools/find_heading_collisions.py", "--repo", ".", "--content-root", "draft"],
    ),
    ToolTask(
        task_id="ambiguous-wikilinks",
        group="Audit",
        title="Find Ambiguous Wikilinks",
        description="List unresolved/ambiguous [[Title]] references.",
        command=[sys.executable, "tools/find_ambiguous_wikilinks.py", "--repo", ".", "--content-root", "draft"],
    ),
]

TASK_MAP = {task.task_id: task for task in TASKS}
SERVICE_MAP = {svc.service_id: svc for svc in SERVICES}


def _utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def _make_run_id(prefix: str) -> str:
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{prefix}-{stamp}-{int(time.time() * 1000) % 100000}"


def _service_cmd(svc: ManagedService) -> List[str]:
    return [sys.executable, svc.script, *svc.args, "--port", str(svc.port)]


def _is_running(state: ServiceState) -> bool:
    return state.process is not None and state.process.poll() is None


def _ensure_dirs() -> None:
    RUNS_DIR.mkdir(parents=True, exist_ok=True)


def _start_service(service_id: str) -> None:
    svc = SERVICE_MAP[service_id]
    with LOCK:
        state = SERVICE_STATE.setdefault(service_id, ServiceState())
        if _is_running(state):
            return
        run_id = _make_run_id(f"service-{service_id}")
        log_path = RUNS_DIR / f"{run_id}.log"
        handle = log_path.open("w", encoding="utf-8")
        cmd = _service_cmd(svc)
        handle.write(f"[{_utc_now()}] start service: {svc.title}\n")
        handle.write(f"cwd: {ROOT}\n")
        handle.write(f"cmd: {' '.join(cmd)}\n\n")
        handle.flush()
        proc = subprocess.Popen(cmd, cwd=str(ROOT), stdout=handle, stderr=subprocess.STDOUT, text=True)
        state.process = proc
        state.started_at = dt.datetime.now(dt.timezone.utc)
        state.log_path = log_path
        state.log_handle = handle


def _stop_service(service_id: str) -> None:
    with LOCK:
        state = SERVICE_STATE.setdefault(service_id, ServiceState())
        proc = state.process
        if proc is None:
            return
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=5)
        if state.log_handle is not None:
            state.log_handle.write(f"\n[{_utc_now()}] service stopped\n")
            state.log_handle.flush()
            state.log_handle.close()
        state.process = None
        state.started_at = None
        state.log_handle = None


def _run_task(task: ToolTask) -> str:
    _ensure_dirs()
    run_id = _make_run_id(task.task_id)
    log_path = RUNS_DIR / f"{run_id}.log"
    started = dt.datetime.now(dt.timezone.utc)
    cmd = task.command
    timed_out = False

    try:
        result = subprocess.run(
            cmd,
            cwd=str(ROOT),
            text=True,
            capture_output=True,
            timeout=task.timeout_sec,
        )
        stdout = result.stdout or ""
        stderr = result.stderr or ""
        exit_code = result.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        exit_code = 124

    ended = dt.datetime.now(dt.timezone.utc)
    duration = (ended - started).total_seconds()
    merged = ""
    if stdout:
        merged += "=== stdout ===\n" + stdout.rstrip() + "\n\n"
    if stderr:
        merged += "=== stderr ===\n" + stderr.rstrip() + "\n\n"
    if not merged:
        merged = "(no output)\n"
    if timed_out:
        merged += f"\nTimed out after {task.timeout_sec}s.\n"

    with log_path.open("w", encoding="utf-8") as fh:
        fh.write(f"task: {task.title}\n")
        fh.write(f"time_utc: {started.isoformat()}\n")
        fh.write(f"cwd: {ROOT}\n")
        fh.write(f"cmd: {' '.join(cmd)}\n")
        fh.write(f"exit_code: {exit_code}\n")
        fh.write(f"duration_sec: {duration:.2f}\n\n")
        fh.write(merged)

    entry = {
        "run_id": run_id,
        "task_id": task.task_id,
        "title": task.title,
        "started": started,
        "duration_sec": duration,
        "exit_code": exit_code,
        "log_path": log_path,
    }
    with LOCK:
        RUN_HISTORY.insert(0, entry)
        del RUN_HISTORY[60:]
    return run_id


HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Development Hub</title>
  <style>
    :root { --bg:#0f1218; --panel:#171c25; --muted:#98a3b3; --line:#2b3443; --text:#ecf0f6; --ok:#59c07a; --bad:#ea6b6b; --accent:#4f9cff; }
    * { box-sizing:border-box; }
    body { margin:0; background:var(--bg); color:var(--text); font:14px/1.45 "Segoe UI", Roboto, Arial, sans-serif; }
    .wrap { max-width:1200px; margin:24px auto; padding:0 16px; }
    .row { display:grid; grid-template-columns:1fr; gap:14px; }
    @media (min-width:1000px) { .row { grid-template-columns:1fr 1fr; } }
    .card { background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:14px; }
    h1,h2,h3 { margin:0 0 10px 0; }
    h1 { font-size:22px; }
    h2 { font-size:16px; }
    .muted { color:var(--muted); }
    .toolbar { display:flex; gap:8px; flex-wrap:wrap; }
    button, .btn { border:1px solid var(--line); background:#202839; color:var(--text); border-radius:9px; padding:7px 10px; cursor:pointer; text-decoration:none; display:inline-block; }
    button:hover, .btn:hover { border-color:var(--accent); }
    .btn-stop { border-color:#6a2f2f; background:#332225; }
    .status-ok { color:var(--ok); font-weight:600; }
    .status-bad { color:var(--bad); font-weight:600; }
    table { width:100%; border-collapse:collapse; }
    th, td { border-bottom:1px solid var(--line); padding:8px 6px; text-align:left; vertical-align:top; }
    th { color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.05em; }
    code { background:#121723; border:1px solid var(--line); padding:1px 6px; border-radius:7px; }
    a { color:#8ec2ff; text-decoration:none; }
    a:hover { text-decoration:underline; }
    .run-ok { color:var(--ok); }
    .run-bad { color:var(--bad); }
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Development Hub</h1>
    <div class="muted">Repo: <code>{{ repo }}</code> | Runs: <code>{{ runs_dir }}</code></div>

    <div class="row" style="margin-top:14px;">
      <section class="card">
        <h2>Managed Services</h2>
        <table>
          <thead><tr><th>Service</th><th>Status</th><th>Actions</th></tr></thead>
          <tbody>
            {% for svc in services %}
            <tr>
              <td>
                <div><strong>{{ svc.title }}</strong></div>
                <div class="muted">{{ svc.description }}</div>
              </td>
              <td>
                {% if svc.running %}
                  <span class="status-ok">Running</span>
                {% else %}
                  <span class="status-bad">Stopped</span>
                {% endif %}
                {% if svc.started_at %}
                  <div class="muted">{{ svc.started_at }}</div>
                {% endif %}
              </td>
              <td>
                <div class="toolbar">
                  <form method="post" action="{{ url_for('service_start', service_id=svc.service_id) }}"><button type="submit">Start</button></form>
                  <form method="post" action="{{ url_for('service_stop', service_id=svc.service_id) }}"><button class="btn-stop" type="submit">Stop</button></form>
                  <a class="btn" target="_blank" href="http://127.0.0.1:{{ svc.port }}">Open</a>
                  {% if svc.log_rel %}
                    <a class="btn" href="{{ url_for('show_log', run_id=svc.log_run_id) }}">Log</a>
                  {% endif %}
                </div>
              </td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </section>

      <section class="card">
        <h2>One-Shot Tools</h2>
        <table>
          <thead><tr><th>Tool</th><th>Group</th><th>Action</th></tr></thead>
          <tbody>
            {% for task in tasks %}
            <tr>
              <td>
                <div><strong>{{ task.title }}</strong></div>
                <div class="muted">{{ task.description }}</div>
                <div class="muted"><code>{{ task.cmd }}</code></div>
              </td>
              <td>{{ task.group }}</td>
              <td>
                <form method="post" action="{{ url_for('run_task', task_id=task.task_id) }}">
                  <button type="submit">Run</button>
                </form>
              </td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </section>
    </div>

    <section class="card" style="margin-top:14px;">
      <h2>Recent Runs</h2>
      <table>
        <thead><tr><th>Task</th><th>Status</th><th>When</th><th>Duration</th><th>Output</th></tr></thead>
        <tbody>
          {% for run in runs %}
          <tr>
            <td>{{ run.title }}</td>
            <td>
              {% if run.exit_code == 0 %}
                <span class="run-ok">OK (0)</span>
              {% else %}
                <span class="run-bad">FAIL ({{ run.exit_code }})</span>
              {% endif %}
            </td>
            <td>{{ run.started }}</td>
            <td>{{ '%.2f'|format(run.duration_sec) }}s</td>
            <td><a href="{{ url_for('show_log', run_id=run.run_id) }}">View Log</a></td>
          </tr>
          {% endfor %}
          {% if runs|length == 0 %}
          <tr><td colspan="5" class="muted">No runs yet.</td></tr>
          {% endif %}
        </tbody>
      </table>
    </section>
  </div>
</body>
</html>
"""


@APP.route("/")
def home() -> str:
    with LOCK:
        services = []
        for svc in SERVICES:
            state = SERVICE_STATE.setdefault(svc.service_id, ServiceState())
            running = _is_running(state)
            log_run_id = None
            log_rel = None
            if state.log_path:
                log_run_id = state.log_path.stem
                try:
                    log_rel = str(state.log_path.relative_to(ROOT)).replace("\\", "/")
                except Exception:
                    log_rel = str(state.log_path)
            started = state.started_at.isoformat() if state.started_at else ""
            services.append(
                {
                    "service_id": svc.service_id,
                    "title": svc.title,
                    "description": svc.description,
                    "port": svc.port,
                    "running": running,
                    "started_at": started,
                    "log_run_id": log_run_id,
                    "log_rel": log_rel,
                }
            )
        runs = [
            {
                "run_id": r["run_id"],
                "title": r["title"],
                "started": r["started"].isoformat(),
                "duration_sec": r["duration_sec"],
                "exit_code": r["exit_code"],
            }
            for r in RUN_HISTORY
        ]
    tasks = [{"task_id": t.task_id, "group": t.group, "title": t.title, "description": t.description, "cmd": " ".join(t.command)} for t in TASKS]
    return render_template_string(
        HTML,
        repo=str(ROOT),
        runs_dir=str(RUNS_DIR),
        services=services,
        runs=runs,
        tasks=tasks,
    )


@APP.post("/run/<task_id>")
def run_task(task_id: str):
    task = TASK_MAP.get(task_id)
    if task is None:
        abort(404)
    run_id = _run_task(task)
    return redirect(url_for("show_log", run_id=run_id))


@APP.post("/service/<service_id>/start")
def service_start(service_id: str):
    if service_id not in SERVICE_MAP:
        abort(404)
    _start_service(service_id)
    return redirect(url_for("home"))


@APP.post("/service/<service_id>/stop")
def service_stop(service_id: str):
    if service_id not in SERVICE_MAP:
        abort(404)
    _stop_service(service_id)
    return redirect(url_for("home"))


@APP.route("/log/<run_id>")
def show_log(run_id: str):
    safe = urllib.parse.unquote(run_id).strip()
    if not safe or "/" in safe or "\\" in safe:
        abort(400)
    path = RUNS_DIR / f"{safe}.log"
    if not path.exists():
        abort(404)
    text = path.read_text(encoding="utf-8", errors="replace")
    page = f"""<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(safe)}</title>
    <style>body{{background:#0f1218;color:#ecf0f6;font:13px/1.5 Consolas,monospace;margin:0}} .top{{padding:10px;border-bottom:1px solid #2b3443}} pre{{margin:0;padding:14px;white-space:pre-wrap}}</style>
    </head><body><div class='top'><a href='/' style='color:#8ec2ff'>Back</a> | <code>{html.escape(str(path))}</code></div><pre>{html.escape(text)}</pre></body></html>"""
    return Response(page, mimetype="text/html")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Centralized development UI for rulebook tools.")
    parser.add_argument("--repo", type=str, default=".", help="Repo root that contains tools/, reports/, and markdown files.")
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8890)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args(argv)

    global ROOT, RUNS_DIR
    ROOT = Path(args.repo).resolve()
    if not ROOT.exists():
        print(f"[error] repo not found: {ROOT}", file=sys.stderr)
        return 2
    RUNS_DIR = ROOT / "reports" / "dev_hub_runs"
    _ensure_dirs()

    if not args.no_browser:
        try:
            webbrowser.open(f"http://{args.host}:{args.port}/", new=1)
        except Exception:
            pass

    APP.run(host=args.host, port=args.port, debug=False, threaded=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
