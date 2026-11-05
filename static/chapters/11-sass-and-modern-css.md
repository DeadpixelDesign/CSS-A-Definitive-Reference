# Sass and modern CSS

Sass is a stylesheet language compiled to CSS. Its strongest advantages are build-time organization, mixins, functions, maps, loops, and module boundaries. Native CSS now provides custom properties, nesting, layers, container queries, color functions, and increasingly powerful value composition.

Sass is best understood as a compile-time language that produces CSS. CSS is the browser's runtime language. They overlap, but they solve different problems: Sass can generate files, calculate values, organize modules, and emit repeated rules before delivery; CSS can participate in the cascade, respond to the viewport and container, inherit values, react to user preferences, and change at runtime.

The practical question is not “Sass or CSS?” It is “which responsibilities belong at build time, and which must remain live in the browser?”

### The central comparison

| Question | Sass | Native CSS |
|---|---|---|
| When does it run? | During the build | In the browser while styles are parsed and applied |
| Can a user change the value at runtime? | Not without generating new CSS | Yes, with custom properties, inheritance, media queries, and scripts |
| Can it loop and generate selectors? | Yes | Not as a general-purpose language |
| Can it respond to a container's size? | No, not by itself | Yes, with container queries |
| Can it create a reusable declaration bundle? | Yes, with mixins | Partly, with custom properties and components |
| Is it required for modern CSS? | No | CSS is the delivery format either way |

Use Sass for compile-time concerns and native CSS for behavior that must remain live. This distinction prevents a common mistake: generating a large number of static selectors when a small set of custom properties would let the browser handle themes, state, and responsive values directly.

| Sass feature | Native CSS complement | Keep Sass when |
|---|---|---|
| `$variables` | Custom properties and `var()` | The value is compile-time or part of a library build API |
| Nesting | Native CSS nesting | You need selector generation or legacy output |
| Mixins | Components, utilities, custom properties | You need parameterized declaration bundles |
| Functions | `calc()`, `min()`, `max()`, `clamp()`, color functions | You need domain-specific build-time computation |
| Modules | Cascade layers plus build tooling | You need compile-time encapsulation and distribution |

Prefer `@use` and `@forward` over legacy Sass `@import`. Move theme values to custom properties when runtime theme switching or user customization is useful.

### Sass variables versus CSS custom properties

Sass variables are replaced during compilation. They are excellent for constants that should never change in the browser. CSS custom properties survive compilation and participate in the cascade, which makes them better for themes, component configuration, user preferences, and values that JavaScript may update.

```scss
// Sass: compile-time value.
$space-3: 0.75rem;

.card {
  padding: $space-3;
}
```

```css
/* CSS: runtime value with a fallback. */
:root { --space-3: 0.75rem; }
.card { padding: var(--space-3, 0.75rem); }
```

Use both when their responsibilities are different. A Sass map can generate a spacing scale, while custom properties can expose the resulting scale to a consuming application.

```scss
$space: (1: .25rem, 2: .5rem, 3: .75rem, 4: 1rem);

:root {
  @each $step, $value in $space {
    --space-#{$step}: #{$value};
  }
}
```

```css
.stack { display: grid; gap: var(--space-3); }
```

### Nesting: Sass and native CSS

Both languages can express selector relationships. Native CSS nesting is delivered to the browser and participates in the normal cascade, while Sass nesting is expanded during compilation.

```scss
// Sass
.card {
  padding: 1rem;
  &__title { margin: 0; }
  &:hover { box-shadow: 0 1rem 2rem rgb(15 23 42 / .12); }
}
```

```css
/* Native CSS nesting */
.card {
  padding: 1rem;
  & .card__title { margin: 0; }
  &:hover { box-shadow: 0 1rem 2rem rgb(15 23 42 / .12); }
}
```

Keep nesting shallow in either language. Deep nesting increases specificity and makes overrides harder to predict.

### Mixins versus custom properties

Sass mixins are parameterized code generation. They are useful when a pattern needs conditions, loops, multiple declarations, or compile-time arguments. Custom properties are better when the component should accept a value at runtime.

```scss
@mixin focus-ring($color: #1d4ed8) {
  outline: 3px solid $color;
  outline-offset: 3px;
}

.button:focus-visible { @include focus-ring(#0f766e); }
```

```css
.button {
  --focus-color: #1d4ed8;
}

.button:focus-visible {
  outline: 3px solid var(--focus-color);
  outline-offset: 3px;
}

.button--danger { --focus-color: #b42318; }
```

The mixin emits a fixed result. The custom property lets the component or its parent change the value without recompiling.

### Functions and runtime calculations

Sass functions calculate known values before delivery. Native CSS functions calculate values in the browser and can combine relative units, custom properties, viewport values, and container values.

