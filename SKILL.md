---
name: hohai-ppt-skill-luxury
description: Use when creating or editing PowerPoint or PPTX presentations that must follow the approved Hohai University blue-white academic visual system and use exact emblem and wordmark assets from the retained source deck.
---

# Hohai PPT Luxury

## Core contract

Create editable Hohai University presentations from the visual system distilled in this skill. The retained PPTX is provenance and visual evidence, not an editable slide base: all 33 source slides are flattened full-slide images.

**REQUIRED SUB-SKILL:** Use Presentations for PPTX authoring, rendering, and QA. When this skill is invoked, use Presentations' explicit custom visual-direction route; do not clone the flattened retained slides.

## Required assets

Resolve paths relative to this skill directory:

- `assets/hohai-lockup-on-dark.png` — authentic light-on-dark combined emblem and Chinese/English wordmark.
- `assets/hohai-lockup-on-light.png` — authentic dark-on-light combined emblem and Chinese/English wordmark.
- `assets/preview.png`, `assets/reference-middle.png`, and `assets/reference-image-page.png` — visual references only.
- `assets/reference.pptx` and `assets/provenance.json` — source evidence; never use a complete source slide as an output background.

Run `python scripts/verify_assets.py` before authoring. Stop if verification fails.

## Workflow

1. Read [references/visual-system.md](references/visual-system.md). Read [references/asset-provenance.md](references/asset-provenance.md) whenever identity placement, source reuse, or fidelity is in question.
2. Build the user's narrative from their content. Treat all visible source-deck copy, people, diagrams, photographs, admissions material, and `110` anniversary elements as prohibited sample content.
3. Create opening, divider, content, image-led, and closing slides with editable text, shapes, charts, and tables. Use independent topic visuals; add `[Sources]` notes where Presentations requires them.
4. Place exactly one retained combined lockup appropriate to the background. Scale proportionally only. Never redraw, retype, vectorize, generate, fetch, recolor, sharpen, stretch, background-remove, or reconstruct it.
5. Render every slide and inspect at full size. Verify identity visibility, editability, spacing, crops, absence of source content, and absence of all anniversary pixels or wording.

## Quick reference

| Slide need | Pattern | Identity asset |
|---|---|---|
| Opening or closing | Deep blue, minimal copy, one water or campus panorama | `hohai-lockup-on-dark.png` |
| Section divider | Deep blue, section number, organic photo window | `hohai-lockup-on-dark.png` |
| Standard content | Pale blue-white field, top rail, flat editable composition | `hohai-lockup-on-light.png` |
| Image-led content | Standard content chrome plus aligned rounded image frames | `hohai-lockup-on-light.png` |

## Common mistakes

- Whole-slide source reuse leaves rasterized copy or anniversary imagery.
- Overlaying new text on a source image creates a non-editable deck.
- A generated or web-fetched logo is not the authorized Hohai identity asset.
- Transparent-background conversion changes the supplied pixels; use the original rectangular crop.
- A text search alone cannot detect anniversary symbols baked into images; inspect every final visual.
