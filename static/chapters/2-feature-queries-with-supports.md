# Feature queries with `@supports`

The `@supports` at-rule is CSS's feature-query mechanism. It lets a stylesheet ask whether a browser understands a particular declaration or selector condition, then apply an enhancement only when the answer is yes. The browser evaluates the condition while parsing the stylesheet; unsupported declarations inside a false block are ignored without preventing the rest of the stylesheet from loading.

Feature queries are most useful when the fallback is already complete. Write the broadly supported experience first, then layer the enhancement on top. This makes the page readable and usable in browsers that do not understand the newer feature.

### The basic shape

```css
.cards {
  display: block;
}

@supports (display: grid) {
  .cards {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }
}
```

The condition contains a declaration in parentheses: `(property: value)`. If the browser recognizes the property and accepts the value grammar, the declarations inside the block become eligible for the cascade. If not, the fallback remains in effect.

### Test the feature you actually need

A property-level test can be too broad. For example, testing `(display: grid)` only proves that Grid exists; it does not prove that every value or behavior your component needs is supported. Test the exact syntax that changes the implementation.

```css
.layout {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

@supports (grid-template-columns: subgrid) {
  .layout {
    display: grid;
    grid-template-columns: subgrid;
  }
}
```

The fallback is flexbox. The enhancement is specifically `subgrid`, rather than a generic Grid test, because `subgrid` is the capability the layout depends on.

### Combine conditions with `and`, `or`, and `not`

Conditions can be composed. Use `and` when every capability is required, `or` when more than one implementation is acceptable, and `not` when an alternate path is needed.

```css
@supports (display: grid) and (gap: 1rem) {
  .toolbar {
    display: grid;
    gap: 1rem;
  }
}

@supports (text-wrap: balance) or (text-wrap: pretty) {
  .headline {
    text-wrap: balance;
  }
}

@supports not (selector(:has(*))) {
  .field:invalid {
    outline: 2px solid crimson;
  }
}
```

Keep compound conditions readable. A long query is a sign that the component may need a simpler fallback or a separate enhancement layer.

### Query selector support

The `selector()` function tests whether a browser can parse a selector. This is useful for selector features whose support cannot be expressed as a property/value pair.

```css
.card {
  border: 1px solid var(--line);
}

@supports selector(:has(*)) {
  .card:has(.media) {
    grid-template-columns: 12rem 1fr;
  }
}
```

The selector must be valid inside `selector()`. Use `selector(:where(*))` or another representative selector when the exact selector feature matters. The test detects parsing support; it does not guarantee that the selector is cheap to evaluate or that the surrounding layout is appropriate.

### Use the cascade to make the fallback obvious

The most maintainable pattern is baseline first, enhancement second. Keep the fallback declarations near the enhanced declarations so a reader can compare the two paths.

```css
.dialog {
  position: fixed;
  inset: 1rem;
  margin: auto;
  max-inline-size: 36rem;
}

@supports (inset: 0) {
  .dialog {
    inset: 50% auto auto 50%;
    translate: -50% -50%;
  }
}
```

If an enhancement is more complex, put it in a named layer. This keeps feature-query declarations from unexpectedly defeating component or utility styles.

```css
@layer base, components, enhancements;

@layer components {
  .panel {
    padding: 1rem;
    border: 1px solid var(--line);
  }
}

@layer enhancements {
  @supports (backdrop-filter: blur(1rem)) {
    .panel {
      background: rgb(255 255 255 / .65);
      backdrop-filter: blur(1rem);
    }
  }
}
```

### `@supports` is not browser detection

A feature query answers whether the current browser accepts syntax. It does not identify the browser, its version, the operating system, the device, available memory, network quality, or whether a feature is enabled by a user preference. Do not use it to target a browser by name or to infer performance.

