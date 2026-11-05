# Property reference: Responsive, logical, and container-aware CSS

> **How to use this section:** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. Each entry follows the same editorial pattern so it can be indexed, typeset, and reviewed consistently.

### `container`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `container` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `container` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `container` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { container: initial; }
```

**Example: Component token.**

```css
:root {
  --book-container: initial;
}
.component {
  container: var(--book-container, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  container: initial;
}

@supports (container: initial) {
  .component { container: var(--book-container, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `container-name`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `container-name` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `container-name` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `container-name` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { container-name: initial; }
```

**Example: Component token.**

```css
:root {
  --book-container-name: initial;
}
.component {
  container-name: var(--book-container-name, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  container-name: initial;
}

@supports (container-name: initial) {
  .component { container-name: var(--book-container-name, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `container-type`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `container-type` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `container-type` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `container-type` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { container-type: initial; }
```

**Example: Component token.**

```css
:root {
  --book-container-type: initial;
}
.component {
  container-type: var(--book-container-type, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  container-type: initial;
}

@supports (container-type: initial) {
  .component { container-type: var(--book-container-type, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `direction`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `direction` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `direction` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `direction` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { direction: initial; }
```

**Example: Component token.**

```css
:root {
  --book-direction: initial;
}
.component {
  direction: var(--book-direction, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  direction: initial;
}

@supports (direction: initial) {
  .component { direction: var(--book-direction, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `env`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `env` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `env` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `env` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { env: initial; }
```

**Example: Component token.**

```css
:root {
  --book-env: initial;
}
.component {
  env: var(--book-env, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  env: initial;
}

@supports (env: initial) {
  .component { env: var(--book-env, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `fallback`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `fallback` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `fallback` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `fallback` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { fallback: initial; }
```

**Example: Component token.**

```css
:root {
  --book-fallback: initial;
}
.component {
  fallback: var(--book-fallback, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  fallback: initial;
}

@supports (fallback: initial) {
  .component { fallback: var(--book-fallback, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `max-block-size`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `max-block-size` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `max-block-size` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `max-block-size` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { max-block-size: min(100%, 40rem); }
```

**Example: Component token.**

```css
:root {
  --book-max-block-size: initial;
}
.component {
  max-block-size: var(--book-max-block-size, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  max-block-size: initial;
}

@supports (max-block-size: initial) {
  .component { max-block-size: var(--book-max-block-size, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `max-inline-size`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `max-inline-size` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `max-inline-size` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `max-inline-size` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { max-inline-size: min(100%, 40rem); }
```

**Example: Component token.**

```css
:root {
  --book-max-inline-size: initial;
}
.component {
  max-inline-size: var(--book-max-inline-size, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  max-inline-size: initial;
}

@supports (max-inline-size: initial) {
  .component { max-inline-size: var(--book-max-inline-size, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `min-block-size`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `min-block-size` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `min-block-size` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `min-block-size` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { min-block-size: min(100%, 40rem); }
```

**Example: Component token.**

```css
:root {
  --book-min-block-size: initial;
}
.component {
  min-block-size: var(--book-min-block-size, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  min-block-size: initial;
}

@supports (min-block-size: initial) {
  .component { min-block-size: var(--book-min-block-size, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `min-inline-size`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `min-inline-size` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `min-inline-size` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `min-inline-size` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { min-inline-size: min(100%, 40rem); }
```

**Example: Component token.**

```css
:root {
  --book-min-inline-size: initial;
}
.component {
  min-inline-size: var(--book-min-inline-size, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  min-inline-size: initial;
}

@supports (min-inline-size: initial) {
  .component { min-inline-size: var(--book-min-inline-size, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `object-view-box`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `object-view-box` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `object-view-box` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `object-view-box` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { object-view-box: initial; }
```

**Example: Component token.**

```css
:root {
  --book-object-view-box: initial;
}
.component {
  object-view-box: var(--book-object-view-box, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  object-view-box: initial;
}

@supports (object-view-box: initial) {
  .component { object-view-box: var(--book-object-view-box, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `orientation`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `orientation` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `orientation` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `orientation` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { orientation: initial; }
```

**Example: Component token.**

```css
:root {
  --book-orientation: initial;
}
.component {
  orientation: var(--book-orientation, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  orientation: initial;
}

@supports (orientation: initial) {
  .component { orientation: var(--book-orientation, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `page`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `page` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `page` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `page` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { page: initial; }
```

**Example: Component token.**

```css
:root {
  --book-page: initial;
}
.component {
  page: var(--book-page, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  page: initial;
}

@supports (page: initial) {
  .component { page: var(--book-page, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `page-break-after`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `page-break-after` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `page-break-after` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `page-break-after` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { page-break-after: initial; }
```

**Example: Component token.**

```css
:root {
  --book-page-break-after: initial;
}
.component {
  page-break-after: var(--book-page-break-after, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  page-break-after: initial;
}

@supports (page-break-after: initial) {
  .component { page-break-after: var(--book-page-break-after, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `page-break-before`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `page-break-before` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `page-break-before` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `page-break-before` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { page-break-before: initial; }
```

**Example: Component token.**

```css
:root {
  --book-page-break-before: initial;
}
.component {
  page-break-before: var(--book-page-break-before, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  page-break-before: initial;
}

@supports (page-break-before: initial) {
  .component { page-break-before: var(--book-page-break-before, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `page-break-inside`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `page-break-inside` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `page-break-inside` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `page-break-inside` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { page-break-inside: initial; }
```

**Example: Component token.**

```css
:root {
  --book-page-break-inside: initial;
}
.component {
  page-break-inside: var(--book-page-break-inside, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  page-break-inside: initial;
}

@supports (page-break-inside: initial) {
  .component { page-break-inside: var(--book-page-break-inside, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `print-color-adjust`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `print-color-adjust` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

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

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `quotes`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `quotes` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

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

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `resolution`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `resolution` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `resolution` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `resolution` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { resolution: initial; }
```

**Example: Component token.**

```css
:root {
  --book-resolution: initial;
}
.component {
  resolution: var(--book-resolution, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  resolution: initial;
}

@supports (resolution: initial) {
  .component { resolution: var(--book-resolution, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `size`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `size` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `size` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `size` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { size: initial; }
```

**Example: Component token.**

```css
:root {
  --book-size: initial;
}
.component {
  size: var(--book-size, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  size: initial;
}

@supports (size: initial) {
  .component { size: var(--book-size, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `text-size-adjust`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `text-size-adjust` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `text-size-adjust` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `text-size-adjust` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { text-size-adjust: initial; }
```

**Example: Component token.**

```css
:root {
  --book-text-size-adjust: initial;
}
.component {
  text-size-adjust: var(--book-text-size-adjust, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  text-size-adjust: initial;
}

@supports (text-size-adjust: initial) {
  .component { text-size-adjust: var(--book-text-size-adjust, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `unicode-bidi`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `unicode-bidi` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `unicode-bidi` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `unicode-bidi` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { unicode-bidi: initial; }
```

**Example: Component token.**

```css
:root {
  --book-unicode-bidi: initial;
}
.component {
  unicode-bidi: var(--book-unicode-bidi, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  unicode-bidi: initial;
}

@supports (unicode-bidi: initial) {
  .component { unicode-bidi: var(--book-unicode-bidi, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `viewport-fit`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `viewport-fit` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `viewport-fit` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `viewport-fit` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { viewport-fit: initial; }
```

**Example: Component token.**

```css
:root {
  --book-viewport-fit: initial;
}
.component {
  viewport-fit: var(--book-viewport-fit, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  viewport-fit: initial;
}

@supports (viewport-fit: initial) {
  .component { viewport-fit: var(--book-viewport-fit, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.

### `zoom`

**Role.** This property helps CSS adapt to writing mode, page context, viewport state, or container conditions. The `zoom` property is commonly used when a component needs an explicit, inspectable contract instead of relying on browser defaults.

**Syntax and values.** Start with the formal syntax on the MDN reference page. In production, prefer a valid baseline value, then add a modern value only when it improves the experience. Common value families include keywords, lengths, percentages, colors, custom-identifiers, functions, and global keywords such as `inherit`, `initial`, `unset`, `revert`, and `revert-layer`.

**Practical guidance.** Use `zoom` where its behavior is part of the component design. Keep the declaration close to the selector that owns it, use a custom property when consumers need a supported token, and avoid coupling the rule to a fragile DOM depth. Check computed styles when debugging because the authored declaration may be overridden, inherited, or invalid after variable substitution. The snippets below use a concrete baseline plus a tokenized form so they remain useful when copied into a real stylesheet.

**Fallback and compatibility.** Treat the feature as progressive enhancement if it is new, experimental, vendor-prefixed, or dependent on a newer value grammar. Put the baseline first, use `@supports` for meaningful capability detection, and verify the exact target browsers with Can I Use and MDN compatibility data. Do not claim that a syntax transform reproduces a browser layout algorithm.

**Accessibility and performance.** Confirm that the declaration does not hide focus, clip essential content, reduce contrast, disable zoom, or create motion that ignores user preferences. If `zoom` is read or written through CSSOM, batch reads and writes and validate any external input.

**Example: Minimal declaration.**

```css
.component { zoom: initial; }
```

**Example: Component token.**

```css
:root {
  --book-zoom: initial;
}
.component {
  zoom: var(--book-zoom, initial);
}
```

**Example: Progressive enhancement.**

```css
.component {
  zoom: initial;
}

@supports (zoom: initial) {
  .component { zoom: var(--book-zoom, initial); }
}
```

**Related concepts.** See the surrounding entries for neighboring longhands and shorthands, and review the `Responsive, logical, and container-aware CSS` chapter before changing a component-wide contract.
