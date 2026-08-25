# Hohai Luxury Visual System

## Visual job

Express formal Chinese university reporting with strong Hohai identity, restrained water imagery, clear technical hierarchy, and an editable PowerPoint structure. The design should feel academic and authoritative, not like a neon control-room dashboard or a generic corporate template.

**Background invariant:** every slide's base fill is solid pure white `#FFFFFF`. Hohai blue appears in type, rules, strips, frames, and imagery — never as a slide background. Authority comes from blue typography, spacing, and photography on white, not from colored fills.

## Source references

- `../assets/preview.png`: cover composition, centered identity, large title, campus panorama, light water ribbons.
- `../assets/reference-middle.png`: content-page top rail, upper-right identity, bold Chinese hierarchy, layered blue conclusion strip.
- `../assets/reference-image-page.png`: image-led page, aligned rounded frames, concise captions, panoramic lower image.

These images contain sample content. Read them for composition only; never copy their text, people, diagrams, photographs, or anniversary material. Their deep-blue and pale-blue full-slide fills are a legacy pattern: reproduce the composition, never the tinted backgrounds — every output slide stays pure white.

## Palette and typography

| Role | Guidance |
|---|---|
| Slide background | Solid `#FFFFFF` on every slide, including opening, divider, and closing pages. No gradients, tints, or pale-blue fields. |
| Deep Hohai blue | Use near `#074A99` to `#0B3F86` for display type, section numbers, conclusion strips, and strong rules — never as a slide background. |
| Primary blue | Use near `#0B5CB8` for headings, icons, and connectors. |
| Pale blue accent | Use `#EAF4FC` sparingly for small takeaway strips, table header rows, or card fills layered on top of white; never as a full-slide field. |

Prefer a bold Chinese Song/Heiti-inspired title face available on the system, with a neutral sans-serif for English and numbers. Match source proportions rather than guessing exact rasterized font names. Keep titles on one line when intended; change wording or layout before shrinking type.

## Page families

### Opening

- Pure white background with substantial negative space.
- Exact combined lockup near the top center or upper right, placed directly on the white background with no plate or rail.
- One concise title in deep Hohai blue, one subtitle, and at most one small descriptor.
- A realistic water-engineering or campus panorama across the lower third to half.
- Subtle pale-blue water ribbons, terrain contours, or data paths may frame the lower edge; they remain decorative and never compete with the title.

### Section divider

- Pure white field with an oversized deep-blue section number and a two-line maximum title.
- One organic rounded photographic window, normally on the right, framed by a thin blue keyline if it needs separation from white.
- Faint pale-blue contour-line or water-wave decoration.
- No body copy and no UI cards.

### Standard content

- Pure white field.
- A small blue section label and thin horizontal rule across the top.
- Exact combined lockup at the upper right, directly on the white background.
- Bold dark-blue Chinese title; information reads left to right or top to bottom.
- Prefer one flat composition: image plus explanation, process flow, comparison, chart, or table.
- Use a pale-blue takeaway strip or dark-blue conclusion strip only when the page needs a single conclusion.

### Image-led content

- Preserve the standard top label, rule, and lockup on white.
- Use two to six consistently cropped rounded image frames.
- Captions stay short, aligned, and readable.
- A single panorama may anchor the lower edge when it materially supports the topic.

### Closing

- Return to pure white and place the exact combined lockup directly on the background.
- Use one short closing title in deep Hohai blue and one optional statement.
- Use one panoramic or organic-window water-engineering image.
- Exclude contact details, QR codes, admissions slogans, and anniversary marks unless the current user explicitly supplies and requests them; the retained deck does not authorize them.

## Example narrative mapping

For a digital-twin water-conservancy presentation: opening title; challenge; sensing-model-decision architecture; physical-to-digital process; application scenarios; implementation path; concise conclusion; closing. Adapt page count and density to the user's actual purpose rather than forcing this example.

## Acceptance

- Every narrative element remains editable.
- Adjacent slides vary silhouette while keeping the same chrome and spacing rhythm.
- No whole source slide appears as a background.
- Every slide's base fill is solid `#FFFFFF`; no gradient, tinted, deep-blue, or pale-blue full-slide field exists anywhere in the deck.
- The exact user-authorized combined lockup appears once per slide, is legible at normal slide-view scale, and retains its original aspect ratio and white field.
- No `110`, anniversary slogan, or anniversary-only motif appears in text or pixels.

## Background rule — non-negotiable

Set every slide's base fill to solid `#FFFFFF` before adding any element.

**No exceptions:**
- Do not use deep-blue gradients on covers or closings.
- Do not use solid deep-blue fields on dividers.
- Do not use pale fields (`#F4F9FE`, `#EAF4FC`, or any near-white tint) as slide fills.
- Do not place a colored rectangle or panel covering most of the slide as a de-facto background.
- Do not treat "very light blue" as white; only `#FFFFFF` counts.

| Excuse | Reality |
|---|---|
| "Covers need deep blue for formality" | Formality comes from blue display type, spacing, and photography on white. |
| "Pale blue is basically white" | Only `#FFFFFF` counts; every tint is prohibited. |
| "A gradient adds depth to the cover" | Depth comes from the panorama image and negative space, not background fills. |
| "The photo window needs a colored backdrop" | Photo windows sit directly on white with an optional thin blue keyline. |
| "This deck is special; one blue cover is fine" | The invariant has no exceptions; one violation breaks the whole system. |

## Red flags — STOP and fix before continuing

- Choosing `#F4F9FE`, `#EAF4FC`, or any gradient for a slide fill.
- A deep-blue opening, divider, or closing page.
- A colored panel covering most of a slide.
- Any slide fill described as "pale", "tinted", or "blue-white".

**All of these mean: set the slide fill back to solid `#FFFFFF` before doing anything else.**
