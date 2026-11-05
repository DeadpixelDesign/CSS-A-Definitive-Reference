# Appendix B: Submission package for publishers

This appendix is for producing a personal spiral-bound print edition, not for submitting a traditional publishing proposal. For one copy or a small private run, the most practical route is to prepare a print-ready PDF and submit it to a local print shop or an online book printer that offers coil binding.

### Recommended options

| Option | Best for | What to submit |
|---|---|---|
| Local independent print shop | Highest control over paper, covers, proofing, and binding | Print-ready PDF and a written specification |
| FedEx Office | Convenient upload, local pickup, and standard document sizes | PDF; choose coil binding and cover options where available |
| Staples Print & Marketing | Local document printing and coil binding where the selected store supports it | PDF; confirm binding capacity and turnaround first |
| Lulu personal printing | A book-like upload workflow with paperback coil-bound options | Interior PDF, cover PDF, trim size, paper, and binding selection |
| University or library print center | Cost-conscious personal copies and large technical documents | PDF plus page-count and binding instructions |

Service availability, page limits, paper stocks, and local turnaround can change. Confirm the exact binding option and maximum page count before placing the order. For a personal spiral edition, local shops are often the easiest place to inspect a proof and request changes.

### Metal ring binding: Wire-O or twin-loop wire

Yes. Ask for **Wire-O**, **twin-loop wire**, **double-loop wire**, **double-O**, or **ring-wire binding**. This is the metal-ring option: pages and covers are punched, then a preformed metal wire is closed through the holes. It lies flat and can usually fold back on itself, making it a strong choice for a technical reference used beside a computer.

Wire-O is different from a continuous plastic spiral coil:

| Binding | Material and shape | Strengths | Tradeoffs |
|---|---|---|---|
| Plastic coil | Continuous plastic helix | Flexible, economical, easy to turn | Less formal appearance; coil can deform if handled roughly |
| Wire-O | Preformed metal double loops | Professional appearance, lies flat, folds back | Printer must have the correct punch and wire size; pages are not easily removable |
| Three-ring binder | Separate metal rings in a cover | Pages can be added or removed | Bulky, pages can shift, and the spine is wider |

For this book, I would request black or silver Wire-O with a clear front cover and opaque back cover. Ask the printer whether it supports 2:1 or 3:1 hole spacing, the maximum thickness, and the binding-side margin. Do not assume that a shop offering plastic coil also offers metal Wire-O.

