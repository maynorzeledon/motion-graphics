# Motion Atlas: agent instructions

Read `skills/motion-atlas/SKILL.md` for the retrieval workflow. Use `dist/catalog.json` as the taxonomy and `entries/*/entry.json` as collected implementation manifests. All initial taxonomy leaves are planned; do not claim they contain code or playable references.

For requested edits, preserve stable IDs and unrelated entries. Edit `scripts/build_catalog.py` for taxonomy, regenerate outputs, and run `npm run check`. Website edits belong in `dist/` and require no package installation. Never overwrite a progress export with regenerated planned defaults. The browser saves locally; only explicit repository commits persist shared changes.

When adding examples, keep the original reference, recreation notes, preview, implementation, dependency versions, asset/license records, and editable parameters together. Prefer small previews and external pointers for large media. Do not invent source links or label placeholder code as ready. Decompose named styles into observable techniques and use real evidence when supplied. Keep implementations deterministic and explain renderer-specific setup.
