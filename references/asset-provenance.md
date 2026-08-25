# Asset Provenance and Identity Rules

## Retained source

`../assets/reference.pptx` is the user-authorized public copy of the supplied `河海大学.pptx`. Its SHA-256, byte size, inspection findings, renders, crop boxes, and derived-asset hashes are recorded in `../assets/provenance.json`.

The deck contains 33 slides and zero editable text shapes. Each slide is one 1280x720 raster image. This makes the deck reliable visual evidence but unsuitable for slide duplication and inherited-element editing.

## User-authorized identity assets

The output identity assets are exact copies of the images the user supplied and authorized:

- `../assets/hohai-lockup-blue-transparent.png`: combined emblem plus Chinese/English school-name lockup, blue artwork on a fully transparent background (authorized 2026-08-25); the default for light backgrounds.
- `../assets/hohai-lockup-white-transparent.png`: combined lockup, white artwork on a fully transparent background (authorized 2026-08-25); the default for dark backgrounds.
- `../assets/hohai-lockup-authorized.jpg`: archival original, blue artwork on a white field (authorized 2026-08-24); only for pure-white backgrounds.
- `../assets/hohai-emblem-authorized.png`: optional standalone blue emblem with transparent outer padding.

They were not cropped, upscaled, background-removed, traced, redrawn, retyped, recolored, sharpened, or generated. The older `hohai-lockup-on-dark.png` and `hohai-lockup-on-light.png` files remain solely as source-deck provenance crops.

## Placement contract

- Place the combined lockup exactly once on every slide; do not split the emblem from the wordmark.
- Match the colorway to the background: `hohai-lockup-blue-transparent.png` on light backgrounds, `hohai-lockup-white-transparent.png` on dark backgrounds. Both are fully transparent — place them directly with no plate, rail, or mat; adding a white rectangle behind the lockup is prohibited.
- Never cross colorways: blue artwork on dark or white artwork on light is invisible.
- Use the archival JPEG only on a pure `#FFFFFF` background, where its white field is invisible.
- Scale proportionally only. Keep the image's width-to-height ratio unchanged.
- Do not crop inside the combined lockups or separate the emblem from the wordmark.
- The standalone PNG is optional. If its empty margins obstruct placement, use PowerPoint's non-destructive crop to the declared `content_bbox` `[370, 340, 848, 817]`; never crop visible emblem pixels.
- Do not manufacture transparent, vector, monochrome, outlined, or alternate-color versions.
- Do not substitute any web result, generated image, remembered logo, typed school name, or mark copied from a newly generated preview.
- If a lockup does not fit a proposed slide, change the slide's identity area rather than changing the asset.

Run `python scripts/verify_assets.py` after cloning and before every identity-sensitive deck build. A hash failure means the source or crop has changed and authoring must stop.

## Source-content boundary

The repository retains three full source renders and two exact source-deck identity crops so an agent can understand composition and verify lineage. Their visible copy and imagery are examples, not output assets. Only the four user-authorized identity files declared under `identity_assets` may enter a generated deck as identity marks.

Divider and content photo backgrounds are external, not retained here: use only free-licensed photographs (e.g. Wikimedia Commons, CC/public-domain), and record license plus attribution in the deck's `[Sources]` notes.

The retained source includes `110` anniversary material. Do not copy or derive any anniversary text, icons, numerals, ribbons, slogans, or decorative motifs. Pixel-level visual inspection is required because those elements may be baked into raster images.