The PDF should reserve extra space on the punched edge. A printer may recommend approximately 0.75–0.875 inches, but use the shop’s template because the required margin depends on paper thickness, punch pattern, and wire size. [Wire-O guidance from PrintingCenterUSA](https://www.printingcenterusa.com/help-center/knowledge-base/binding-wire-o/) describes a 7/8-inch binding-side margin, while other binders use different specifications.

### My practical recommendation

Start with one proof at a local print shop. Request:

- US Letter or A4, depending on where you will read it;
- double-sided printing;
- a clear front cover and durable back cover;
- black plastic coil binding;
- 28–32 lb interior paper for a long reference book;
- heavier cover stock or laminated covers;
- color printing only for diagrams, QR codes, and pages where color carries meaning.

If the proof is satisfactory and you want a second copy, compare its total price with Lulu’s personal-printing workflow. A local shop is usually better for immediate feedback; an online printer is more convenient when you want repeatable copies shipped to you.

### Prepare the print-ready PDF

Do not submit the SvelteKit HTML or the raw Markdown file to a print shop. Export a paginated PDF with:

1. A defined trim size and page orientation.
2. Embedded fonts.
3. Page numbers and a tested table of contents.
4. A title page, edition date, and copyright page.
5. Headers, footers, and chapter openers that do not collide with the binding edge.
6. Print-safe contrast and code blocks that do not rely on a dark screen theme alone.
7. Images and QR codes at sufficient resolution.
8. Intentional blank pages where chapters need to begin on a right-hand page.
9. A front cover PDF and a separate interior PDF if the service requests them separately.

For coil binding, leave a generous inner margin on the punched edge. Lulu’s formatting guidance recommends additional binding-side space for coil-bound books; a local printer may use a different punch and margin specification, so ask the printer for its exact template before final export.

### Suggested file package

```text
css-definitive-reference/
├── CSS-Definitive-Reference-interior.pdf
├── CSS-Definitive-Reference-cover.pdf
├── CSS-Definitive-Reference-proof-notes.md
└── CSS-Definitive-Reference-source.md
```

The Markdown file is useful for revisions, but the PDF is the file that controls pagination and print output. Keep the source and print proof together so a later compatibility update can be traced to the edition that was printed.

### Recommended fonts for the print edition

Use three clearly separated typographic roles: a readable text face, a sturdy display face, and a monospace face for code. The web edition already uses this three-role model; the print edition should preserve the roles while using embedded, print-tested font files.

| Role | Primary recommendation | Good alternative | Use |
|---|---|---|---|
| Body text | Source Serif 4 | Literata or Charter | Paragraphs, notes, captions, and long explanations |
| Headings and interface labels | DM Sans | Source Sans 3 or IBM Plex Sans | Chapter titles, headings, tables, badges, and navigation |
| Code | DM Mono | Source Code Pro or IBM Plex Mono | CSS, JavaScript, URLs, commands, and tokens |

The recommended combination for this book is Source Serif 4 for reading text, DM Sans for headings and interface labels, and DM Mono for code. It creates a clear contrast between explanation and implementation while remaining familiar to readers who spend long periods reading technical material.

```css
:root {
  --font-reading: "Source Serif 4", Georgia, serif;
  --font-display: "DM Sans", "Source Sans 3", Arial, sans-serif;
  --font-code: "DM Mono", "Source Code Pro", "SFMono-Regular", Consolas, monospace;
}

body { font-family: var(--font-reading); }
h1, h2, h3, h4, nav, .badge, .button { font-family: var(--font-display); }
code, pre, kbd, samp { font-family: var(--font-code); }
```

For a print PDF, embed the exact font files and confirm that the licenses permit embedding and distribution. Open-source families from Google Fonts are convenient, but still keep a copy of the license and record the font version used for the edition.

### Print typography checks

Before approving the proof:

1. Check body text at approximately 10.5–11.5 pt with 1.35–1.55 line spacing.
2. Keep the prose measure near 55–75 characters per line.
3. Confirm that headings do not orphan at the bottom of a page.
4. Check that code remains legible at approximately 8.5–9.5 pt.
5. Inspect similar glyphs such as `0/O`, `1/l/I`, braces, brackets, and punctuation.
6. Verify that code lines wrap intentionally or are split into readable examples.
7. Compare the font metrics against the HTML edition before final pagination.
8. Print a grayscale proof; hierarchy should remain clear without color.

Changing fonts after pagination can alter line breaks, page count, table widths, code wrapping, and the position of QR codes. Treat the font choice as part of the print specification, not as a final cosmetic adjustment.

### Print-shop submission note

Use a short specification instead of sending an open-ended request:

```text
Please print one double-sided, full-color proof from the attached PDF.
Trim size: US Letter, portrait.
Binding: black or silver Wire-O / twin-loop metal wire, left edge.
Covers: clear front cover and heavy opaque back cover.
Interior: 28–32 lb white paper.
Please confirm the binding-side margin, hole pattern, wire size, and maximum page count before production.
Please provide a proof or digital preflight for approval.
```

### Copyright and personal-use boundary

This workflow assumes that you own or have permission to print the manuscript, code, illustrations, fonts, and other included assets. A personal copy of your own book is different from uploading someone else’s copyrighted book to a print service. Check licenses for fonts, screenshots, third-party code, and logos before ordering copies.

### Current service links

- [Lulu personal printing](https://help.lulu.com/en/support/solutions/articles/64000255486-how-to-create-a-print-book) — supports personal-printing projects and offers book binding choices.
- [Lulu binding options](https://help.api.lulu.com/en/support/solutions/articles/64000254625-what-is-the-difference-between-binding-types-) — describes coil-bound books and other binding types.
- [Lulu formatting tips](https://help.lulu.com/en/support/solutions/articles/64000255583) — includes PDF preparation and coil-binding margin guidance.
- [FedEx Office document printing](https://www.office.fedex.com/default/copies.html) — offers document upload, paper choices, coil binding, and pickup options where available.
- [FedEx Office binding and finishing](https://www.office.fedex.com/default/binding-laminating-finishing-services) — describes binding and finishing services.
- [Staples document printing](https://www.staples.com/services/printing/copies-documents-printing/) — offers document printing and coil binding options subject to location and service availability.
- [PrintingCenterUSA Wire-O guidance](https://www.printingcenterusa.com/help-center/knowledge-base/binding-wire-o/) — explains metal Wire-O binding, page ranges, and binding-side margin guidance.

For this book, the best first submission is a print-ready PDF to a nearby independent print shop for one proof, followed by Lulu if you want a repeatable online order. Always confirm current pricing, page limits, binding availability, and file requirements before payment.
