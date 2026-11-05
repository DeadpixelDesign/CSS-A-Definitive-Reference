# Property reference: Modern CSS and progressive enhancement

> **How to use this section:** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. Each entry follows the same editorial pattern so it can be indexed, typeset, and reviewed consistently.

### `anchor-name`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `anchor-name` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `anchor-name` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `anchor-name` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { anchor-name: initial; }
```

**Example: Component token.**

```css
:root {
  --book-anchor-name: initial;
}
.component {
  anchor-name: var(--book-anchor-name, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  anchor-name: initial;
}

@supports (anchor-name: initial) {
  .component { anchor-name: var(--book-anchor-name, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `anchor-scope`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `anchor-scope` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `anchor-scope` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `anchor-scope` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { anchor-scope: initial; }
```

**Example: Component token.**

```css
:root {
  --book-anchor-scope: initial;
}
.component {
  anchor-scope: var(--book-anchor-scope, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  anchor-scope: initial;
}

@supports (anchor-scope: initial) {
  .component { anchor-scope: var(--book-anchor-scope, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `backdrop-filter`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `backdrop-filter` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `backdrop-filter` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `backdrop-filter` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { backdrop-filter: initial; }
```

**Example: Component token.**

```css
:root {
  --book-backdrop-filter: initial;
}
.component {
  backdrop-filter: var(--book-backdrop-filter, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  backdrop-filter: initial;
}

@supports (backdrop-filter: initial) {
  .component { backdrop-filter: var(--book-backdrop-filter, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `baseline-source`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `baseline-source` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `baseline-source` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `baseline-source` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { baseline-source: initial; }
```

**Example: Component token.**

```css
:root {
  --book-baseline-source: initial;
}
.component {
  baseline-source: var(--book-baseline-source, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  baseline-source: initial;
}

@supports (baseline-source: initial) {
  .component { baseline-source: var(--book-baseline-source, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `block-ellipsis`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `block-ellipsis` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `block-ellipsis` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `block-ellipsis` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { block-ellipsis: initial; }
```

**Example: Component token.**

```css
:root {
  --book-block-ellipsis: initial;
}
.component {
  block-ellipsis: var(--book-block-ellipsis, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  block-ellipsis: initial;
}

@supports (block-ellipsis: initial) {
  .component { block-ellipsis: var(--book-block-ellipsis, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `color-interpolation`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `color-interpolation` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `color-interpolation` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `color-interpolation` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { color-interpolation: initial; }
```

**Example: Component token.**

```css
:root {
  --book-color-interpolation: initial;
}
.component {
  color-interpolation: var(--book-color-interpolation, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  color-interpolation: initial;
}

@supports (color-interpolation: initial) {
  .component { color-interpolation: var(--book-color-interpolation, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `color-interpolation-filters`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `color-interpolation-filters` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `color-interpolation-filters` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `color-interpolation-filters` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { color-interpolation-filters: initial; }
```

**Example: Component token.**

```css
:root {
  --book-color-interpolation-filters: initial;
}
.component {
  color-interpolation-filters: var(--book-color-interpolation-filters, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  color-interpolation-filters: initial;
}

@supports (color-interpolation-filters: initial) {
  .component { color-interpolation-filters: var(--book-color-interpolation-filters, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `color-mix`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `color-mix` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `color-mix` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `color-mix` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { color-mix: initial; }
```

**Example: Component token.**

```css
:root {
  --book-color-mix: initial;
}
.component {
  color-mix: var(--book-color-mix, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  color-mix: initial;
}

@supports (color-mix: initial) {
  .component { color-mix: var(--book-color-mix, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `corner-shape`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `corner-shape` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `corner-shape` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `corner-shape` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { corner-shape: initial; }
```

**Example: Component token.**

```css
:root {
  --book-corner-shape: initial;
}
.component {
  corner-shape: var(--book-corner-shape, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  corner-shape: initial;
}

@supports (corner-shape: initial) {
  .component { corner-shape: var(--book-corner-shape, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `cursor`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `cursor` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `cursor` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `cursor` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { cursor: pointer; }
```

**Example: Component token.**

```css
:root {
  --book-cursor: initial;
}
.component {
  cursor: var(--book-cursor, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  cursor: initial;
}

@supports (cursor: initial) {
  .component { cursor: var(--book-cursor, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `dynamic-range-limit`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `dynamic-range-limit` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `dynamic-range-limit` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `dynamic-range-limit` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { dynamic-range-limit: initial; }
```

**Example: Component token.**

```css
:root {
  --book-dynamic-range-limit: initial;
}
.component {
  dynamic-range-limit: var(--book-dynamic-range-limit, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  dynamic-range-limit: initial;
}

@supports (dynamic-range-limit: initial) {
  .component { dynamic-range-limit: var(--book-dynamic-range-limit, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `field-sizing`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `field-sizing` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

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

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `interpolate-size`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `interpolate-size` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `interpolate-size` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `interpolate-size` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { interpolate-size: initial; }
```

**Example: Component token.**

```css
:root {
  --book-interpolate-size: initial;
}
.component {
  interpolate-size: var(--book-interpolate-size, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  interpolate-size: initial;
}

@supports (interpolate-size: initial) {
  .component { interpolate-size: var(--book-interpolate-size, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `interest-delay`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `interest-delay` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `interest-delay` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `interest-delay` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { interest-delay: initial; }
```

**Example: Component token.**

```css
:root {
  --book-interest-delay: initial;
}
.component {
  interest-delay: var(--book-interest-delay, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  interest-delay: initial;
}

@supports (interest-delay: initial) {
  .component { interest-delay: var(--book-interest-delay, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `interest-target`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `interest-target` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `interest-target` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `interest-target` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { interest-target: initial; }
```

**Example: Component token.**

```css
:root {
  --book-interest-target: initial;
}
.component {
  interest-target: var(--book-interest-target, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  interest-target: initial;
}

@supports (interest-target: initial) {
  .component { interest-target: var(--book-interest-target, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `light-dark`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `light-dark` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `light-dark` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `light-dark` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { light-dark: initial; }
```

**Example: Component token.**

```css
:root {
  --book-light-dark: initial;
}
.component {
  light-dark: var(--book-light-dark, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  light-dark: initial;
}

@supports (light-dark: initial) {
  .component { light-dark: var(--book-light-dark, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `line-clamp`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `line-clamp` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `line-clamp` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `line-clamp` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { line-clamp: initial; }
```

**Example: Component token.**

```css
:root {
  --book-line-clamp: initial;
}
.component {
  line-clamp: var(--book-line-clamp, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  line-clamp: initial;
}

@supports (line-clamp: initial) {
  .component { line-clamp: var(--book-line-clamp, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `position-anchor`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `position-anchor` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `position-anchor` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `position-anchor` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { position-anchor: initial; }
```

**Example: Component token.**

```css
:root {
  --book-position-anchor: initial;
}
.component {
  position-anchor: var(--book-position-anchor, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  position-anchor: initial;
}

@supports (position-anchor: initial) {
  .component { position-anchor: var(--book-position-anchor, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `position-area`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `position-area` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `position-area` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `position-area` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { position-area: initial; }
```

**Example: Component token.**

```css
:root {
  --book-position-area: initial;
}
.component {
  position-area: var(--book-position-area, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  position-area: initial;
}

@supports (position-area: initial) {
  .component { position-area: var(--book-position-area, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `position-try`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `position-try` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `position-try` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `position-try` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { position-try: initial; }
```

**Example: Component token.**

```css
:root {
  --book-position-try: initial;
}
.component {
  position-try: var(--book-position-try, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  position-try: initial;
}

@supports (position-try: initial) {
  .component { position-try: var(--book-position-try, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `position-try-fallbacks`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `position-try-fallbacks` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `position-try-fallbacks` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `position-try-fallbacks` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { position-try-fallbacks: initial; }
```

**Example: Component token.**

```css
:root {
  --book-position-try-fallbacks: initial;
}
.component {
  position-try-fallbacks: var(--book-position-try-fallbacks, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  position-try-fallbacks: initial;
}

@supports (position-try-fallbacks: initial) {
  .component { position-try-fallbacks: var(--book-position-try-fallbacks, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `position-try-order`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `position-try-order` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `position-try-order` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `position-try-order` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { position-try-order: initial; }
```

**Example: Component token.**

```css
:root {
  --book-position-try-order: initial;
}
.component {
  position-try-order: var(--book-position-try-order, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  position-try-order: initial;
}

@supports (position-try-order: initial) {
  .component { position-try-order: var(--book-position-try-order, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `scroll-marker-group`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `scroll-marker-group` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `scroll-marker-group` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `scroll-marker-group` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { scroll-marker-group: initial; }
```

**Example: Component token.**

```css
:root {
  --book-scroll-marker-group: initial;
}
.component {
  scroll-marker-group: var(--book-scroll-marker-group, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  scroll-marker-group: initial;
}

@supports (scroll-marker-group: initial) {
  .component { scroll-marker-group: var(--book-scroll-marker-group, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `text-box`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `text-box` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `text-box` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `text-box` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { text-box: initial; }
```

**Example: Component token.**

```css
:root {
  --book-text-box: initial;
}
.component {
  text-box: var(--book-text-box, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  text-box: initial;
}

@supports (text-box: initial) {
  .component { text-box: var(--book-text-box, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `text-box-edge`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `text-box-edge` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `text-box-edge` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `text-box-edge` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { text-box-edge: initial; }
```

**Example: Component token.**

```css
:root {
  --book-text-box-edge: initial;
}
.component {
  text-box-edge: var(--book-text-box-edge, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  text-box-edge: initial;
}

@supports (text-box-edge: initial) {
  .component { text-box-edge: var(--book-text-box-edge, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `text-box-trim`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `text-box-trim` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `text-box-trim` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `text-box-trim` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { text-box-trim: initial; }
```

**Example: Component token.**

```css
:root {
  --book-text-box-trim: initial;
}
.component {
  text-box-trim: var(--book-text-box-trim, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  text-box-trim: initial;
}

@supports (text-box-trim: initial) {
  .component { text-box-trim: var(--book-text-box-trim, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `text-wrap`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `text-wrap` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `text-wrap` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `text-wrap` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { text-wrap: balance; }
```

**Example: Component token.**

```css
:root {
  --book-text-wrap: initial;
}
.component {
  text-wrap: var(--book-text-wrap, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  text-wrap: initial;
}

@supports (text-wrap: initial) {
  .component { text-wrap: var(--book-text-wrap, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `timeline-scope`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `timeline-scope` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `timeline-scope` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `timeline-scope` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { timeline-scope: initial; }
```

**Example: Component token.**

```css
:root {
  --book-timeline-scope: initial;
}
.component {
  timeline-scope: var(--book-timeline-scope, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  timeline-scope: initial;
}

@supports (timeline-scope: initial) {
  .component { timeline-scope: var(--book-timeline-scope, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.

### `view-transition-name`

**Role.** This is an evolving or recently expanded feature. Gate it, test it, and provide a useful baseline. The `view-transition-name` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `view-transition-name` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `view-transition-name` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { view-transition-name: initial; }
```

**Example: Component token.**

```css
:root {
  --book-view-transition-name: initial;
}
.component {
  view-transition-name: var(--book-view-transition-name, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  view-transition-name: initial;
}

@supports (view-transition-name: initial) {
  .component { view-transition-name: var(--book-view-transition-name, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Modern CSS and progressive enhancement` chapter before changing a component-wide contract.
