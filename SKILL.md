---
name: hohai-ppt-skill-luxury
description: Use when creating or editing PowerPoint or PPTX presentations that must follow the approved Hohai University blue-white academic visual system and use the exact user-authorized emblem and combined wordmark assets retained by this skill.
---

# Hohai PPT Luxury

## Core contract

Create editable Hohai University presentations from the visual system distilled in this skill. The retained PPTX is provenance and visual evidence, not an editable slide base: all 33 source slides are flattened full-slide images.

## The identity rule (first principles)

The authorized combined lockup exists in two transparent colorways:

- `assets/hohai-lockup-blue-transparent.png` — blue artwork, for **light** backgrounds (pure white, pale blue field).
- `assets/hohai-lockup-white-transparent.png` — white artwork, for **dark** backgrounds (deep Hohai blue).

Both files have fully transparent backgrounds, so no white rectangle can ever appear. Placement is one contrast match: **light background → blue version; dark background → white version.** Never cross the colorways — blue on dark or white on light renders the lockup invisible. No rails, plates, or mats are needed, and adding one is prohibited: it reintroduces the white-rectangle problem the transparent assets exist to solve.

`assets/hohai-lockup-authorized.jpg` (blue artwork on a white field) is the archival original: use it only on a pure `#FFFFFF` background when the transparent set is unavailable — the transparent PNG is otherwise always preferred.

**REQUIRED SUB-SKILL:** Use Presentations for PPTX authoring, rendering, and QA. When this skill is invoked, use Presentations' explicit custom visual-direction route; do not clone the flattened retained slides.

## Required assets

Resolve paths relative to this skill directory:

- `assets/hohai-lockup-blue-transparent.png` — combined lockup, blue artwork on transparent background; the default for light backgrounds.
- `assets/hohai-lockup-white-transparent.png` — combined lockup, white artwork on transparent background; the default for dark backgrounds.
- `assets/hohai-lockup-authorized.jpg` — archival original, blue artwork on a white field; only for pure-white backgrounds.
- `assets/hohai-emblem-authorized.png` — optional exact standalone emblem supplied and authorized by the user; it has transparent outer padding.
- `assets/hohai-lockup-on-dark.png` and `assets/hohai-lockup-on-light.png` — retained source-deck crops for provenance comparison only, not output identity assets.
- `assets/preview.png`, `assets/reference-middle.png`, and `assets/reference-image-page.png` — visual references only.
- `assets/reference.pptx` and `assets/provenance.json` — source evidence; never use a complete source slide as an output background.

Run `python scripts/verify_assets.py` before authoring. If `python` is unavailable or blocked, use the Python executable returned by the workspace dependency loader; the interpreter must provide Pillow. Stop if verification fails.

## Workflow

1. Read [references/visual-system.md](references/visual-system.md). Read [references/asset-provenance.md](references/asset-provenance.md) whenever identity placement, source reuse, or fidelity is in question.
2. Build the user's narrative from their content. Treat all visible source-deck copy, people, diagrams, photographs, admissions material, and `110` anniversary elements as prohibited sample content.
3. Create opening, divider, content, image-led, and closing slides with editable text, shapes, charts, and tables. Divider and content backgrounds use the retained photograph `assets/photos/three-gorges-dam.jpg` under a semi-transparent white overlay — ≈88% opacity on the divider, ≈83% on content pages. It is CC BY-SA 2.0 (Thomas Bächinger / Wikimedia Commons): record that attribution in the slide's `[Sources]` notes. Use independent topic visuals elsewhere.
4. Place the combined lockup exactly once on every slide, choosing the colorway by background: `hohai-lockup-blue-transparent.png` on light backgrounds, `hohai-lockup-white-transparent.png` on dark backgrounds; place it directly — never add a plate, rail, or mat behind it — and keep clear space of at least 25% of the lockup's height on all sides. Scale proportionally only. `assets/hohai-emblem-authorized.png` is optional and may be PowerPoint-cropped only to its declared transparent-margin `content_bbox`; never crop visible emblem pixels. Omit the optional emblem when it would merely duplicate the emblem already present in the combined lockup. Never redraw, retype, vectorize, generate, fetch, recolor, sharpen, stretch, background-remove, or reconstruct either asset.
5. Render every slide and inspect at full size. Verify identity visibility, editability, spacing, crops, absence of source content, and absence of all anniversary pixels or wording. For identity: zoom to 100% on each lockup — the colorway must contrast with its background, and no white rectangle may sit behind or around any lockup.

## Quick reference

| Slide need | Pattern | Identity placement |
|---|---|---|
| Opening or closing | Deep-blue gradient, minimal copy, one water or campus panorama | `hohai-lockup-white-transparent.png` directly on the blue, top center or upper right |
| Section divider | Retained dam photo under ≈88% white wash; oversized section number, two-line title | `hohai-lockup-blue-transparent.png` directly on the wash, top center or upper right |
| Standard content | Same photo under ≈83% white wash, thin top rule | `hohai-lockup-blue-transparent.png` directly on the wash, upper right |
| Image-led content | Standard content chrome plus aligned rounded image frames | `hohai-lockup-blue-transparent.png` directly on the wash, upper right |

## Common mistakes

- Whole-slide source reuse leaves rasterized copy or anniversary imagery.
- Overlaying new text on a source image creates a non-editable deck.
- A generated or web-fetched logo is not the authorized Hohai identity asset.
- Changing the transparent assets' visible pixels or recoloring them breaks the authorized assets.
- Crossing colorways — blue version on a dark background or white version on a light background — makes the lockup invisible.
- Adding any plate, rail, or mat behind a transparent lockup — white or tinted — reintroduces the white-rectangle sticker problem; place the lockup directly.
- A text search alone cannot detect anniversary symbols baked into images; inspect every final visual.
