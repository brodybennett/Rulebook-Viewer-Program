How to use (clickthrough UI):

Put lotm_sanity_check.py in your repo root (same place as tag-registry.yml)

Run:

python lotm_sanity_check.py --serve --open


Then you’ll get a local page like:

Issues (click a file path to open it at that line)

Registry (browse registry files + anchors; click a file to open)

Files (list of build/**/*.md)

Default URL: http://127.0.0.1:8787/

If that port is busy:

python lotm_sanity_check.py --serve --port 8799 --open

Why this scales with your content additions

As you populate the existing files with more headings/anchors/links, the UI updates automatically:

new {#anchors} show up as “anchor exists in Markdown but missing from registry”

new [[links]] show as unresolved until you add titles/aliases

registry says status: exists but file is empty can be treated as info/warn/error

To silence placeholder noise:

python lotm_sanity_check.py --serve --placeholder-level ignore


If you run it once and paste the first page’s “ERROR/WARN” list here, I can tell you which ones are the real blockers vs normal “still filling content” warnings.