```css
/* Good: ask whether this exact value is understood. */
@supports (scroll-timeline-name: --reading) {
  .progress {
    animation-timeline: --reading;
  }
}

/* Fragile: a browser name is not a capability query. */
/* .chrome .progress { ... } */
```

For actual runtime conditions, combine feature queries with media queries, container queries, accessibility preferences, and normal application state. A browser may support a feature while a user has disabled animation or while the available container is too narrow.

### Custom properties need a careful test

Most modern browsers parse custom properties, so `@supports (--theme-color: teal)` is rarely a useful test for whether a component can use a token. It checks custom-property syntax, not whether a browser understands the property that consumes the token.

```css
:root {
  --accent: #1d4ed8;
}

.button {
  background: #1d4ed8;
  background: var(--accent);
}

@supports (color: color-mix(in srgb, red, white)) {
  .button:hover {
    background: color-mix(in srgb, var(--accent), white 20%);
  }
}
```

Test the consuming feature, such as `color-mix()`, instead of testing only that variables exist. Always provide a valid fallback before the feature query when the enhanced value affects a critical color, size, or layout.

### Feature queries and progressive enhancement

Use `@supports` when the browser can safely ignore the enhancement. For a decorative gradient, blur, or improved layout, graceful degradation is usually enough. For a change that affects reading order, form submission, focus management, or content visibility, the HTML and baseline CSS must remain correct without the enhancement.

```css
.article-list {
  display: block;
}

.article-list > article {
  margin-block-end: 1rem;
}

@supports (display: grid) {
  .article-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
    gap: 1rem;
  }

  .article-list > article {
    margin-block-end: 0;
  }
}
```

The fallback still produces a sensible reading order. The enhanced layout changes arrangement, not meaning.

### JavaScript can ask the same question

When CSS alone is sufficient, keep the decision in CSS. When JavaScript must coordinate behavior with the CSS enhancement, use `CSS.supports()` with the same declaration or selector condition.

```js
const supportsGrid = CSS.supports('display', 'grid');
const supportsHas = CSS.supports('selector(:has(*))');

if (supportsGrid) {
  document.documentElement.dataset.grid = 'true';
}

if (supportsHas) {
  document.documentElement.classList.add('has-has-selector');
}
```

Do not duplicate a large CSS decision tree in JavaScript. Adding a class should coordinate behavior or analytics, not become a second layout engine. Guard `CSS.supports` if the script must run in very old environments:

```js
const canUseFeatureQueries =
  typeof CSS !== 'undefined' && typeof CSS.supports === 'function';
```

### Debugging feature queries

If an enhancement is not appearing, inspect the following in order:

1. Confirm the `@supports` condition is syntactically valid.
2. Test the exact property/value or selector in DevTools.
3. Check whether the feature query block is inside an unexpected `@layer`, `@media`, `@scope`, or container query.
4. Inspect whether a later declaration wins in the cascade.
5. Verify that the fallback is not being mistaken for a failed build or missing stylesheet.
6. Check the target browser data before deciding whether a polyfill or alternate implementation is necessary.

```css
/* A visible diagnostic that can be removed after testing. */
@supports (display: grid) {
  body::before {
    content: 'Grid supported';
    position: fixed;
    inset: auto 1rem 1rem auto;
    z-index: 9999;
    padding: .5rem .75rem;
    color: white;
    background: #0f766e;
  }
}
```

Do not ship a diagnostic banner accidentally. Prefer DevTools' computed styles and the browser's compatibility panel for final verification.

### Compatibility and source trail

Consult current compatibility data before shipping a feature query. `@supports` itself is broadly available, but the feature being queried may not be.

- MDN `@supports`: https://developer.mozilla.org/en-US/docs/Web/CSS/@supports
- MDN `CSS.supports()`: https://developer.mozilla.org/en-US/docs/Web/API/CSS/supports_static
- Can I Use CSS feature queries: https://caniuse.com/css-featurequeries
- web.dev Learn CSS: https://web.dev/learn/css
