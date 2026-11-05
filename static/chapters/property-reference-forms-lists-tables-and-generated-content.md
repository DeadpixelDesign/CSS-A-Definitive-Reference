# Property reference: Forms, lists, tables, and generated content

> **How to use this section:** This property styles semantic content, controls, counters, lists, tables, or generated content. Each entry follows the same editorial pattern so it can be indexed, typeset, and reviewed consistently.

### `appearance`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `appearance` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `appearance` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `appearance` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { appearance: initial; }
```

**Example: Component token.**

```css
:root {
  --book-appearance: initial;
}
.component {
  appearance: var(--book-appearance, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  appearance: initial;
}

@supports (appearance: initial) {
  .component { appearance: var(--book-appearance, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `accent-color`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `accent-color` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

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

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `caret-shape`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `caret-shape` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `caret-shape` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `caret-shape` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { caret-shape: initial; }
```

**Example: Component token.**

```css
:root {
  --book-caret-shape: initial;
}
.component {
  caret-shape: var(--book-caret-shape, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  caret-shape: initial;
}

@supports (caret-shape: initial) {
  .component { caret-shape: var(--book-caret-shape, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `content`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `content` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `content` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `content` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { content: normal; }
```

**Example: Component token.**

```css
:root {
  --book-content: initial;
}
.component {
  content: var(--book-content, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  content: initial;
}

@supports (content: initial) {
  .component { content: var(--book-content, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `counter-increment`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `counter-increment` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `counter-increment` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `counter-increment` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { counter-increment: none; }
```

**Example: Component token.**

```css
:root {
  --book-counter-increment: initial;
}
.component {
  counter-increment: var(--book-counter-increment, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  counter-increment: initial;
}

@supports (counter-increment: initial) {
  .component { counter-increment: var(--book-counter-increment, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `counter-reset`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `counter-reset` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `counter-reset` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `counter-reset` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { counter-reset: none; }
```

**Example: Component token.**

```css
:root {
  --book-counter-reset: initial;
}
.component {
  counter-reset: var(--book-counter-reset, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  counter-reset: initial;
}

@supports (counter-reset: initial) {
  .component { counter-reset: var(--book-counter-reset, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `counter-set`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `counter-set` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `counter-set` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `counter-set` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { counter-set: initial; }
```

**Example: Component token.**

```css
:root {
  --book-counter-set: initial;
}
.component {
  counter-set: var(--book-counter-set, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  counter-set: initial;
}

@supports (counter-set: initial) {
  .component { counter-set: var(--book-counter-set, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `field-sizing`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `field-sizing` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `field-sizing` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `field-sizing` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { field-sizing: initial; }
```

**Example: Component token.**

```css
:root {
  --book-field-sizing: initial;
}
.component {
  field-sizing: var(--book-field-sizing, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  field-sizing: initial;
}

@supports (field-sizing: initial) {
  .component { field-sizing: var(--book-field-sizing, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `list-style`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `list-style` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `list-style` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `list-style` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { list-style: disc; }
```

**Example: Component token.**

```css
:root {
  --book-list-style: initial;
}
.component {
  list-style: var(--book-list-style, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  list-style: initial;
}

@supports (list-style: initial) {
  .component { list-style: var(--book-list-style, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `list-style-image`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `list-style-image` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `list-style-image` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `list-style-image` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { list-style-image: initial; }
```

**Example: Component token.**

```css
:root {
  --book-list-style-image: initial;
}
.component {
  list-style-image: var(--book-list-style-image, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  list-style-image: initial;
}

@supports (list-style-image: initial) {
  .component { list-style-image: var(--book-list-style-image, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `list-style-position`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `list-style-position` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `list-style-position` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `list-style-position` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { list-style-position: initial; }
```

**Example: Component token.**

```css
:root {
  --book-list-style-position: initial;
}
.component {
  list-style-position: var(--book-list-style-position, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  list-style-position: initial;
}

@supports (list-style-position: initial) {
  .component { list-style-position: var(--book-list-style-position, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `list-style-type`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `list-style-type` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `list-style-type` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `list-style-type` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { list-style-type: disc; }
```

**Example: Component token.**

```css
:root {
  --book-list-style-type: initial;
}
.component {
  list-style-type: var(--book-list-style-type, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  list-style-type: initial;
}

@supports (list-style-type: initial) {
  .component { list-style-type: var(--book-list-style-type, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `marker`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `marker` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `marker` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `marker` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { marker: initial; }
```

**Example: Component token.**

```css
:root {
  --book-marker: initial;
}
.component {
  marker: var(--book-marker, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  marker: initial;
}

@supports (marker: initial) {
  .component { marker: var(--book-marker, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `object-fit`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `object-fit` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `object-fit` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `object-fit` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { object-fit: cover; }
```

**Example: Component token.**

```css
:root {
  --book-object-fit: initial;
}
.component {
  object-fit: var(--book-object-fit, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  object-fit: initial;
}

@supports (object-fit: initial) {
  .component { object-fit: var(--book-object-fit, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `quotes`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `quotes` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `quotes` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `quotes` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { quotes: initial; }
```

**Example: Component token.**

```css
:root {
  --book-quotes: initial;
}
.component {
  quotes: var(--book-quotes, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  quotes: initial;
}

@supports (quotes: initial) {
  .component { quotes: var(--book-quotes, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `ruby-align`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `ruby-align` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `ruby-align` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `ruby-align` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { ruby-align: initial; }
```

**Example: Component token.**

```css
:root {
  --book-ruby-align: initial;
}
.component {
  ruby-align: var(--book-ruby-align, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  ruby-align: initial;
}

@supports (ruby-align: initial) {
  .component { ruby-align: var(--book-ruby-align, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `ruby-position`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `ruby-position` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `ruby-position` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `ruby-position` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { ruby-position: initial; }
```

**Example: Component token.**

```css
:root {
  --book-ruby-position: initial;
}
.component {
  ruby-position: var(--book-ruby-position, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  ruby-position: initial;
}

@supports (ruby-position: initial) {
  .component { ruby-position: var(--book-ruby-position, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `speak`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `speak` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `speak` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `speak` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { speak: initial; }
```

**Example: Component token.**

```css
:root {
  --book-speak: initial;
}
.component {
  speak: var(--book-speak, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  speak: initial;
}

@supports (speak: initial) {
  .component { speak: var(--book-speak, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `text-combine-upright`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `text-combine-upright` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `text-combine-upright` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `text-combine-upright` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { text-combine-upright: initial; }
```

**Example: Component token.**

```css
:root {
  --book-text-combine-upright: initial;
}
.component {
  text-combine-upright: var(--book-text-combine-upright, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  text-combine-upright: initial;
}

@supports (text-combine-upright: initial) {
  .component { text-combine-upright: var(--book-text-combine-upright, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.

### `user-select`

**Role.** This property styles semantic content, controls, counters, lists, tables, or generated content. The `user-select` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

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

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Forms, lists, tables, and generated content` chapter before changing a component-wide contract.
