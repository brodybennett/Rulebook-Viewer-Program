# TODO / Known Issues

## P0 (release blockers)
- Improve anchor validation in `rulebook_viewer.py`: surface duplicate `{#id}` collisions and show the offending files in the UI, not just server logs.
- Add basic automated smoke test (load index, render one page) to catch Flask startup errors after dependency bumps.

## P1 (quality)
- Search ranking: prioritize exact title matches and heading-level boosts so sidebar titles outrank body hits.
- Zip source cleanup: after serving from a zip, offer a CLI flag to auto-delete the extracted temp folder on exit.
- Accessibility: ensure sidebar contrast and focus states meet WCAG AA; add skip-to-content link.

## P2 (nice-to-have)
- Dark theme toggle using the existing `viewer_theme.css` tokens.
- Keyboard shortcuts: `/` to focus search, `[`/`]` to move between heading anchors in the current page.
- Add example content template to `_templates/` for new rule sections with required front matter and anchor pattern.
