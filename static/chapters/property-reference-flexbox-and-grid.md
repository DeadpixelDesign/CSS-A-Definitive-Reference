# Property reference: Flexbox and Grid

> **How to use this section:** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. Each entry follows the same editorial pattern so it can be indexed, typeset, and reviewed consistently.

### `align-content`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `align-content` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `align-content` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `align-content` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { align-content: start; }
```

**Example: Component token.**

```css
:root {
  --book-align-content: initial;
}
.component {
  align-content: var(--book-align-content, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  align-content: initial;
}

@supports (align-content: initial) {
  .component { align-content: var(--book-align-content, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `align-items`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `align-items` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `align-items` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `align-items` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { align-items: center; }
```

**Example: Component token.**

```css
:root {
  --book-align-items: initial;
}
.component {
  align-items: var(--book-align-items, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  align-items: initial;
}

@supports (align-items: initial) {
  .component { align-items: var(--book-align-items, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `align-self`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `align-self` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `align-self` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `align-self` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { align-self: auto; }
```

**Example: Component token.**

```css
:root {
  --book-align-self: initial;
}
.component {
  align-self: var(--book-align-self, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  align-self: initial;
}

@supports (align-self: initial) {
  .component { align-self: var(--book-align-self, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `column-rule`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `column-rule` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `column-rule` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `column-rule` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { column-rule: initial; }
```

**Example: Component token.**

```css
:root {
  --book-column-rule: initial;
}
.component {
  column-rule: var(--book-column-rule, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  column-rule: initial;
}

@supports (column-rule: initial) {
  .component { column-rule: var(--book-column-rule, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `flex`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `flex` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flex` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flex` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { flex: 1 1 auto; }
```

**Example: Component token.**

```css
:root {
  --book-flex: initial;
}
.component {
  flex: var(--book-flex, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flex: initial;
}

@supports (flex: initial) {
  .component { flex: var(--book-flex, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `flex-basis`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `flex-basis` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flex-basis` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flex-basis` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { flex-basis: auto; }
```

**Example: Component token.**

```css
:root {
  --book-flex-basis: initial;
}
.component {
  flex-basis: var(--book-flex-basis, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flex-basis: initial;
}

@supports (flex-basis: initial) {
  .component { flex-basis: var(--book-flex-basis, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `flex-direction`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `flex-direction` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flex-direction` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flex-direction` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { flex-direction: column; }
```

**Example: Component token.**

```css
:root {
  --book-flex-direction: initial;
}
.component {
  flex-direction: var(--book-flex-direction, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flex-direction: initial;
}

@supports (flex-direction: initial) {
  .component { flex-direction: var(--book-flex-direction, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `flex-flow`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `flex-flow` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flex-flow` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flex-flow` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { flex-flow: initial; }
```

**Example: Component token.**

```css
:root {
  --book-flex-flow: initial;
}
.component {
  flex-flow: var(--book-flex-flow, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flex-flow: initial;
}

@supports (flex-flow: initial) {
  .component { flex-flow: var(--book-flex-flow, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `flex-grow`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `flex-grow` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flex-grow` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flex-grow` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { flex-grow: 1; }
```

**Example: Component token.**

```css
:root {
  --book-flex-grow: initial;
}
.component {
  flex-grow: var(--book-flex-grow, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flex-grow: initial;
}

@supports (flex-grow: initial) {
  .component { flex-grow: var(--book-flex-grow, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `flex-shrink`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `flex-shrink` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flex-shrink` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flex-shrink` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { flex-shrink: 1; }
```

**Example: Component token.**

```css
:root {
  --book-flex-shrink: initial;
}
.component {
  flex-shrink: var(--book-flex-shrink, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flex-shrink: initial;
}

@supports (flex-shrink: initial) {
  .component { flex-shrink: var(--book-flex-shrink, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `flex-wrap`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `flex-wrap` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `flex-wrap` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `flex-wrap` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { flex-wrap: wrap; }
```

**Example: Component token.**

```css
:root {
  --book-flex-wrap: initial;
}
.component {
  flex-wrap: var(--book-flex-wrap, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  flex-wrap: initial;
}

@supports (flex-wrap: initial) {
  .component { flex-wrap: var(--book-flex-wrap, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `gap`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `gap` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `gap` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `gap` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { gap: 1rem; }
```

**Example: Component token.**

```css
:root {
  --book-gap: initial;
}
.component {
  gap: var(--book-gap, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  gap: initial;
}

@supports (gap: initial) {
  .component { gap: var(--book-gap, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid: initial;
}
.component {
  grid: var(--book-grid, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid: initial;
}

@supports (grid: initial) {
  .component { grid: var(--book-grid, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-area`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-area` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-area` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-area` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { grid-area: auto; }
```

**Example: Component token.**

```css
:root {
  --book-grid-area: initial;
}
.component {
  grid-area: var(--book-grid-area, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-area: initial;
}

@supports (grid-area: initial) {
  .component { grid-area: var(--book-grid-area, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-auto-columns`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-auto-columns` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-auto-columns` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-auto-columns` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid-auto-columns: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid-auto-columns: initial;
}
.component {
  grid-auto-columns: var(--book-grid-auto-columns, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-auto-columns: initial;
}

@supports (grid-auto-columns: initial) {
  .component { grid-auto-columns: var(--book-grid-auto-columns, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-auto-flow`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-auto-flow` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-auto-flow` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-auto-flow` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { grid-auto-flow: row; }
```

**Example: Component token.**

```css
:root {
  --book-grid-auto-flow: initial;
}
.component {
  grid-auto-flow: var(--book-grid-auto-flow, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-auto-flow: initial;
}

@supports (grid-auto-flow: initial) {
  .component { grid-auto-flow: var(--book-grid-auto-flow, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-auto-rows`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-auto-rows` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-auto-rows` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-auto-rows` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid-auto-rows: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid-auto-rows: initial;
}
.component {
  grid-auto-rows: var(--book-grid-auto-rows, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-auto-rows: initial;
}

@supports (grid-auto-rows: initial) {
  .component { grid-auto-rows: var(--book-grid-auto-rows, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-column`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-column` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-column` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-column` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { grid-column: auto; }
```

**Example: Component token.**

```css
:root {
  --book-grid-column: initial;
}
.component {
  grid-column: var(--book-grid-column, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-column: initial;
}

@supports (grid-column: initial) {
  .component { grid-column: var(--book-grid-column, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-column-end`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-column-end` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-column-end` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-column-end` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid-column-end: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid-column-end: initial;
}
.component {
  grid-column-end: var(--book-grid-column-end, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-column-end: initial;
}

@supports (grid-column-end: initial) {
  .component { grid-column-end: var(--book-grid-column-end, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-column-start`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-column-start` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-column-start` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-column-start` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid-column-start: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid-column-start: initial;
}
.component {
  grid-column-start: var(--book-grid-column-start, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-column-start: initial;
}

@supports (grid-column-start: initial) {
  .component { grid-column-start: var(--book-grid-column-start, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-row`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-row` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-row` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-row` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { grid-row: auto; }
```

**Example: Component token.**

```css
:root {
  --book-grid-row: initial;
}
.component {
  grid-row: var(--book-grid-row, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-row: initial;
}

@supports (grid-row: initial) {
  .component { grid-row: var(--book-grid-row, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-row-end`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-row-end` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-row-end` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-row-end` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid-row-end: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid-row-end: initial;
}
.component {
  grid-row-end: var(--book-grid-row-end, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-row-end: initial;
}

@supports (grid-row-end: initial) {
  .component { grid-row-end: var(--book-grid-row-end, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-row-start`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-row-start` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-row-start` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-row-start` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid-row-start: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid-row-start: initial;
}
.component {
  grid-row-start: var(--book-grid-row-start, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-row-start: initial;
}

@supports (grid-row-start: initial) {
  .component { grid-row-start: var(--book-grid-row-start, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-template`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-template` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-template` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-template` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid-template: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid-template: initial;
}
.component {
  grid-template: var(--book-grid-template, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-template: initial;
}

@supports (grid-template: initial) {
  .component { grid-template: var(--book-grid-template, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-template-areas`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-template-areas` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-template-areas` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-template-areas` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.layout { grid-template-areas: initial; }
```

**Example: Component token.**

```css
:root {
  --book-grid-template-areas: initial;
}
.component {
  grid-template-areas: var(--book-grid-template-areas, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-template-areas: initial;
}

@supports (grid-template-areas: initial) {
  .component { grid-template-areas: var(--book-grid-template-areas, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-template-columns`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-template-columns` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-template-columns` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-template-columns` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr)); }
```

**Example: Component token.**

```css
:root {
  --book-grid-template-columns: initial;
}
.component {
  grid-template-columns: var(--book-grid-template-columns, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-template-columns: initial;
}

@supports (grid-template-columns: initial) {
  .component { grid-template-columns: var(--book-grid-template-columns, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `grid-template-rows`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `grid-template-rows` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `grid-template-rows` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `grid-template-rows` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { grid-template-rows: auto; }
```

**Example: Component token.**

```css
:root {
  --book-grid-template-rows: initial;
}
.component {
  grid-template-rows: var(--book-grid-template-rows, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  grid-template-rows: initial;
}

@supports (grid-template-rows: initial) {
  .component { grid-template-rows: var(--book-grid-template-rows, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `justify-content`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `justify-content` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `justify-content` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `justify-content` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { justify-content: space-between; }
```

**Example: Component token.**

```css
:root {
  --book-justify-content: initial;
}
.component {
  justify-content: var(--book-justify-content, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  justify-content: initial;
}

@supports (justify-content: initial) {
  .component { justify-content: var(--book-justify-content, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `justify-items`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `justify-items` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `justify-items` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `justify-items` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { justify-items: stretch; }
```

**Example: Component token.**

```css
:root {
  --book-justify-items: initial;
}
.component {
  justify-items: var(--book-justify-items, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  justify-items: initial;
}

@supports (justify-items: initial) {
  .component { justify-items: var(--book-justify-items, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `justify-self`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `justify-self` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `justify-self` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `justify-self` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { justify-self: auto; }
```

**Example: Component token.**

```css
:root {
  --book-justify-self: initial;
}
.component {
  justify-self: var(--book-justify-self, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  justify-self: initial;
}

@supports (justify-self: initial) {
  .component { justify-self: var(--book-justify-self, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `place-content`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `place-content` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `place-content` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `place-content` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { place-content: start; }
```

**Example: Component token.**

```css
:root {
  --book-place-content: initial;
}
.component {
  place-content: var(--book-place-content, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  place-content: initial;
}

@supports (place-content: initial) {
  .component { place-content: var(--book-place-content, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `place-items`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `place-items` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `place-items` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `place-items` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { place-items: center; }
```

**Example: Component token.**

```css
:root {
  --book-place-items: initial;
}
.component {
  place-items: var(--book-place-items, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  place-items: initial;
}

@supports (place-items: initial) {
  .component { place-items: var(--book-place-items, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `place-self`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `place-self` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `place-self` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `place-self` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { place-self: auto; }
```

**Example: Component token.**

```css
:root {
  --book-place-self: initial;
}
.component {
  place-self: var(--book-place-self, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  place-self: initial;
}

@supports (place-self: initial) {
  .component { place-self: var(--book-place-self, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `row-gap`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `row-gap` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `row-gap` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `row-gap` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { row-gap: 1rem; }
```

**Example: Component token.**

```css
:root {
  --book-row-gap: initial;
}
.component {
  row-gap: var(--book-row-gap, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  row-gap: initial;
}

@supports (row-gap: initial) {
  .component { row-gap: var(--book-row-gap, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.

### `order`

**Role.** This property participates in one-dimensional Flexbox or two-dimensional Grid alignment and sizing. The `order` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `order` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `order` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { order: 0; }
```

**Example: Component token.**

```css
:root {
  --book-order: initial;
}
.component {
  order: var(--book-order, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  order: initial;
}

@supports (order: initial) {
  .component { order: var(--book-order, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Flexbox and Grid` chapter before changing a component-wide contract.
