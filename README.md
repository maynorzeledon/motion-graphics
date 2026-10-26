# Motion Atlas

Your expandable motion design reference library. Start with a collection checklist; grow it into a searchable set of references, previews, reusable code, and finished scenes.

**4,923 collection entries · 27 categories · nested browser · portable AI instructions**

## Browse

The website is in `dist/`. Run `npm run serve` and open `http://localhost:3000`. It is buildless and has no npm dependencies. Deploy `dist/` on any static host. Use the cards to explore or switch to the expandable tree. Search, filter by status, save favorites, add custom entries, and record notes and reference links.

Entry notes are saved in browser storage; uploaded files are saved in IndexedDB on this device. Neither automatically syncs to GitHub or other devices. **Export library backup** includes entry metadata and uploaded file bytes in one JSON backup. **Import backup** merges progress and restores those files. Older metadata-only progress exports remain supported. Send a backup into our chat when you want material committed. Do not store sensitive notes in this public repository.

Open any entry to add videos, images, scripts, source code, or storyboards (up to 100 MB per file). The file-role selector distinguishes reference footage, transcript, visual breakdown, and other assets. Video, audio, common raster images, and text/code files have local viewers; other files can be downloaded. File attachments persist independently of the Save entry button. Use reference links for larger source videos.

## Storytelling versus editing styles

**Storytelling** studies what makes the story work: premise, hook, information order, stakes, escalation, open loops, causal progression, punchline, and payoff. **Styles and inspiration** studies how it looks and sounds: camera, composition, typography, transitions, color, sound, and visual rhythm. Keep a creator in both collections when useful; link the same reference in each. Each entry has a study type, creator name, script/transcript, visual beat sheet, and reusable structure notes.

The catalog includes 37 creator/platform study folders. These are prompts for analysis, not completed or verified descriptions of a creator’s formula. See `docs/CREATOR_STUDIES.md` and `templates/story-study.json`.

Card navigation now opens every folder level; use the breadcrumbs or the expandable tree to move through the hierarchy. Existing entry IDs were retained so saved progress continues to match.

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
13. Color grading and looks — series-inspired grades, filter families, LUTs, and color controls.
14. Textures — surfaces, print, film, animated overlays, and 3D texture maps.
15. B-roll — subject collections, shot types, editorial purpose, and delivery.
16. Meme clips and reactions — reactions, named references, comedic timing, and edit formats.
17. Archival media and documents — historical material, evidence, and source records.
18. Photography and cutouts — portraits, objects, isolated layers, and photo animation preparation.
19. VFX and compositing — practical elements, keying, tracking, and scene integration.
20. Palettes and design systems — reusable color, layout, brand, and composition recipes.
21. Storytelling — creator studies, hooks, story progression, scripts, visual breakdowns, and payoffs.
22. Captions and localization — caption styles, translation, and accessibility.
23. Voiceover and narration — voice direction, recording, pronunciation, and timing.
24. Comments and replies — Gen Z and internet humor, brand voices, wordplay, thoughtful replies, context, and thread analysis.
25. Meme templates — blank image macros, editable caption slots, meme-news cards, and reusable joke layouts.
26. Reply GIFs, images and stickers — reactions organized by emotion, intent, format, and use context.
27. Personal B-roll — self-filmed everyday actions, specific camera angles, solo shot lists, and action sequences.

Browse the full [text checklist](docs/CATALOG.md). Edit the catalog modules in `scripts/`, then run `npm run build` to regenerate the catalog and checklist. IDs derive from the full hierarchy: preserve existing names and IDs when possible because saved progress uses IDs.

## Comments and replies

Use the Comments and replies tab to collect examples with their original video, parent comment, reply, voice, and explanation. Each entry has dedicated fields for context, reply text, analysis, and observed response. Attach thread screenshots and reference clips using the file-role selector. See `templates/comment-study.json` and `skills/motion-atlas/references/comments-and-replies.md`. Actual examples and likes are not pre-filled; checklist entries are collection targets.

## Joke and comedy studies

Storytelling → Comedy formats contains Literal jokes, Dad jokes, relatable everyday moments and canon events, puns, one-liners, knock-knock jokes, anti-jokes, deadpan, misdirection, observational humor, surreal humor, physical comedy, irony, parody, satire, callbacks, and more. Each family has folders for mechanics, delivery, and reference studies. Read `skills/motion-atlas/references/comedy-formats.md` when using these patterns.

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

Keep large source videos outside Git initially; record their URLs or storage paths. Device-local uploads are available for smaller references; export a backup before clearing browser data. Later we can choose Git LFS or object storage. A folder is only created when there is something to collect—4,923 empty folders would add clutter.

## Use with an AI

Read [AGENTS.md](AGENTS.md), or point Claude at [CLAUDE.md](CLAUDE.md). The reusable skill lives under `skills/motion-atlas/`; copy that folder into the tool's supported skills location if needed. No proprietary runtime is required. This is a retrieval/reference system: adding examples does not train model weights. A model needs access to the repository and the files it will inspect.

Convert a browser backup into portable entry folders with `python3 scripts/unpack_backup.py motion-atlas-library-backup.json --output entries`. The unpacker restores scripts and file attachments, keeps source filenames in metadata, and refuses to overwrite different existing files.

Search locally with `python3 scripts/search_catalog.py "globe"` or `rg "route" docs/CATALOG.md`. Planned entries are a wishlist, not working animation code.

## Checks

`npm run check` validates JavaScript syntax and taxonomy structure. `python3 .../quick_validate.py skills/motion-atlas` can validate the optional skill metadata in an environment with the skill creator tooling.

The catalog includes a user-supplied meme-news screenshot and a lightweight preview of a user-supplied filmmaking video as collected references. It includes no copied third party code, fonts, or music. Names identify collection targets and references, not bundled assets or affiliation. When importing from other repositories, preserve each license and attribution in `THIRD_PARTY.md` and the entry metadata. Exact creator references can be added later; currently named styles are descriptive technique checklists.
