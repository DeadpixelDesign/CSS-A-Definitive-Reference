# Appendix G: A11y field guide

The current practical alternative is not always another giant reset file. Modern browsers agree on most of the old cross-browser inconsistencies, so many teams use a small, project-owned baseline inside a cascade layer, then add only the defaults their design system actually needs. This approach is sometimes called a sensible reset, a remedy, or a minimal baseline.

The choice depends on the project:

| Approach | What it does | Best fit |
| --- | --- | --- |
| Minimal project-owned baseline | Changes only box sizing, typography inheritance, media defaults, and known application needs | Most custom applications and design systems |
| `normalize.css` | Preserves useful browser defaults while correcting documented inconsistencies | Broad cross-browser foundations and older target ranges |
| `sanitize.css` | Normalizes and adds opinionated sensible defaults | Teams that want a maintained foundation with more styling decisions |
| `modern-normalize` | Smaller normalization aimed at current Chrome, Firefox, and Safari behavior | Projects targeting evergreen browsers |
| Framework preflight | A framework-specific baseline, such as Tailwind Preflight or Bootstrap Reboot | Projects already committed to that framework |
| No global reset | Keeps user-agent defaults and styles components locally | Content-first pages, prototypes, and systems that value native defaults |

There is no universal “best” reset. The important decision is to choose one baseline, understand what it changes, and avoid stacking multiple resets that fight over the same elements.

### Recommended default: a layered, minimal baseline

For a new application, start with a small reset in a named layer. This keeps the baseline easy to inspect and prevents it from becoming an unowned collection of global overrides.

```css
@layer reset, base, components, utilities;

@layer reset {
  *,
  *::before,
  *::after {
    box-sizing: border-box;
  }

  html {
    text-size-adjust: 100%;
  }

  body {
    min-block-size: 100vh;
    margin: 0;
    line-height: 1.5;
    text-rendering: optimizeLegibility;
  }

  :where(h1, h2, h3, h4, p, figure, blockquote, dl, dd) {
    margin-block: 0;
  }

  :where(ul, ol)[role='list'] {
    padding: 0;
    list-style: none;
  }

  :where(img, picture, video, canvas, svg) {
    display: block;
    max-inline-size: 100%;
  }

  :where(input, button, textarea, select) {
    font: inherit;
  }

  :where(button, input, textarea, select) {
    color: inherit;
  }

  :where(textarea) {
    resize: vertical;
  }

  :where(button, label, select, summary) {
    cursor: pointer;
  }

  :where(button:disabled, input:disabled, select:disabled, textarea:disabled) {
    cursor: not-allowed;
  }
}
```

This baseline intentionally does not erase every browser default. Headings, lists, tables, buttons, and form controls still receive meaningful component or base styles instead of becoming blank boxes that every page must rebuild.

### Why use a cascade layer?

A reset is foundational CSS, so it should have a predictable relationship to the rest of the stylesheet. A reset layer can establish box sizing and baseline behavior while allowing components and utilities to override it normally.

```css
@layer reset, base, components, utilities;

@layer reset {
  [hidden] {
    display: none !important;
  }
}

@layer components {
  .dialog[open] {
    display: grid;
  }
}
```

The `[hidden]` rule is an example of a true boundary: an author component should not accidentally make a hidden element visible. Keep such exceptions rare and document them.

### Do not remove useful semantics

Older resets often removed all margins, list markers, outlines, button appearance, and form-control styling globally. Those declarations can save a designer from unexpected defaults, but they also remove useful affordances. A modern baseline should be selective.

```css
/* Risky as a global rule: it removes a valuable keyboard signal. */
/* *:focus { outline: none; } */

/* Better: keep a visible, branded focus indicator. */
:where(:focus-visible) {
  outline: 3px solid var(--color-accent, #1d4ed8);
  outline-offset: 3px;
}
```

Do not globally set `appearance: none` on every control. Do not remove list markers from every list when some lists are content. Do not make every image `user-select: none` unless the product has a specific interaction reason.

### Keep semantic lists semantic

Navigation lists and application menus often need visual list styles removed, but article lists and ordered procedures may need their markers. Scope the reset to the role or component that owns the visual treatment.

