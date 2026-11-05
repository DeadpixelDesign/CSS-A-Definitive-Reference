# Architecture, custom properties, and layers

A CSS architecture should make ownership visible. Tokens define shared decisions, components define local contracts, utilities provide narrowly scoped composition, and layers define precedence.

### Runtime tokens

Custom properties are inherited values in the cascade. They can be changed by themes, media queries, container queries, and JavaScript. Register typed properties with `@property` when animation or validation makes the contract worthwhile.

### Component contracts

Expose a small set of custom properties rather than allowing arbitrary descendants to reach inside a component. Document defaults, inheritance, and whether a token is safe to override.

### Cascade layers

Use a stable layer order. Imported vendor CSS should not be allowed to compete unpredictably with application CSS. Keep utility layers explicit and resist creating a new layer for every component.

### Architecture is an ownership map

CSS becomes difficult to maintain when every rule can override every other rule. An architecture gives each decision a home and makes the intended override path visible. A practical arrangement is:

```text
tokens       shared values and theme decisions
reset        predictable browser baseline
base         element defaults and readable document styles
objects      layout primitives such as stacks and clusters
components  named UI contracts such as card, dialog, and form
utilities    small, intentional one-purpose overrides
overrides    rare application-level exceptions
```

The names are not sacred. The ownership rules are. A token should not secretly contain component layout; a utility should not become a second component system; and a component should not depend on a selector chain outside its documented boundary.

### Establish layer order once

Declare the layer order near the top of the main stylesheet. Later normal layers win over earlier normal layers, so the order itself becomes a high-level API for precedence.

```css
@layer reset, base, objects, components, utilities, overrides;

@layer reset {
  *,
  *::before,
  *::after {
    box-sizing: border-box;
  }
}

@layer base {
  body {
    margin: 0;
    color: var(--color-ink);
    background: var(--color-surface);
  }
}
```

Put third-party styles in a named early layer so the application can override them without specificity escalation:

```css
@import url('vendor.css') layer(vendor);
@layer vendor, reset, base, components, utilities;
```

The order declaration should appear before rules that depend on it. Keep the list stable; inserting a new layer in the wrong position can change the behavior of an otherwise untouched application.

### Understand `!important` in layers

Layer precedence reverses for important declarations: important declarations in earlier layers take precedence over important declarations in later layers. This allows a reset or user-accessibility layer to protect a value from normal application overrides, but it can surprise maintainers.

```css
@layer reset, components, utilities;

@layer reset {
  [hidden] {
    display: none !important;
  }
}
```

Use `!important` as a boundary tool, not as a routine repair. First inspect ownership, layer order, specificity, and source order. A stylesheet with many important declarations has lost useful information about its design system.

### Separate global tokens from component tokens

Global tokens describe decisions shared across the product: color roles, type scale, spacing scale, radii, borders, and motion. Component tokens describe the small set of values a component intentionally exposes.

```css
:root {
  --color-ink: #172033;
  --color-surface: #ffffff;
  --color-accent: #1d4ed8;
  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .75rem;
  --space-4: 1rem;
  --radius-control: .5rem;
}

.button {
  --button-background: var(--color-accent);
  --button-ink: white;
  --button-radius: var(--radius-control);
}
```

Consumers can safely customize `--button-background` without reaching into the component’s internal selectors. Avoid exposing every internal measurement as a public token; a small API is easier to document and preserve.

### Custom properties are inherited values

Custom properties inherit by default, even when their names begin with a component-like prefix. They remain token streams until a real property consumes them. A variable can therefore be syntactically present but semantically invalid at computed-value time.

```css
:root {
  --accent: #1d4ed8;
}

.card {
  border-color: var(--accent);
  color: var(--text-color, #172033);
}
```

The fallback inside `var()` is used when the custom property is missing or invalid. It does not repair a value that is present but incompatible with the consuming property unless the entire declaration has an appropriate fallback.

```css
:root {
  --space: 1rem;
}

.panel {
  padding: var(--space, 1rem);
  inline-size: calc(100% - (2 * var(--space, 1rem)));
}
```

Use fallbacks at the consumption site. A component can then remain usable when it is rendered outside the theme that normally defines its tokens.

### Use `@property` for typed, animatable tokens

The `@property` rule registers a custom property with a syntax, inheritance behavior, and initial value. This is useful when a token should be validated or animated as a color, length, percentage, or number.

```css
@property --card-progress {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.card {
  --card-progress: 35%;
  background:
    linear-gradient(
      to right,
      var(--color-accent) var(--card-progress),
      transparent var(--card-progress)
    );
  transition: --card-progress 300ms ease;
}

.card[data-complete='true'] {
  --card-progress: 100%;
}
```

The registered syntax improves interpolation and validation, but it does not make every browser support the feature. Put a normal fallback before the enhancement when the registered property is optional.

### Theme with an explicit contract

Theme selectors should change semantic tokens, not rewrite every component selector. A `data-theme` attribute works well when the theme is an application state; `prefers-color-scheme` is useful as a user-preference baseline.

```css
:root {
  color-scheme: light dark;
  --color-surface: #ffffff;
  --color-ink: #172033;
  --color-muted: #5b6475;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-surface: #101827;
    --color-ink: #f4f7fb;
    --color-muted: #b8c1d1;
  }
}

[data-theme='dark'] {
  --color-surface: #101827;
  --color-ink: #f4f7fb;
  --color-muted: #b8c1d1;
}
```

If an explicit user choice exists, it should override the system preference. Store the choice in application state and apply the attribute early enough to avoid a flash of the wrong theme.

### Component contracts and local defaults

A component should define its own defaults and consume its public tokens locally. Use a fallback chain when the component supports both a local token and a global theme token.

