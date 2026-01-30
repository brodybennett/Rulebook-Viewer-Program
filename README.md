# LOTM Rulebook Viewer

A community-driven tabletop RPG rulebook inspired by Lord of the Mysteries, focused on structured mechanics and clean UI-ready formatting.

- Current state: Early-draft rules with scaffolded Markdown files; viewer MVP and registry already working for browsing and link checks.
- What makes this unique: Wiki-link and anchor-aware workflow with a tag registry to keep references consistent; single-file, read-only Flask viewer that runs locally without touching your files.
- Goal: Deliver a playable fan project with publishable Markdown that can be skinned for the table or a future web UI.

## What is this?
- A curated set of Markdown rulebook chapters under `build/` plus supporting assets (`viewer_theme.css`, `tag-registry.yml`, `style-guide.md`).
- `rulebook_viewer.py`: a single-file Flask app that renders the rulebook with sidebar navigation, search, anchors, and wiki-link resolution.
- `lotm_sanity_check.py`: a helper that surfaces missing anchors, unresolved wiki-links, and empty planned files.

## Why does it exist?
- To keep the homebrew LOTM system readable and consistent while it grows.
- To ensure every mechanic and lore reference has an anchor or id that survives copy-paste into other tools.
- To provide a local, zero-write viewer so contributors can explore without risking edits.

## What do you want help with?
- Filling out the Markdown stubs with rules text, examples, and balance notes that match `style-guide.md`.
- Adding or confirming anchors in `tag-registry.yml` when new sections are created.
- Running the viewer and sanity checker on Windows/macOS/Linux to report broken links, layout bugs, or confusing UX.
- Proposing structure tweaks to the navigation order under `build/` so new players can onboard faster.

## Start in 5 minutes
1) Install Python 3.10+.
2) Install deps: `pip install flask pyyaml mistune`.
3) From the repo root, launch the viewer: `python "VSCODE MD Files/rulebook_viewer.py" --source "VSCODE MD Files"` (add `--no-browser` if you do not want auto-open).
4) Open http://127.0.0.1:7860/ (or the printed host/port) to browse; search, sidebar, and wiki-links are live.
5) Optional: run the checker for a quick issues list: `python "VSCODE MD Files/lotm_sanity_check.py" --serve --open`.

## Common commands
- Change port: `python "VSCODE MD Files/rulebook_viewer.py" --port 8799 --source "VSCODE MD Files"`.
- Ignore placeholder noise in the checker: `python "VSCODE MD Files/lotm_sanity_check.py" --serve --placeholder-level ignore`.
- Serve a zipped snapshot instead of the working tree: `python "VSCODE MD Files/rulebook_viewer.py" --source path/to/VSCODE MD Files.zip`.

## Project layout
- `build/` - rulebook chapters and sequences (Markdown).
- `tag-registry.yml` - canonical anchors and status for every section.
- `style-guide.md` - formatting and tagging rules for contributors.
- `viewer_theme.css` / `viewer_theme.js` - theme and UI behavior for the viewer.