```scss
$content-max: 72rem;
$gutter: 1.5rem;

.layout { width: min($content-max, calc(100% - ($gutter * 2))); }
```

```css
.layout {
  inline-size: min(72rem, calc(100% - 3rem));
  margin-inline: auto;
  padding-inline: clamp(1rem, 4vw, 3rem);
}
```

Use Sass math when the result is a fixed design token. Use `calc()`, `min()`, `max()`, and `clamp()` when the browser must combine values at runtime.

### Maps, loops, and finite output

Sass maps and loops remain useful when they generate a deliberately finite set of utilities, sizes, or themes. They should not be used to generate thousands of selectors that could be represented by a few custom properties.

```scss
$sizes: (
  sm: (padding: .5rem .75rem, font-size: .875rem),
  md: (padding: .7rem 1rem, font-size: 1rem),
  lg: (padding: .9rem 1.25rem, font-size: 1.125rem)
);

@use "sass:map";

@each $name, $values in $sizes {
  .button--#{$name} {
    padding: map.get($values, padding);
    font-size: map.get($values, font-size);
  }
}
```

The output is predictable: three classes, not an unbounded runtime system. If consumers need arbitrary values, use custom properties instead.

### Modules with `@use` and `@forward`

Use Sass modules to control what a package exposes. `@use` loads a module with a namespace; `@forward` creates a public entry point for consumers.

```scss
// _tokens.scss
$brand: #1d4ed8;
$radius: .75rem;

// _index.scss
@forward "tokens";

// app.scss
@use "index" as design;

.button {
  background: design.$brand;
  border-radius: design.$radius;
}
```

Namespaces make dependencies visible at the point of use. They also avoid the accidental global variables associated with older `@import`-based architectures.

### Cascade layers and Sass modules solve different problems

`@layer` controls cascade order in the browser. Sass modules control source organization and compile-time visibility. They complement each other.

```scss
@use "reset";
@use "tokens";

@layer reset, base, components, utilities;

@layer base {
  :root { --ink: #172033; }
}

@layer components {
  .card { color: var(--ink); }
}
```

Use layers to make precedence explicit. Use modules to define build boundaries and prevent accidental globals.

### A complete hybrid component

This example uses Sass for a finite component-size API and native CSS for runtime theming, responsive sizing, and interaction states.

```scss
// button.scss
.button {
  --button-bg: #1d4ed8;
  --button-ink: #fff;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  border: 0;
  border-radius: .6rem;
  background: var(--button-bg);
  color: var(--button-ink);
  font: inherit;
  cursor: pointer;

  &:hover { filter: brightness(1.08); }
  &:active { transform: translateY(1px); }
  &:focus-visible { outline: 3px solid #0f766e; outline-offset: 3px; }
}

.button--sm { padding: .5rem .75rem; font-size: .875rem; }
.button--md { padding: .7rem 1rem; font-size: 1rem; }
.button--lg { padding: .9rem 1.25rem; font-size: 1.125rem; }

@media (prefers-reduced-motion: reduce) {
  .button { transition: none; }
}
```

```html
<button class="button button--md" type="button">Save changes</button>
<button class="button button--md" style="--button-bg: #0f766e" type="button">Publish</button>
```

Sass or a preprocessor can generate the finite size classes. Native CSS keeps the color configurable per instance and responds to user motion preferences.

### A practical migration pattern

Migration does not need to be a rewrite:

1. Keep Sass as the compiler and add native CSS inside existing components.
2. Convert theme values from Sass variables to custom properties where runtime changes matter.
3. Replace simple Sass nesting with native nesting only after checking target browsers.
4. Keep Sass maps, loops, and functions that generate useful finite output.
5. Replace mixins that only assign theme values with custom properties.
6. Retain Sass modules for package organization while moving cascade control to CSS layers.
7. Remove an abstraction only after reviewing the generated CSS and testing the browser targets.

### When Sass remains the better tool

Keep Sass when it provides a measurable benefit: generating a finite family of utilities, building a distributable component library with a stable module API, creating mixins that emit coordinated declarations and fallbacks, calculating fixed build-time values, or organizing a large source tree.

Avoid Sass when it merely hides a value that should be themeable, duplicates a browser capability, or creates a long chain of generated selectors that is harder to debug than straightforward CSS.

### Sass and CSS review checklist

1. Does this value need to change after compilation?
2. Does it depend on viewport, container, user preference, or component state?
3. Would a custom property make the component easier to theme?
4. Is the generated CSS smaller and clearer than the source it replaces?
5. Does the abstraction increase specificity or hide the cascade?
6. Is the module public, private, or a local implementation detail?
7. Can the behavior be tested in the final CSS, not only in the Sass source?
8. Is a native CSS function or at-rule now a better fit?

The goal is not to eliminate Sass. It is to reserve compile-time power for compile-time problems while allowing the browser to handle runtime behavior.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
