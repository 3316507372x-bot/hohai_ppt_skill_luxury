---
name: hohai-ppt-skill-luxury
description: Use when creating or editing PowerPoint or PPTX presentations that must follow the approved Hohai University blue-white academic visual system and use the exact user-authorized emblem and combined wordmark assets retained by this skill.
---

# Hohai PPT Luxury

## Core contract

Create editable Hohai University presentations from the visual system distilled in this skill. The retained PPTX is provenance and visual evidence, not an editable slide base: all 33 source slides are flattened full-slide images.

**Background invariant:** every slide's base fill is solid pure white `#FFFFFF` — opening, divider, content, image-led, and closing alike. No gradients, tints, pale-blue fields, or colored panels may act as a slide background. Hohai blue lives in type, rules, strips, frames, and imagery only. No exceptions.

**REQUIRED SUB-SKILL:** Use Presentations for PPTX authoring, rendering, and QA. When this skill is invoked, use Presentations' explicit custom visual-direction route; do not clone the flattened retained slides.

## Required assets

Resolve paths relative to this skill directory:

- `assets/hohai-lockup-authorized.jpg` — primary exact combined emblem plus Chinese/English school-name lockup supplied and authorized by the user.
- `assets/hohai-emblem-authorized.png` — optional exact standalone emblem supplied and authorized by the user; it has transparent outer padding.
- `assets/hohai-lockup-on-dark.png` and `assets/hohai-lockup-on-light.png` — retained source-deck crops for provenance comparison only, not output identity assets.
- `assets/preview.png`, `assets/reference-middle.png`, and `assets/reference-image-page.png` — visual references only.
- `assets/reference.pptx` and `assets/provenance.json` — source evidence; never use a complete source slide as an output background.

Run `python scripts/verify_assets.py` before authoring. If `python` is unavailable or blocked, use the Python executable returned by the workspace dependency loader; the interpreter must provide Pillow. Stop if verification fails.

## Workflow

1. Read [references/visual-system.md](references/visual-system.md). Read [references/asset-provenance.md](references/asset-provenance.md) whenever identity placement, source reuse, or fidelity is in question.
2. Build the user's narrative from their content. Treat all visible source-deck copy, people, diagrams, photographs, admissions material, and `110` anniversary elements as prohibited sample content.
3. Create opening, divider, content, image-led, and closing slides with editable text, shapes, charts, and tables. Use independent topic visuals; add `[Sources]` notes where Presentations requires them.
4. Place `assets/hohai-lockup-authorized.jpg` exactly once on every slide. Because every slide background is pure white, place the lockup directly on the background with no plate or rail behind it. Scale proportionally only. `assets/hohai-emblem-authorized.png` is optional and may be PowerPoint-cropped only to its declared transparent-margin `content_bbox`; never crop visible emblem pixels. Omit the optional emblem when it would merely duplicate the emblem already present in the combined lockup. Never redraw, retype, vectorize, generate, fetch, recolor, sharpen, stretch, background-remove, or reconstruct either asset.
5. Render every slide and inspect at full size. Verify identity visibility, editability, spacing, crops, absence of source content, and absence of all anniversary pixels or wording.

## Quick reference

| Slide need | Pattern | Identity asset |
|---|---|---|
| Opening or closing | Pure white field, deep-blue display type, one water or campus panorama | `hohai-lockup-authorized.jpg` directly on the white background |
| Section divider | Pure white field, oversized blue section number, organic photo window | `hohai-lockup-authorized.jpg` directly on the white background |
| Standard content | Pure white field, thin blue top rule, flat editable composition | `hohai-lockup-authorized.jpg` directly on the white background |
| Image-led content | Standard content chrome plus aligned rounded image frames | `hohai-lockup-authorized.jpg` directly on the white background |

## Common mistakes

- Whole-slide source reuse leaves rasterized copy or anniversary imagery.
- Overlaying new text on a source image creates a non-editable deck.
- A generated or web-fetched logo is not the authorized Hohai identity asset.
- Removing the JPEG's white field or changing the PNG's visible pixels breaks the authorized assets.
- Using deep-blue gradients, solid blue fields, or pale-blue fills as slide backgrounds is a legacy pattern and prohibited; only solid `#FFFFFF` backgrounds are allowed.
- A text search alone cannot detect anniversary symbols baked into images; inspect every final visual.
