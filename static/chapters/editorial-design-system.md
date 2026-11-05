# Editorial design system

This manuscript is intentionally structured for book production. A typesetter can map these tokens to a print or EPUB theme without rewriting the content.

| Token | Recommendation |
|---|---|
| Body type | 10.5–11 pt serif or humanist sans; 1.45–1.6 line height |
| Code type | 8.5–9 pt monospace; shaded background; never split a short example |
| Heading scale | H1 24 pt, H2 17 pt, H3 12.5 pt; keep headings with the next paragraph |
| Measure | 55–75 characters for prose; wider measure for tables and code |
| Spacing | 4/8/12/18/28/40 pt rhythm; avoid arbitrary one-off gaps |
| Callouts | One visual treatment for Note, Warning, Accessibility, and Compatibility |
| Tables | Repeating header row, zebra striping, minimum 9 pt text in print |
| Color | Navy ink, teal secondary, blue links, amber warnings; test in grayscale |

### Fonts used in this book

The web edition uses three complementary typefaces. **DM Sans** is the display and interface face for titles, navigation, buttons, badges, and labels. **Source Serif 4** is the reading face for paragraphs and longer explanations. **DM Mono** is the code face for CSS, JavaScript, URLs, and technical tokens.

Each font has a system fallback so the book remains readable while web fonts load or when a reader is offline. The fallback stack is part of the design contract, not an afterthought: it preserves the role of the typeface even when the exact font is unavailable.

```css
:root {
  --font-display: 'DM Sans', sans-serif;
  --font-reading: 'Source Serif 4', Georgia, serif;
  --font-code: 'DM Mono', 'SFMono-Regular', Consolas, monospace;
}

body {
  font-family: var(--font-reading);
}

h1, h2, h3, nav, .button {
  font-family: var(--font-display);
}

code, pre {
  font-family: var(--font-code);
}
```

For a print or EPUB edition, substitute fonts with equivalent metrics only after checking line breaks, heading wraps, code width, and the readable measure. Typography changes geometry: changing the font can change the layout.

### Color tokens and values

The web edition uses a restrained color system so hierarchy remains clear in color, grayscale print, and high-contrast contexts. The named tokens below are the colors used by the interface and the book theme.

| Token or value | Color value | Purpose |
|---|---|---|
| `--navy` | `#14213d` | Primary headings, brand mark, dark surfaces, table headers |
| `--blue` | `#1d4ed8` | Links, primary actions, active navigation, chapter numbers |
| `--teal` | `#0f766e` | Secondary accents, section labels, quote borders |
| `--gold` | `#a16207` | Warnings, amber metadata, caution states |
| `--ink` | `#172033` | Main reading text |
| `--muted` | `#5b6475` | Supporting text, labels, navigation copy |
| `--line` | `#d7deea` | Borders, dividers, and table rules |
| `--soft` | `#f4f7fb` | Callout surfaces and alternating content-table rows |
| Page background | `#f7f9fc` | Overall application background |
| Hero accent | `#1e3a68` | Deep blue midpoint in the hero gradient |
| Hero eyebrow | `#b8d6ff` | Light text on the hero surface |
| Hero lede | `#dce8f8` | Supporting hero copy |
| Code surface | `#272822` | Monokai-style code background |
| Inline code ink | `#8a2151` | Inline code and technical tokens in prose |
| Link tint surface | `#eaf1ff` | Active navigation and blue badges |
| Teal tint surface | `#e8f7ef` | Teal badges and positive accents |
| Gold tint surface | `#fff6db` | Gold badges and caution accents |
| White | `#ffffff` | Cards, buttons, table text, and high-contrast foregrounds |

The following modern color functions are useful when the design needs a different color space or a more intentional lightness model. They are examples for authoring and comparison, not additional interface tokens.

| Color space | Example value | Typical use |
|---|---|---|
| HWB | `hwb(210 10% 20%)` | Human-oriented hue with white and black components |
| Lab | `lab(55% 40 30)` | Perceptual color adjustments across a broad gamut |
| LCH | `lch(55% 60 30)` | Perceptual lightness, chroma, and hue control |
| OKLab | `oklab(60% 0.1 0.1)` | Modern perceptual mixing and interpolation |
| OKLCH | `oklch(65% 0.15 250)` | Theme scales and accessible lightness adjustments |

When using a modern color function, provide a tested fallback before it and check contrast in the actual rendering environment. A color-space conversion is not automatically a contrast guarantee.
