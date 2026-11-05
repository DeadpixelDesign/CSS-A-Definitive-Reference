# The CSS mental model

CSS answers three questions: which nodes are selected, which declarations win, and how the resulting values participate in layout and painting. A useful debugging order is selector -> cascade -> computed value -> box model -> layout -> paint -> interaction.

### Rule anatomy

```css
/* selector */
.card {
  /* property: value; */
  padding: 1rem;
  color: var(--ink, #172033);
}
```

The selector chooses a set of elements. A declaration assigns a value. A shorthand expands into longhands. A custom property stores a token, but it is not validated until consumed by a real property. The computed value is the result after inheritance and substitution; the used value is what layout actually consumes.

### The cascade, in practice

When two declarations compete, reason from the outside in: origin and importance, cascade layer, specificity, scoping proximity where applicable, and source order. Prefer changing the layer or component contract over adding `!important`. Keep utility layers intentionally late, and keep third-party CSS in an early layer.

```css
@layer reset, vendor, base, components, utilities;
@layer vendor { /* imported library CSS */ }
@layer components {
  .button { color: var(--button-ink); }
}
```

### Values and units

Use `rem` for scalable type and spacing, `em` when a component should scale from its own font size, `%` for relationship to a containing block, `ch` for readable text measure, and `dvh`/`svh`/`lvh` with care on mobile. `clamp()` is often the right way to express a bounded fluid value.

```css
h1 { font-size: clamp(2rem, 1.2rem + 3vw, 4.5rem); }
```

### Selectors and scope

Prefer semantic classes and low-specificity selectors. Use `:where()` to deliberately contribute zero specificity, `:is()` to share selector logic, and `:has()` when the relationship is part of the component contract. Avoid selectors whose meaning depends on DOM depth that a component consumer cannot control.

### Inheritance and initial values

Text properties commonly inherit; box-model properties generally do not. When a component boundary matters, reset intentionally with `inherit`, `initial`, `unset`, `revert`, or `revert-layer`. `revert-layer` is particularly useful when a component should step back to the previous cascade layer rather than to the user-agent default.

### Selector matching is a relationship

A selector is not a command to style one element; it describes a set of elements that match a relationship. A class selector can match many nodes, a child combinator describes ownership, and a pseudo-class describes state or structure. Start debugging by asking which elements match before asking why a declaration did not win.

```css
/* Every card gets the base contract. */
.card {
  padding: 1rem;
  border: 1px solid var(--line);
}

/* Only cards containing an invalid field get the error treatment. */
.card:has(input:invalid) {
  border-color: crimson;
}

/* A low-specificity variant remains easy to override. */
:where(.card[data-tone='quiet']) {
  background: var(--soft);
}
```

Keep selectors close to the component contract. A selector that depends on five ancestor elements may work today but becomes fragile when markup changes, a component is reused, or a consumer adds a wrapper.

### Specificity is a budget

Specificity is an ordering signal, not a measure of importance. IDs, classes, attributes, pseudo-classes, elements, and pseudo-elements contribute different weights. Prefer low-specificity selectors and use cascade layers to establish ownership before reaching for `!important`.

```css
@layer reset, components, utilities;

@layer components {
  .button { color: var(--ink); }
  .button.button-danger { color: crimson; }
}

@layer utilities {
  .text-muted { color: var(--muted); }
}
```

Because the utility layer comes later, `.text-muted` can intentionally override a component declaration without becoming a specificity contest. This is easier to maintain than selectors such as `main .toolbar nav a.button span`.

### The value lifecycle

Authored values move through several stages. The declaration is parsed, variables are substituted, inheritance is applied, and the property produces a computed value. Layout then resolves percentages and intrinsic sizes into used values; painting and the device determine the actual result. DevTools often exposes these stages separately, which is why an authored value can differ from a computed value.

```css
:root {
  --space: 1rem;
}

.panel {
  inline-size: calc(100% - 2 * var(--space));
  padding: var(--space);
  color: var(--ink, #172033);
}
```

If `--space` is missing, the `calc()` declaration becomes invalid unless it has a fallback. If `--ink` is missing, the fallback color is used. Custom properties preserve tokens as text until a real property consumes them, so validation happens later than many newcomers expect.

### Custom properties are contracts

Custom properties inherit by default. Treat them as a component API: define a name, document its type and fallback, and expose only the tokens a consumer should change. `@property` can add a syntax, inheritance behavior, and initial value when the contract needs stronger guarantees.

```css
@property --card-accent {
  syntax: '<color>';
  inherits: false;
  initial-value: #1d4ed8;
}

.card {
  --card-accent: #0f766e;
  border-inline-start: .35rem solid var(--card-accent);
}
```

