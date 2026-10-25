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
