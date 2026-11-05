# Typography and readable interfaces

Typography affects both aesthetics and geometry. The font family changes glyph widths, line breaks, baseline position, and perceived weight. Treat type tokens as layout tokens.

### A useful type system

Define a small scale, a readable body measure, and clear line-height rules. Use `clamp()` for display type, but avoid fluid body text that becomes unpredictable across zoom levels. Use `rem` so user preferences remain effective.

### Font loading

Use `font-display` intentionally, subset large fonts, and test the fallback stack. A fallback with radically different metrics can cause layout shift. `size-adjust`, `ascent-override`, `descent-override`, and `line-gap-override` can align fallback metrics when the performance benefit is worth the complexity.

### Text wrapping and overflow

`text-wrap: balance` is especially useful for headings. `text-overflow: ellipsis` is not a replacement for a disclosure mechanism; truncated content still needs an accessible way to be read. Use `overflow-wrap: anywhere` for hostile identifiers and URLs, not for ordinary prose.

### Writing modes

Logical properties express intent in terms of block and inline flow. Pair them with `writing-mode`, `direction`, and `text-orientation` testing. A component that uses only physical left/right properties is harder to localize and harder to reuse in vertical writing modes.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
