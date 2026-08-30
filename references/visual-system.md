# Hohai Luxury Visual System

## Visual job

Express formal Chinese university reporting with strong Hohai identity, restrained water imagery, clear technical hierarchy, and an editable PowerPoint structure. The design should feel academic and authoritative, not like a neon control-room dashboard or a generic corporate template.

**Identity rule:** the combined lockup exists in two transparent colorways — blue artwork for light backgrounds, white artwork for dark backgrounds. Match the colorway to the background and place it directly; both files are fully transparent, so no plate, rail, or mat is ever needed, and adding one is prohibited. Never cross colorways.

## Source references

- `../assets/preview.png`: cover composition, deep-blue gradient, centered identity, large title, campus panorama, light water ribbons.
- `../assets/reference-middle.png`: content-page top label band, upper-right identity, pale blue-white field, bold Chinese hierarchy, layered blue conclusion strip.
- `../assets/reference-image-page.png`: image-led page, aligned rounded frames, concise captions, panoramic lower image.

These images contain sample content. Read them for composition only; never copy their text, people, diagrams, photographs, or anniversary material.

## Palette and typography

| Role | Guidance |
|---|---|
| Deep Hohai blue | Use near `#074A99` to `#0B3F86` for covers, closings, conclusion strips, and strong rules. Prefer subtle gradients between nearby blues (e.g. `#0B3F86` → `#1E6FC4`) over large flat fills. |
| Primary blue | Use near `#0B5CB8` for headings, icons, and connectors. |
| Photo wash | Divider: white overlay ≈88% opacity over the retained dam photo (`../assets/photos/three-gorges-dam.jpg`). Content pages: ≈83%. The wash is a light field and carries the blue lockup colorway. |
| Pale field | `#F4F9FE` to `#EAF4FC` — fallback content background when no suitable photo is available. |
| White | Titles on deep blue. The transparent lockup colorways need no white plate or rail behind them. |
| Warm ivory | Optional for one high-emphasis cover or closing title; keep it restrained. |

Use Chinese-compatible faces that render consistently in Windows PowerPoint. **Chinese titles, body, labels, captions, and notes:** `Microsoft YaHei` (`微软雅黑`) as the primary face; use Bold/Semibold for titles and emphasis, and Regular for body text. If it is unavailable, fall back to `Source Han Sans SC` (`思源黑体`) or `Noto Sans CJK SC`, then `DengXian` (`等线`). **English and numbers:** `Aptos` or `Arial`. Do not use macOS-only `Songti SC`, `Hiragino Sans GB`, or `PingFang SC` as the primary face in Windows deliverables; never rely on rasterized type.

Match source proportions rather than guessing exact rasterized font names. Keep titles on one line when intended; change wording or layout before shrinking type.

## Page families

### Opening

- Deep-blue vertical gradient with substantial negative space; vary the gradient across the identity zone (deep toward one corner, lighter toward the lockup) so no large flat area sits behind or beside the lockup.
- Exact combined lockup near the top center or upper right — `hohai-lockup-white-transparent.png` placed directly on the blue.
- One concise title, one subtitle, and at most one small descriptor.
- A realistic water-engineering or campus panorama across the lower third to half.
- Subtle water ribbons, terrain contours, or data paths may frame the lower edge; they remain decorative and never compete with the title.

### Section divider

- Full-bleed background: the retained Three Gorges Dam photograph (`../assets/photos/three-gorges-dam.jpg`, CC BY-SA 2.0) under a semi-transparent white overlay at about **88% opacity**, so the structure reads faintly through.
- An oversized section number and a two-line maximum title in the title face; deep navy on the light wash.
- Exact combined lockup near the top center or upper right — `hohai-lockup-blue-transparent.png` placed directly on the light wash.
- Subtle contour-line or water-wave decoration may frame an edge; never compete with the title.
- No body copy and no UI cards.

### Standard content

- Same photographic treatment as the divider but denser: the retained dam photo under a white overlay at about **83% opacity**, with the stronger photographic presence reserved for the background layer and body text kept in clear content zones.
- A small section label and thin horizontal rule across the top.
- Exact combined lockup at the upper right — `hohai-lockup-blue-transparent.png` placed directly on the wash.
- Bold dark-blue Chinese title; information reads left to right or top to bottom.
- Prefer one flat composition: image plus explanation, process flow, comparison, chart, or table.
- Use a pale-blue takeaway strip or dark-blue conclusion strip only when the page needs a single conclusion.

### Image-led content

- Preserve the standard top label, rule, and lockup.
- Use two to six consistently cropped rounded image frames.
- Captions stay short, aligned, and readable.
- A single panorama may anchor the lower edge when it materially supports the topic.

### Closing

- Return to deep blue with `hohai-lockup-white-transparent.png` placed directly on the blue, top center or upper right.
- Use `谢谢聆听` as the default visible closing title, unless the current user explicitly requests another phrase, plus one optional statement.
- Use one panoramic or organic-window water-engineering image.
- Exclude contact details, QR codes, admissions slogans, and anniversary marks unless the current user explicitly supplies and requests them; the retained deck does not authorize them.

## Example narrative mapping

For a digital-twin water-conservancy presentation: opening title; challenge; sensing-model-decision architecture; physical-to-digital process; application scenarios; implementation path; concise conclusion; closing. Adapt page count and density to the user's actual purpose rather than forcing this example.

## Acceptance

- Every narrative element remains editable.
- Adjacent slides vary silhouette while keeping the same chrome and spacing rhythm.
- No whole source slide appears as a background.
- The exact user-authorized combined lockup appears once per slide, is legible at normal slide-view scale, and retains its original aspect ratio.
- The colorway always contrasts with its background: blue transparent version on light, white transparent version on dark; no white rectangle sits behind or around any lockup.
- No `110`, anniversary slogan, or anniversary-only motif appears in text or pixels.

## Identity placement

Two transparent colorways of the combined lockup are authorized:

| Background | Asset |
|---|---|
| Light — white photo wash, pure white, or pale field (`#F4F9FE`–`#EAF4FC`) | `../assets/hohai-lockup-blue-transparent.png` |
| Dark — deep Hohai blue (`#074A99`–`#0B3F86` range) | `../assets/hohai-lockup-white-transparent.png` |

- Place the lockup directly on the background with no plate, rail, or mat behind it; both files are fully transparent, so any added white rectangle is prohibited — it reintroduces the sticker problem these assets exist to solve.
- Never cross colorways: blue artwork on a dark background or white artwork on a light background is invisible.
- Scale proportionally and keep clear space of at least 25% of the lockup's height on all sides.
- `../assets/hohai-lockup-authorized.jpg` (blue artwork on a white field) is the archival original: use it only on a pure `#FFFFFF` background, where its field is invisible.

**Verification:** render the slide, zoom to 100% on the lockup, and confirm the colorway contrasts with its background and no white rectangle appears behind or around it.
