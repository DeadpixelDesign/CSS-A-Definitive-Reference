# Property reference: Color, backgrounds, borders, and effects

> **How to use this section:** This property controls color, surfaces, visual effects, focus indication, or user interaction. Each entry follows the same editorial pattern so it can be indexed, typeset, and reviewed consistently.

### `accent-color`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `accent-color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `accent-color` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `accent-color` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { accent-color: #1d4ed8; }
```

**Example: Component token.**

```css
:root {
  --book-accent-color: initial;
}
.component {
  accent-color: var(--book-accent-color, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  accent-color: initial;
}

@supports (accent-color: initial) {
  .component { accent-color: var(--book-accent-color, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { background: #ffffff; }
```

**Example: Component token.**

```css
:root {
  --book-background: initial;
}
.component {
  background: var(--book-background, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background: initial;
}

@supports (background: initial) {
  .component { background: var(--book-background, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-attachment`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-attachment` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-attachment` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-attachment` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.surface { background-attachment: initial; }
```

**Example: Component token.**

```css
:root {
  --book-background-attachment: initial;
}
.component {
  background-attachment: var(--book-background-attachment, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-attachment: initial;
}

@supports (background-attachment: initial) {
  .component { background-attachment: var(--book-background-attachment, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-blend-mode`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-blend-mode` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-blend-mode` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-blend-mode` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.surface { background-blend-mode: initial; }
```

**Example: Component token.**

```css
:root {
  --book-background-blend-mode: initial;
}
.component {
  background-blend-mode: var(--book-background-blend-mode, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-blend-mode: initial;
}

@supports (background-blend-mode: initial) {
  .component { background-blend-mode: var(--book-background-blend-mode, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-clip`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-clip` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-clip` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-clip` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.surface { background-clip: initial; }
```

**Example: Component token.**

```css
:root {
  --book-background-clip: initial;
}
.component {
  background-clip: var(--book-background-clip, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-clip: initial;
}

@supports (background-clip: initial) {
  .component { background-clip: var(--book-background-clip, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-color`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-color` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-color` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { background-color: #ffffff; }
```

**Example: Component token.**

```css
:root {
  --book-background-color: initial;
}
.component {
  background-color: var(--book-background-color, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-color: initial;
}

@supports (background-color: initial) {
  .component { background-color: var(--book-background-color, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-image`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-image` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-image` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-image` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.surface { background-image: initial; }
```

**Example: Component token.**

```css
:root {
  --book-background-image: initial;
}
.component {
  background-image: var(--book-background-image, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-image: initial;
}

@supports (background-image: initial) {
  .component { background-image: var(--book-background-image, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-origin`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-origin` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-origin` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-origin` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.surface { background-origin: initial; }
```

**Example: Component token.**

```css
:root {
  --book-background-origin: initial;
}
.component {
  background-origin: var(--book-background-origin, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-origin: initial;
}

@supports (background-origin: initial) {
  .component { background-origin: var(--book-background-origin, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-position`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-position` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-position` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-position` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { background-position: center; }
```

**Example: Component token.**

```css
:root {
  --book-background-position: initial;
}
.component {
  background-position: var(--book-background-position, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-position: initial;
}

@supports (background-position: initial) {
  .component { background-position: var(--book-background-position, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-position-x`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-position-x` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-position-x` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-position-x` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.surface { background-position-x: initial; }
```

**Example: Component token.**

```css
:root {
  --book-background-position-x: initial;
}
.component {
  background-position-x: var(--book-background-position-x, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-position-x: initial;
}

@supports (background-position-x: initial) {
  .component { background-position-x: var(--book-background-position-x, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-position-y`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-position-y` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-position-y` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-position-y` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.surface { background-position-y: initial; }
```

**Example: Component token.**

```css
:root {
  --book-background-position-y: initial;
}
.component {
  background-position-y: var(--book-background-position-y, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-position-y: initial;
}

@supports (background-position-y: initial) {
  .component { background-position-y: var(--book-background-position-y, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-repeat`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-repeat` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-repeat` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-repeat` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { background-repeat: no-repeat; }
```

**Example: Component token.**

```css
:root {
  --book-background-repeat: initial;
}
.component {
  background-repeat: var(--book-background-repeat, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-repeat: initial;
}

@supports (background-repeat: initial) {
  .component { background-repeat: var(--book-background-repeat, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `background-size`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `background-size` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `background-size` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `background-size` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { background-size: cover; }
```

**Example: Component token.**

```css
:root {
  --book-background-size: initial;
}
.component {
  background-size: var(--book-background-size, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  background-size: initial;
}

@supports (background-size: initial) {
  .component { background-size: var(--book-background-size, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `border-image-outset`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `border-image-outset` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `border-image-outset` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `border-image-outset` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { border-image-outset: initial; }
```

**Example: Component token.**

```css
:root {
  --book-border-image-outset: initial;
}
.component {
  border-image-outset: var(--book-border-image-outset, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  border-image-outset: initial;
}

@supports (border-image-outset: initial) {
  .component { border-image-outset: var(--book-border-image-outset, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `border-image-repeat`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `border-image-repeat` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `border-image-repeat` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `border-image-repeat` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { border-image-repeat: initial; }
```

**Example: Component token.**

```css
:root {
  --book-border-image-repeat: initial;
}
.component {
  border-image-repeat: var(--book-border-image-repeat, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  border-image-repeat: initial;
}

@supports (border-image-repeat: initial) {
  .component { border-image-repeat: var(--book-border-image-repeat, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `border-image-slice`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `border-image-slice` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `border-image-slice` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `border-image-slice` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { border-image-slice: initial; }
```

**Example: Component token.**

```css
:root {
  --book-border-image-slice: initial;
}
.component {
  border-image-slice: var(--book-border-image-slice, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  border-image-slice: initial;
}

@supports (border-image-slice: initial) {
  .component { border-image-slice: var(--book-border-image-slice, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `border-image-source`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `border-image-source` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `border-image-source` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `border-image-source` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { border-image-source: initial; }
```

**Example: Component token.**

```css
:root {
  --book-border-image-source: initial;
}
.component {
  border-image-source: var(--book-border-image-source, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  border-image-source: initial;
}

@supports (border-image-source: initial) {
  .component { border-image-source: var(--book-border-image-source, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `border-image-width`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `border-image-width` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `border-image-width` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `border-image-width` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { border-image-width: initial; }
```

**Example: Component token.**

```css
:root {
  --book-border-image-width: initial;
}
.component {
  border-image-width: var(--book-border-image-width, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  border-image-width: initial;
}

@supports (border-image-width: initial) {
  .component { border-image-width: var(--book-border-image-width, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `caret-color`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `caret-color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `caret-color` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `caret-color` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { caret-color: #1d4ed8; }
```

**Example: Component token.**

```css
:root {
  --book-caret-color: initial;
}
.component {
  caret-color: var(--book-caret-color, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  caret-color: initial;
}

@supports (caret-color: initial) {
  .component { caret-color: var(--book-caret-color, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `color`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `color` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `color` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { color: #172033; }
```

**Example: Component token.**

```css
:root {
  --book-color: initial;
}
.component {
  color: var(--book-color, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  color: initial;
}

@supports (color: initial) {
  .component { color: var(--book-color, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `color-scheme`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `color-scheme` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `color-scheme` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `color-scheme` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { color-scheme: light dark; }
```

**Example: Component token.**

```css
:root {
  --book-color-scheme: initial;
}
.component {
  color-scheme: var(--book-color-scheme, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  color-scheme: initial;
}

@supports (color-scheme: initial) {
  .component { color-scheme: var(--book-color-scheme, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `filter`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `filter` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `filter` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `filter` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { filter: initial; }
```

**Example: Component token.**

```css
:root {
  --book-filter: initial;
}
.component {
  filter: var(--book-filter, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  filter: initial;
}

@supports (filter: initial) {
  .component { filter: var(--book-filter, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `flood-color`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `flood-color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flood-color` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flood-color` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { flood-color: initial; }
```

**Example: Component token.**

```css
:root {
  --book-flood-color: initial;
}
.component {
  flood-color: var(--book-flood-color, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flood-color: initial;
}

@supports (flood-color: initial) {
  .component { flood-color: var(--book-flood-color, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `flood-opacity`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `flood-opacity` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flood-opacity` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flood-opacity` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { flood-opacity: initial; }
```

**Example: Component token.**

```css
:root {
  --book-flood-opacity: initial;
}
.component {
  flood-opacity: var(--book-flood-opacity, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flood-opacity: initial;
}

@supports (flood-opacity: initial) {
  .component { flood-opacity: var(--book-flood-opacity, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `forced-color-adjust`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `forced-color-adjust` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `forced-color-adjust` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `forced-color-adjust` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { forced-color-adjust: initial; }
```

**Example: Component token.**

```css
:root {
  --book-forced-color-adjust: initial;
}
.component {
  forced-color-adjust: var(--book-forced-color-adjust, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  forced-color-adjust: initial;
}

@supports (forced-color-adjust: initial) {
  .component { forced-color-adjust: var(--book-forced-color-adjust, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `image-orientation`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `image-orientation` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `image-orientation` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `image-orientation` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { image-orientation: initial; }
```

**Example: Component token.**

```css
:root {
  --book-image-orientation: initial;
}
.component {
  image-orientation: var(--book-image-orientation, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  image-orientation: initial;
}

@supports (image-orientation: initial) {
  .component { image-orientation: var(--book-image-orientation, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `image-rendering`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `image-rendering` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `image-rendering` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `image-rendering` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { image-rendering: initial; }
```

**Example: Component token.**

```css
:root {
  --book-image-rendering: initial;
}
.component {
  image-rendering: var(--book-image-rendering, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  image-rendering: initial;
}

@supports (image-rendering: initial) {
  .component { image-rendering: var(--book-image-rendering, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `mix-blend-mode`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `mix-blend-mode` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `mix-blend-mode` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `mix-blend-mode` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { mix-blend-mode: initial; }
```

**Example: Component token.**

```css
:root {
  --book-mix-blend-mode: initial;
}
.component {
  mix-blend-mode: var(--book-mix-blend-mode, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  mix-blend-mode: initial;
}

@supports (mix-blend-mode: initial) {
  .component { mix-blend-mode: var(--book-mix-blend-mode, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `outline`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `outline` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `outline` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `outline` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { outline: 3px solid currentColor; }
```

**Example: Component token.**

```css
:root {
  --book-outline: initial;
}
.component {
  outline: var(--book-outline, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  outline: initial;
}

@supports (outline: initial) {
  .component { outline: var(--book-outline, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `outline-color`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `outline-color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `outline-color` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `outline-color` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { outline-color: initial; }
```

**Example: Component token.**

```css
:root {
  --book-outline-color: initial;
}
.component {
  outline-color: var(--book-outline-color, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  outline-color: initial;
}

@supports (outline-color: initial) {
  .component { outline-color: var(--book-outline-color, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `outline-offset`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `outline-offset` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `outline-offset` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `outline-offset` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { outline-offset: 3px; }
```

**Example: Component token.**

```css
:root {
  --book-outline-offset: initial;
}
.component {
  outline-offset: var(--book-outline-offset, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  outline-offset: initial;
}

@supports (outline-offset: initial) {
  .component { outline-offset: var(--book-outline-offset, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `outline-style`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `outline-style` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `outline-style` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `outline-style` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { outline-style: initial; }
```

**Example: Component token.**

```css
:root {
  --book-outline-style: initial;
}
.component {
  outline-style: var(--book-outline-style, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  outline-style: initial;
}

@supports (outline-style: initial) {
  .component { outline-style: var(--book-outline-style, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `outline-width`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `outline-width` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `outline-width` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `outline-width` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { outline-width: initial; }
```

**Example: Component token.**

```css
:root {
  --book-outline-width: initial;
}
.component {
  outline-width: var(--book-outline-width, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  outline-width: initial;
}

@supports (outline-width: initial) {
  .component { outline-width: var(--book-outline-width, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `print-color-adjust`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `print-color-adjust` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `print-color-adjust` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `print-color-adjust` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { print-color-adjust: initial; }
```

**Example: Component token.**

```css
:root {
  --book-print-color-adjust: initial;
}
.component {
  print-color-adjust: var(--book-print-color-adjust, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  print-color-adjust: initial;
}

@supports (print-color-adjust: initial) {
  .component { print-color-adjust: var(--book-print-color-adjust, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `scrollbar-color`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `scrollbar-color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `scrollbar-color` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `scrollbar-color` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { scrollbar-color: initial; }
```

**Example: Component token.**

```css
:root {
  --book-scrollbar-color: initial;
}
.component {
  scrollbar-color: var(--book-scrollbar-color, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  scrollbar-color: initial;
}

@supports (scrollbar-color: initial) {
  .component { scrollbar-color: var(--book-scrollbar-color, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `scrollbar-gutter`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `scrollbar-gutter` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `scrollbar-gutter` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `scrollbar-gutter` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { scrollbar-gutter: initial; }
```

**Example: Component token.**

```css
:root {
  --book-scrollbar-gutter: initial;
}
.component {
  scrollbar-gutter: var(--book-scrollbar-gutter, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  scrollbar-gutter: initial;
}

@supports (scrollbar-gutter: initial) {
  .component { scrollbar-gutter: var(--book-scrollbar-gutter, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `scrollbar-width`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `scrollbar-width` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `scrollbar-width` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `scrollbar-width` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { scrollbar-width: initial; }
```

**Example: Component token.**

```css
:root {
  --book-scrollbar-width: initial;
}
.component {
  scrollbar-width: var(--book-scrollbar-width, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  scrollbar-width: initial;
}

@supports (scrollbar-width: initial) {
  .component { scrollbar-width: var(--book-scrollbar-width, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `shape-image-threshold`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `shape-image-threshold` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `shape-image-threshold` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `shape-image-threshold` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { shape-image-threshold: initial; }
```

**Example: Component token.**

```css
:root {
  --book-shape-image-threshold: initial;
}
.component {
  shape-image-threshold: var(--book-shape-image-threshold, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  shape-image-threshold: initial;
}

@supports (shape-image-threshold: initial) {
  .component { shape-image-threshold: var(--book-shape-image-threshold, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `shape-margin`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `shape-margin` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `shape-margin` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `shape-margin` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { shape-margin: initial; }
```

**Example: Component token.**

```css
:root {
  --book-shape-margin: initial;
}
.component {
  shape-margin: var(--book-shape-margin, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  shape-margin: initial;
}

@supports (shape-margin: initial) {
  .component { shape-margin: var(--book-shape-margin, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `shape-outside`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `shape-outside` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `shape-outside` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `shape-outside` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { shape-outside: initial; }
```

**Example: Component token.**

```css
:root {
  --book-shape-outside: initial;
}
.component {
  shape-outside: var(--book-shape-outside, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  shape-outside: initial;
}

@supports (shape-outside: initial) {
  .component { shape-outside: var(--book-shape-outside, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `text-fill-color`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `text-fill-color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `text-fill-color` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `text-fill-color` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { text-fill-color: initial; }
```

**Example: Component token.**

```css
:root {
  --book-text-fill-color: initial;
}
.component {
  text-fill-color: var(--book-text-fill-color, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  text-fill-color: initial;
}

@supports (text-fill-color: initial) {
  .component { text-fill-color: var(--book-text-fill-color, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `text-stroke`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `text-stroke` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `text-stroke` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `text-stroke` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { text-stroke: initial; }
```

**Example: Component token.**

```css
:root {
  --book-text-stroke: initial;
}
.component {
  text-stroke: var(--book-text-stroke, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  text-stroke: initial;
}

@supports (text-stroke: initial) {
  .component { text-stroke: var(--book-text-stroke, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `touch-action`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `touch-action` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `touch-action` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `touch-action` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { touch-action: manipulation; }
```

**Example: Component token.**

```css
:root {
  --book-touch-action: initial;
}
.component {
  touch-action: var(--book-touch-action, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  touch-action: initial;
}

@supports (touch-action: initial) {
  .component { touch-action: var(--book-touch-action, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.

### `user-select`

**Role.** This property controls color, surfaces, visual effects, focus indication, or user interaction. The `user-select` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `user-select` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `user-select` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { user-select: text; }
```

**Example: Component token.**

```css
:root {
  --book-user-select: initial;
}
.component {
  user-select: var(--book-user-select, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  user-select: initial;
}

@supports (user-select: initial) {
  .component { user-select: var(--book-user-select, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Color, backgrounds, borders, and effects` chapter before changing a component-wide contract.