```css
.alert {
  --alert-background: var(--surface-warning, #fff7db);
  --alert-border: var(--accent-warning, #a16207);
  --alert-ink: var(--ink-warning, #172033);

  padding: 1rem;
  border: 1px solid var(--alert-border);
  border-radius: .75rem;
  color: var(--alert-ink);
  background: var(--alert-background);
}

.alert[data-tone='danger'] {
  --alert-background: #fff1f0;
  --alert-border: #b42318;
}
```

This creates a stable contract: consumers can set `--surface-warning` globally or `--alert-background` locally, while the component retains a safe final fallback.

### Naming strategies

Naming conventions reduce accidental coupling. BEM-style names make ownership visible; utility names describe a single effect; data attributes represent state; and custom-property names distinguish global tokens from component APIs.

```html
<article class="card card--featured" data-state="expanded">
  <h2 class="card__title">A component contract</h2>
  <p class="u-muted">A utility adds one deliberate treatment.</p>
</article>
```

```css
.card { /* block */ }
.card__title { /* element */ }
.card--featured { /* modifier */ }
.u-muted { color: var(--color-muted); }
.card[data-state='expanded'] { /* state */ }
```

Do not combine several naming systems without documenting which one owns a declaration. A class that is both a component element and an ad hoc utility becomes difficult to refactor.

### Keep specificity low

Low specificity makes component APIs easier to override and makes layers more valuable. `:where()` contributes zero specificity and is useful for defaults; `:is()` groups selectors while retaining the specificity of its most specific argument.

```css
@layer components {
  :where(.card, .panel) {
    border: 1px solid var(--line);
    border-radius: .75rem;
  }

  :where(.card, .panel) :where(h2, h3) {
    margin-block: 0 1rem;
  }
}
```

Avoid selectors such as `main .page .sidebar nav ul li a` when a component class can express the same contract. Deep selectors couple the component to markup that its owner does not control.

### Scoping styles with `@scope`

`@scope` can limit a rule to a component boundary while preserving a clear relationship between the scope root and descendants. Use it when the supported browser range allows it and retain a class-based fallback when necessary.

```css
@scope (.profile-card) {
  :scope {
    display: grid;
    gap: 1rem;
  }

  .profile-card__name {
    margin: 0;
  }

  .profile-card__meta {
    color: var(--color-muted);
  }
}
```

Scoping is not permission to hide an API. Document which tokens, states, and descendant slots are public, and keep internals private by convention.

### Architecture for third-party and legacy CSS

Place third-party CSS in a low-priority layer and isolate legacy selectors behind a wrapper or layer. Do not edit vendor files to win a local specificity battle.

```css
@layer vendor, reset, base, components, utilities;

@import url('date-picker.css') layer(vendor);

@layer components {
  .booking .date-picker {
    --date-picker-accent: var(--color-accent);
  }
}
```

If the vendor stylesheet uses `!important`, create a deliberate override boundary and record why it exists. Future maintainers need to know whether a rule is a temporary migration, a security constraint, or a true product requirement.

### A complete component architecture

```css
@layer reset, tokens, base, components, utilities;

@layer tokens {
  :root {
    --color-accent: #1d4ed8;
    --color-ink: #172033;
    --color-surface: #ffffff;
    --space-3: .75rem;
    --space-4: 1rem;
  }
}

@layer components {
  .notice {
    --notice-accent: var(--color-accent);
    display: grid;
    grid-template-columns: auto minmax(0, 1fr) auto;
    align-items: start;
    gap: var(--space-3);
    padding: var(--space-4);
    border-inline-start: .35rem solid var(--notice-accent);
    color: var(--color-ink);
    background: var(--color-surface);
  }

  .notice[data-tone='success'] {
    --notice-accent: #087443;
  }
}

@layer utilities {
  .u-hidden-visually {
    position: absolute;
    inline-size: 1px;
    block-size: 1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
  }
}
```

The component owns its layout and public accent token. The theme owns global colors. The utility owns one narrow behavior. The layer order explains which category wins without requiring a selector-length contest.

### Debugging architecture problems

When a CSS override feels difficult, ask these questions in order:

1. Which component or layer owns the declaration?
2. Is the value a global token, component token, or one-off exception?
3. Is the selector more specific than it needs to be?
4. Is an unlayered rule competing with layered CSS?
5. Is a custom property missing, inherited unexpectedly, or invalid when consumed?
6. Is the problem really layout, or is it a token, cascade, or state problem?
7. Can a test fixture demonstrate the intended contract without the whole application?

Temporary diagnostics can expose token values and boundaries:

```css
/* Development-only diagnostic layer. */
@layer diagnostics {
  [data-debug-boundary] {
    outline: 2px dashed #a16207;
  }

  [data-debug-token]::after {
    content: attr(data-debug-token);
    display: block;
    padding: .25rem .5rem;
    font: 0.75rem/1 monospace;
    color: white;
    background: #14213d;
  }
}
```

Remove diagnostics before shipping. An architecture is successful when a new contributor can locate the owning rule and understand the intended override path without relying on accidental source order.

### Architecture checklist

- Define layer order before component rules.
- Keep tokens semantic: `--color-danger`, not `--red-500` at every call site.
- Give components a small, documented custom-property API.
- Provide fallbacks when tokens or modern registration are unavailable.
- Keep selectors short and specificity low.
- Use `@scope`, Shadow DOM, CSS Modules, or naming conventions deliberately.
- Put third-party CSS in an early layer.
- Test themes, forced colors, zoom, and component isolation.
- Treat `!important` as an explicit boundary, not a default repair.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- MDN CSS custom properties: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_and_inheritance/Using_CSS_custom_properties
- MDN `@property`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property
- MDN CSS cascade layers: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction
- MDN `@scope`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
