# Hohai PPT Skill Luxury Design

## Goal

Create a portable Codex skill repository named `hohai_ppt_skill_luxury` that produces editable PowerPoint decks in the approved Hohai University blue-white academic style while using only authentic emblem/wordmark pixels cropped from the supplied source PPTX.

## Confirmed requirements

- The GitHub repository is public and named `hohai_ppt_skill_luxury`.
- The source file `河海大学.pptx` may be retained and uploaded publicly.
- The internal Codex skill name is `hohai-ppt-skill-luxury`; underscores are invalid in skill frontmatter.
- The source deck controls visual style and brand identity only. Its narrative, copy, people, diagrams, charts, photographs, admissions material, and 110-anniversary elements are not reusable content.
- The exact combined Hohai emblem, Chinese school name, and English wordmark must be cropped from source PPT slide renders. Generated, redrawn, retyped, vectorized, web-fetched, recolored, or reconstructed substitutes are forbidden.
- The approved visual family includes a deep-blue photographic opening, blue-white editable content pages, dark-blue section dividers, image-led pages, and a restrained deep-blue closing.

## Source constraint

The reference contains 33 slides. Each slide is a single 1280x720 raster image and exposes zero editable text shapes. Therefore the retained PPTX is evidence and provenance, not an editable template base. The skill must not duplicate or use any complete source slide as an output background.

## Architecture

The repository root is the installable skill. `SKILL.md` provides concise routing and non-negotiable identity rules. `references/visual-system.md` defines slide families, palette, typography hierarchy, geometry, and content replacement behavior. `references/asset-provenance.md` explains the flattened source and exact brand extraction contract. `assets/` retains the public source PPTX, representative source renders, two authentic combined lockups, and a machine-readable provenance manifest. `scripts/verify_assets.py` verifies hashes, dimensions, crop provenance, and prohibited asset substitutions.

The skill establishes an explicit custom visual direction for new presentations. It does not invoke exact-clone template-following against the flattened source. New decks use editable presentation primitives and external or generated topic visuals, while authentic Hohai identity is inserted only from the retained crops.

## Repository structure

```text
hohai_ppt_skill_luxury/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── reference.pptx
│   ├── preview.png
│   ├── reference-middle.png
│   ├── reference-image-page.png
│   ├── hohai-lockup-on-dark.png
│   ├── hohai-lockup-on-light.png
│   └── provenance.json
├── references/
│   ├── visual-system.md
│   └── asset-provenance.md
├── scripts/verify_assets.py
├── tests/test_asset_integrity.py
├── README.md
└── NOTICE.md
```

## Identity asset contract

- `hohai-lockup-on-dark.png` is an unscaled rectangular crop from the source cover render.
- `hohai-lockup-on-light.png` is an unscaled rectangular crop from a source content-page render.
- Each crop keeps its original background, pixel dimensions, colors, and aspect ratio.
- Placement may scale proportionally only. Cropping, stretching, recoloring, sharpening, tracing, background removal, or regeneration fails acceptance.
- `assets/provenance.json` records original filename, source SHA-256, source slide, crop box, output dimensions, and asset SHA-256.

## Page families

1. **Opening:** deep Hohai-blue gradient, authentic light-on-dark lockup, minimal title/subtitle, one water-engineering or campus panorama, restrained light ribbons.
2. **Section divider:** deep blue field, small section number, concise title, organic photographic window, faint contour or water-line decoration.
3. **Content:** pale blue-white field, thin top rail, authentic dark-on-light lockup at upper right, bold Chinese title, editable flat composition, optional pale-blue takeaway strip.
4. **Image-led content:** the content chrome above plus two to six aligned rounded image frames with concise captions.
5. **Closing:** deep blue, authentic light-on-dark lockup, minimal closing statement, one panoramic or organic water-engineering image.

## Content boundary

Only brand lockup pixels may be copied into generated decks. Source-slide subject matter is sample content and must not be transferred. New topic imagery must be independently sourced or generated and recorded in speaker-note sources when applicable.

## Verification

- Official Codex `quick_validate.py` passes with UTF-8 mode.
- Asset integrity tests pass from a clean checkout.
- The source SHA and both crop hashes match `provenance.json`.
- A source-deck inspection confirms 33 slide images and zero text shapes.
- Skill application testing confirms no complete source slide is reused, identity marks resolve only to retained crop paths, and output guidance excludes 110-anniversary elements.
- GitHub verification re-reads `SKILL.md`, `provenance.json`, and repository metadata after push.

## Publishing and rights notice

The public repository includes the user-authorized source PPTX. `NOTICE.md` states that Hohai University names and marks remain the property of their respective rights holder and that the repository does not grant trademark rights. No permissive software license is attached to the source presentation or marks.