Do not use a custom property as an excuse to hide every design decision behind an override. A small token surface makes a component adaptable without making its internal layout unknowable.

### Layout, paint, and interaction are different questions

When a visual result is wrong, separate the stages. Layout determines size and position. Paint determines backgrounds, borders, shadows, and text appearance. Compositing determines how layers combine. Interaction determines hit testing, focus, selection, and pointer behavior. A `z-index` change cannot fix a wrong grid track, and `pointer-events` cannot fix a missing focus style.

```css
.tooltip {
  position: absolute;
  inset-block-start: anchor(bottom);
  inset-inline-start: anchor(center);
  translate: -50% .5rem;
  opacity: 0;
  pointer-events: none;
}

.trigger:hover + .tooltip,
.trigger:focus-visible + .tooltip {
  opacity: 1;
}
```

This example has a layout concern (anchoring), a paint concern (opacity), and an interaction concern (whether the tooltip can receive pointer events). Debug each concern separately and preserve an accessible name or description in the HTML.

### Scoping and component boundaries

Modern CSS provides more ways to keep styles local. A component can use a naming convention, a wrapper, `@scope`, or a framework’s style boundary. The goal is not isolation at any cost; the goal is predictable ownership and a clear escape hatch for themes and states.

```css
@scope (.profile-card) {
  :scope {
    container-type: inline-size;
  }

  .title {
    margin-block: 0;
  }

  @container (min-width: 32rem) {
    .content {
      display: grid;
      grid-template-columns: 8rem 1fr;
    }
  }
}
```

Use a boundary when it makes ownership clearer, but keep the component usable when the boundary is not supported. A fallback class-based selector should remain understandable to the next person debugging the stylesheet.

### A repeatable debugging workflow

When a rule appears not to work, follow a fixed sequence:

1. **Match:** confirm the intended element is selected.
2. **Parse:** check that the declaration and value grammar are valid.
3. **Cascade:** inspect overridden declarations, specificity, layers, and source order.
4. **Compute:** inspect variables, inheritance, and the computed value.
5. **Layout:** check the containing block, formatting context, intrinsic minimums, and available space.
6. **Paint:** inspect stacking contexts, clipping, opacity, filters, and transforms.
7. **Interact:** test focus, pointer events, hit targets, selection, and reduced motion.

```css
/* Temporary diagnostic stylesheet. Remove after isolating the issue. */
* { outline: 1px solid rgb(255 0 0 / .12); }
[data-debug='layout'] { outline: 2px solid #1d4ed8; }
[data-debug='overflow'] { overflow: visible !important; }
```

The diagnostic style should answer one question at a time. Avoid fixing a cascade problem by adding random `!important` declarations; that removes evidence and makes the next bug harder to explain.

### Compatibility and source trail

Consult the current standards, authoring guidance, browser documentation, and testing tools before shipping. Accessibility advice changes as standards, browser behavior, and assistive technologies evolve; this chapter is a teaching reference, not a frozen guarantee.

#### Standards and normative guidance

- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — the W3C Recommendation that defines testable accessibility success criteria.
- [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) — explanations, intent, benefits, and sufficient techniques for WCAG criteria.
- [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) — roles, states, and properties for communicating custom interface semantics.
- [ARIA in HTML](https://www.w3.org/TR/html-aria/) — rules for using ARIA with HTML elements and when native semantics take precedence.

#### Authoring patterns and accessibility education

- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — interaction patterns and keyboard behavior for dialogs, tabs, menus, accordions, and other widgets.
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) — practical guidance for semantic HTML, CSS, JavaScript, forms, and assistive technology.
- [MDN CSS accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Accessibility) — CSS-specific considerations for contrast, motion, focus, layout, and user preferences.
- [web.dev Accessibility](https://web.dev/accessibility/) — guidance and learning resources for building accessible web experiences.
- [web.dev Learn Accessibility](https://web.dev/learn/accessibility/) — structured lessons covering semantics, focus, forms, color, responsive design, and testing.

#### Automated testing and quality tools

- [axe-core](https://github.com/dequelabs/axe-core) — an automated accessibility engine that can run in browser tests and development tooling.
- [Deque axe DevTools](https://www.deque.com/axe/devtools/) — browser and enterprise tooling built around axe accessibility checks.
- [Lighthouse accessibility audits](https://developer.chrome.com/docs/lighthouse/accessibility/) — automated checks integrated into Chrome DevTools and related workflows.
- [Accessibility Insights](https://accessibilityinsights.io/) — guided assessments and automated checks for web accessibility.
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) — a focused tool for evaluating foreground and background contrast.

Automated tools find only some classes of problems. Pair them with keyboard testing, zoom and reflow checks, forced-colors and reduced-motion checks, screen-reader testing, and task-based testing with people who use assistive technologies.
