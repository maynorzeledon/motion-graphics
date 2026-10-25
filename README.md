# Motion Atlas

Your expandable motion design reference library. Start with a collection checklist; grow it into a searchable set of references, previews, reusable code, and finished scenes.

**1,444 collection entries · 12 categories · nested browser · portable AI instructions**

## Browse

The website is in `dist/`. Run `npm run serve` and open `http://localhost:3000`. It is buildless and has no npm dependencies. Deploy `dist/` on any static host. Use the cards to explore or switch to the expandable tree. Search, filter by status, save favorites, add custom entries, and record notes and reference links.

Progress is stored in the current browser, not automatically committed to GitHub or synced across devices. Use **Export progress** for a JSON backup; import merges it with local progress. Send an export into our chat when you want changes committed. Do not store sensitive notes in this public repository.

## Categories

1. Animations — controls, platform UI, typography, objects, characters, backgrounds, data.
2. Maps and geography — projections, terrain, satellite layers, boundaries, roads, rail, flight arcs, routes, camera moves, data preparation.
3. 2D assets — devices, characters, objects, environments, UI kits, icons, textures.
4. 3D assets — phones, computers, audio devices, models, materials, rigs.
5. Sound effects — feedback, movement, impacts, ambience, technology, voices.
6. Music — moods, genres, use cases, stems and edits.
7. Fonts and typography — families, multilingual support, type systems.
8. Transitions and effects — spatial, masked, optical, digital, physics, color.
9. Styles and inspiration — named creator and brand references plus visual languages, broken into concrete techniques.
10. Video formats and scenes — social videos, documentaries, ads, broadcast packages.
11. Production building blocks — camera, lighting, motion mechanics, delivery.
12. Code recipes and integrations — implementation and rendering approaches.

Browse the full [text checklist](docs/CATALOG.md). Edit `scripts/build_catalog.py`, then run `npm run build` to regenerate the catalog and checklist. IDs derive from the full hierarchy: preserve existing names and IDs when possible because saved progress uses IDs.

## Add a real reference later

1. Pick a specific entry and add the original creator/source link and notes.
2. Set it to **Reference collected** only after a real reference is available.
3. When implementation begins, use **Building**.
4. Put files in `entries/<entry-slug>/` using [the entry template](templates/entry.json).
5. Keep preview, code, dependencies, parameters, and source/license information together.
6. Mark **Ready to reuse** after rendering and reviewing the implementation.

Recommended entry layout:

```text
entries/<entry-slug>/
  entry.json
  references/        # small permitted reference files or source-links.json
  previews/          # lightweight preview / contact sheet
  src/               # animation implementation
  assets/            # dependencies used by this entry
```

Keep large source videos outside Git initially; record their URLs or storage paths. Later we can choose Git LFS or object storage. A folder is only created when there is something to collect—1,444 empty folders would add clutter.

## Use with an AI

Read [AGENTS.md](AGENTS.md), or point Claude at [CLAUDE.md](CLAUDE.md). The reusable skill lives under `skills/motion-atlas/`; copy that folder into the tool's supported skills location if needed. No proprietary runtime is required. This is a retrieval/reference system: adding examples does not train model weights. A model needs access to the repository and the files it will inspect.

Search locally with `python3 scripts/search_catalog.py "globe"` or `rg "route" docs/CATALOG.md`. Planned entries are a wishlist, not working animation code.

## Checks

`npm run check` validates JavaScript syntax and taxonomy structure. `python3 .../quick_validate.py skills/motion-atlas` can validate the optional skill metadata in an environment with the skill creator tooling.

The initial catalog includes no copied third party code, fonts, music, or video. Names identify collection targets and references, not bundled assets or affiliation. When importing from other repositories, preserve each license and attribution in `THIRD_PARTY.md` and the entry metadata. Exact creator references can be added later; currently named styles are descriptive technique checklists.
