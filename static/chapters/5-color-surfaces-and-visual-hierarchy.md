# Color, surfaces, and visual hierarchy

Color should encode hierarchy without being the only carrier of meaning. Start with semantic tokens—surface, ink, muted ink, border, accent, danger, success—then map them to a theme.

### Color spaces

Hex, `rgb()`, `hsl()`, `lab()`, `lch()`, and `oklch()` are value syntaxes, not design systems. `color-mix()` and relative color syntax can derive relationships, but always provide a stable fallback before a new declaration when the color is essential.

### Focus and forced colors

Use `:focus-visible` and an outline that survives high-contrast modes. Avoid `outline: none` unless an equally visible replacement is present. Test Windows forced colors, dark mode, reduced transparency, and grayscale print.

### Backgrounds and images

Multiple backgrounds are painted back-to-front. `background-size: cover` crops; `contain` letterboxes. Use `object-fit` for replaced elements and `aspect-ratio` to reserve space. Treat decorative images as decoration and provide meaningful alternative text in HTML when the image carries content.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
