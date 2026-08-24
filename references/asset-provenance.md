# Asset Provenance and Identity Rules

## Retained source

`../assets/reference.pptx` is the user-authorized public copy of the supplied `河海大学.pptx`. Its SHA-256, byte size, inspection findings, renders, crop boxes, and derived-asset hashes are recorded in `../assets/provenance.json`.

The deck contains 33 slides and zero editable text shapes. Each slide is one 1280x720 raster image. This makes the deck reliable visual evidence but unsuitable for slide duplication and inherited-element editing.

## Authentic identity assets

The two combined lockups are deterministic rectangular crops from source renders:

- `../assets/hohai-lockup-on-dark.png`: source slide 1; light mark for deep-blue backgrounds.
- `../assets/hohai-lockup-on-light.png`: source slide 17; dark mark for pale backgrounds.

They preserve the source pixels and rectangular background. They were not upscaled, background-removed, traced, redrawn, retyped, recolored, sharpened, or generated.

## Placement contract

- Choose the asset whose retained background matches the slide field.
- Scale proportionally only. Keep the image's width-to-height ratio unchanged.
- Do not crop inside the asset or separate the emblem from the wordmark.
- Do not manufacture transparent, vector, monochrome, outlined, or alternate-color versions.
- Do not substitute any web result, generated image, remembered logo, typed school name, or mark copied from a newly generated preview.
- If neither retained background fits a proposed slide, change the slide field rather than changing the identity asset.

Run `python scripts/verify_assets.py` after cloning and before every identity-sensitive deck build. A hash failure means the source or crop has changed and authoring must stop.

## Source-content boundary

The repository retains three full source renders so an agent can understand composition. Their visible copy and imagery are examples, not output assets. Only the two declared combined-lockup files may be copied from this repository into a generated deck.

The retained source includes `110` anniversary material. Do not copy or derive any anniversary text, icons, numerals, ribbons, slogans, or decorative motifs. Pixel-level visual inspection is required because those elements may be baked into raster images.

