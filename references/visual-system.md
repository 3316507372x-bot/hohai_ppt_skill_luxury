# Hohai Luxury Visual System

## Visual job

Express formal Chinese university reporting with strong Hohai identity, restrained water imagery, clear technical hierarchy, and an editable PowerPoint structure. The design should feel academic and authoritative, not like a neon control-room dashboard or a generic corporate template.

**Identity harmony invariant:** the combined lockup JPEG carries a permanent pure-white (`#FFFFFF`) field. Blend it only on pure-white backgrounds; on tinted or colored areas, frame it in a clean white plate or rail (exact specs under "Identity harmony" below; a subtle gradient or ribbon wedge in the surrounding blue helps Frame read as designed). Never blend on a tinted fill, never a floating rounded box, never a plate straddling a color boundary. Backgrounds are otherwise free.

## Source references

- `../assets/preview.png`: cover composition, deep-blue gradient, centered identity, large title, campus panorama, light water ribbons.
- `../assets/reference-middle.png`: content-page top rail, upper-right identity, pale blue-white field, bold Chinese hierarchy, layered blue conclusion strip.
- `../assets/reference-image-page.png`: image-led page, aligned rounded frames, concise captions, panoramic lower image.

These images contain sample content. Read them for composition only; never copy their text, people, diagrams, photographs, or anniversary material.

## Palette and typography

| Role | Guidance |
|---|---|
| Deep Hohai blue | Use near `#074A99` to `#0B3F86` for covers, dividers, conclusion strips, and strong rules. Prefer subtle gradients between nearby blues (e.g. `#0B3F86` → `#1E6FC4`) over large flat fills. |
| Primary blue | Use near `#0B5CB8` for headings, icons, and connectors. |
| Pale field | Use `#F4F9FE` to `#EAF4FC` for content backgrounds. |
| White | Use for titles on deep blue and for the intentional identity plate or rail that holds the blue combined lockup on deep blue. |
| Warm ivory | Optional for one high-emphasis cover or closing title; keep it restrained. |

Prefer a bold Chinese Song/Heiti-inspired title face available on the system, with a neutral sans-serif for English and numbers. Match source proportions rather than guessing exact rasterized font names. Keep titles on one line when intended; change wording or layout before shrinking type.

## Page families

### Opening

- Deep-blue vertical gradient with substantial negative space; vary the gradient across the identity zone (deep toward one corner, lighter toward the plate) so no large flat area sits behind or beside the identity plate.
- Exact combined lockup near the top center or upper right, contained in a deliberate white identity plate or rail that is flush with an edge or fully inside the blue field with even margins.
- One concise title, one subtitle, and at most one small descriptor.
- A realistic water-engineering or campus panorama across the lower third to half.
- Subtle water ribbons, terrain contours, or data paths may frame the lower edge; they remain decorative and never compete with the title.

### Section divider

- Deep-blue field with a small section number and a two-line maximum title.
- One organic rounded photographic window, normally on the right.
- Faint contour-line or water-wave decoration.
- Exact combined lockup in an edge-aligned white identity plate; never floating mid-blue.
- No body copy and no UI cards.

### Standard content

- Pale blue-white field.
- A small section label and thin horizontal rule across the top.
- Exact combined lockup at the upper right, seated on a white header rail that is flush with the top edge (never blended directly on the tinted field).
- Bold dark-blue Chinese title; information reads left to right or top to bottom.
- Prefer one flat composition: image plus explanation, process flow, comparison, chart, or table.
- Use a pale-blue takeaway strip or dark-blue conclusion strip only when the page needs a single conclusion.

### Image-led content

- Preserve the standard top rail and lockup.
- Use two to six consistently cropped rounded image frames.
- Captions stay short, aligned, and readable.
- A single panorama may anchor the lower edge when it materially supports the topic.

### Closing

- Return to deep blue and place the exact combined lockup in a deliberate white identity plate or rail that is flush with an edge or fully inside the blue field.
- Use one short closing title and one optional statement.
- Use one panoramic or organic-window water-engineering image.
- Exclude contact details, QR codes, admissions slogans, and anniversary marks unless the current user explicitly supplies and requests them; the retained deck does not authorize them.

## Example narrative mapping

For a digital-twin water-conservancy presentation: opening title; challenge; sensing-model-decision architecture; physical-to-digital process; application scenarios; implementation path; concise conclusion; closing. Adapt page count and density to the user's actual purpose rather than forcing this example.

## Acceptance

- Every narrative element remains editable.
- Adjacent slides vary silhouette while keeping the same chrome and spacing rhythm.
- No whole source slide appears as a background.
- The exact user-authorized combined lockup appears once per slide, is legible at normal slide-view scale, and retains its original aspect ratio and white field.
- The lockup's white field always reads as intentional: blended on pure white (boundary invisible), or contained in a white rail or plate per the Identity harmony specs — never blended on a tinted fill, never a floating rounded box, never straddling a boundary between two color regions.
- No `110`, anniversary slogan, or anniversary-only motif appears in text or pixels.

## Identity harmony

The combined lockup JPEG carries a permanent pure-white (`#FFFFFF`) field. Place it by exactly one of two modes:

- **Blend** — only on pure `#FFFFFF` backgrounds. Place the lockup directly; the field is invisible. On tinted areas (even `#F4F9FE`) the field shows as a faint rectangle, so blending there is forbidden — use Frame.
- **Frame** — a white (`#FFFFFF`) plate or rail on a colored area:
  - **Rail (flush):** anchored to the slide edge or band edge with zero offset; square corners (radius 0); no border stroke.
  - **Plate (inside color):** fully inside one color region; uniform padding around the lockup image of 20–30% of the lockup's height on all sides; corner radius at most 10% of plate height; at most one subtle soft shadow; never straddling a color boundary — keep at least one padding-width of clear color between the plate and any boundary.
  - The plate must be visibly larger than the lockup's white field on every side; a plate hugging the field edge reads as a raw paste.

**Ideas that help Frame read as designed:**

- A subtle two-stop deep-blue gradient across the surrounding field (`#0B3F86` → `#1E6FC4`), deepening away from the plate; avoid larger jumps that band.
- Layered ribbon or wedge shapes in a lighter blue near the plate, echoing the water motif.
- A full-width white rail along the top edge, so the plate becomes part of the page structure.
- Align the plate to the content grid so it shares edges and spacing with other elements.

**Never:**

- Blend on a tinted background (any fill that is not `#FFFFFF`).
- A floating rounded box with colored margins on all four sides.
- A plate or lockup straddling the boundary between two color regions.

**Verification:** render the slide, zoom to 100% on the lockup, and confirm: in Blend the field boundary is invisible; in Frame the padding is even and no plate edge crosses a color boundary.