```css
/* Good: only presentation lists lose their markers. */
:where(ul, ol)[role='list'],
.nav-list,
.tag-list {
  padding: 0;
  list-style: none;
}

/* Keep this semantic list styled. */
.instructions {
  padding-inline-start: 1.5rem;
  list-style: decimal;
}
```

### Normalize instead of reset

If the project needs a cross-browser foundation that preserves useful defaults, use a maintained normalization package rather than combining several ad hoc snippets. [normalize.css](https://csstools.github.io/normalize.css/) is the conservative option: it targets browser inconsistencies while trying to keep elements recognizable. The current package documentation lists installation through `@csstools/normalize.css`.

```css
@import url('@csstools/normalize.css');

@layer base {
  /* Project-specific rules follow the normalization layer. */
  body {
    font-family: var(--font-reading);
  }
}
```

Treat normalization as a foundation, not a design system. You still need to define type, spacing, focus, form, and component behavior for the product.

### `sanitize.css`

[`sanitize.css`](https://csstools.github.io/sanitize.css/) is a more opinionated foundation that combines normalization with sensible defaults. It can be a good fit when a team wants a curated baseline across a broad set of elements.

```js
// JavaScript or TypeScript entry point
import 'sanitize.css';
```

Audit the package against the project’s accessibility requirements. A “sensible” default for one interface can be an unwanted global opinion for another, especially around form controls, media, typography, or print.

### `modern-normalize`

[`modern-normalize`](https://www.npmjs.com/package/modern-normalize) is a smaller normalization package aimed at current Chrome, Firefox, and Safari behavior. It can be appropriate for an evergreen-browser application that wants a compact starting point rather than broad legacy coverage.

```js
import 'modern-normalize/modern-normalize.css';
```

Check the package’s current target and maintenance status before adopting it. A smaller package is not automatically a better fit if the application must support browsers outside its documented scope.

### Framework preflights and reboots

Frameworks often include their own baseline. Tailwind’s Preflight, Bootstrap Reboot, and UnoCSS reset presets are examples of framework-coupled approaches. Use the framework’s baseline when the framework owns the rest of the styling model; avoid adding another global reset on top without comparing the output.

```css
/* Example: keep a framework baseline in its own layer. */
@import 'tailwindcss' layer(framework);
@layer framework, reset, base, components, utilities;
```

The exact import and layer behavior depends on the framework version. Read the current framework documentation and inspect the generated CSS rather than assuming that two reset layers compose safely.

### Component-local baselines

A design system can avoid a heavy global reset by making each component locally complete. This is especially useful for web components, embedded widgets, and applications that must coexist with host-page CSS.

```css
.date-picker {
  box-sizing: border-box;
  font: 1rem/1.4 system-ui, sans-serif;
}

.date-picker,
.date-picker::before,
.date-picker::after {
  box-sizing: inherit;
}

.date-picker button {
  font: inherit;
  color: inherit;
}
```

Component-local baselines reduce global side effects, but they require discipline. Put shared rules in a reusable layer or component primitive instead of copying a different mini-reset into every component.

### A reset decision workflow

1. List the browsers, embedded contexts, and rendering modes the product supports.
2. Decide whether user-agent defaults are useful for the content.
3. Choose one approach: minimal baseline, normalization package, sanitize-style foundation, framework preflight, or no reset.
4. Put the choice in a named layer and record it in the project documentation.
5. Test headings, lists, tables, forms, focus, media, `dialog`, print, forced colors, zoom, and reduced motion.
6. Remove rules that do not solve a demonstrated problem.
7. Recheck the baseline when changing browser targets or major framework versions.

### What this book uses

This book’s web edition uses a small project-owned baseline rather than importing a full reset package. It sets predictable box sizing, readable typography, media behavior, form inheritance, focus treatment, and responsive defaults in the application stylesheet. That approach keeps the visual contract close to the components and avoids silently changing native semantics across every element.

### Appendix source trail

- normalize.css: https://csstools.github.io/normalize.css/
- sanitize.css: https://csstools.github.io/sanitize.css/
- modern-normalize: https://www.npmjs.com/package/modern-normalize
- Andy Bell, “A Modern CSS Reset”: https://bell.bz/a-modern-css-reset/
- UnoCSS reset presets: https://unocss.dev/guide/style-reset
- MDN CSS cascade layers: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction
- web.dev Learn CSS: https://web.dev/learn/css
