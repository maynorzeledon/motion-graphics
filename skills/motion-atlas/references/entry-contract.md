# Entry contract

## Status

- `planned`: collection target only.
- `reference`: actual reference supplied or linked.
- `building`: implementation in progress.
- `ready`: implementation rendered and reviewed.

## Files

Use the repository's `templates/entry.json`. Keep an entry under `entries/<slug>/`. Include original reference links or permitted small files, rendered preview, representative frames, source, renderer/dependency versions, controls, and provenance. Keep relative paths rooted at the entry folder. Map the manifest's `catalogId` to an existing taxonomy leaf ID; multiple implementations may reference one catalog ID.

`dist/catalog.json` is the shared taxonomy; its initial status fields are defaults. Browser progress exports overlay those defaults and are local until deliberately committed or merged. Read the newest provided progress export when using collection notes.

For style references, collect actual examples and record typography, palette, composition, timing, transitions, camera, texture, and sound. For maps, record projection, bounds, boundary date, disputed region handling, layer source, labels, route data, and attribution. Font entries require actual font files or source links and license records; a named font in the checklist is not installed.

## Story and editing studies

Use `templates/story-study.json` in the repository for creator studies. Keep `studyType`, `creator`, `script`, `visuals`, and `structure` distinct. Record timestamped spoken text, visible action, narrative purpose, open loops, and payoffs. Separate how the story is constructed from how its shots are edited. Creator folders are study prompts until reference material has actually been examined. Device-local media is in IndexedDB; full library backups include its bytes, while older progress exports may omit files.

To inspect uploaded files from a browser backup, run `python3 scripts/unpack_backup.py <backup.json> --output <new-entry-directory>` from the repository root, then inspect restored manifests and files. Never paste a large base64 media payload into the context window.
