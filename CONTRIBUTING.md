# Contributing to LOTM Rulebook Viewer

Thanks for helping keep this fan project organized and readable. Please keep everything non-commercial and respect the *Lord of the Mysteries* IP.

## Quick start
1. Clone or fork the repo.
2. Install deps: `pip install flask pyyaml mistune`.
3. Run the viewer: `python "VSCODE MD Files/rulebook_viewer.py" --source "VSCODE MD Files"`.
4. Optional checker: `python "VSCODE MD Files/lotm_sanity_check.py" --serve --open`.

## Writing content
- Follow `style-guide.md` for headings, tone, and formatting.
- Add `{#anchors}` to new sections and register them in `tag-registry.yml`.
- Keep file placement consistent with `build/` structure and existing sequences.
- Prefer examples and rules text over placeholders; mark drafts clearly.

## Testing your changes
- Run the sanity checker to catch missing anchors or unresolved wiki-links.
- Skim the viewer to confirm navigation, search hits, and anchor links behave as expected.

## Submitting changes
- Keep commits focused and include a short rationale.
- Note any new anchors or IDs in your summary so reviewers can double-check registry updates.
- Do not add any monetization, ads, or licensing terms that conflict with the non-commercial notice in `LICENSE.md`.

## Attribution and IP
- This is an unofficial, non-commercial fan project; do not imply endorsement by the *Lord of the Mysteries* rights holders.
- If you include external material, ensure you have permission and cite the source in-line where appropriate.
