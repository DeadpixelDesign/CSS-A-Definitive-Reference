# The box model and formatting contexts

Every element participates in a formatting context. The classic box consists of content, padding, border, and margin. `box-sizing: border-box` makes declared dimensions include padding and border, which makes component sizing easier to reason about.

### Normal flow first

Normal flow is not a primitive to escape as quickly as possible; it is the most resilient layout mode. Use block flow for vertical composition, inline flow for text, and modern layout systems for groups. Reach for absolute positioning for overlays and anchored details, not for the primary page skeleton.

```html
<article class="story">
  <h2>Normal flow</h2>
  <p>Block boxes stack vertically, while inline content flows inside a line box.</p>
  <a href="/learn">Continue reading</a>
</article>
```

```css
.story {
  display: flow-root;
  max-inline-size: 42rem;
  margin-inline: auto;
  padding: 1.5rem;
}

.story h2,
.story p {
  margin-block: 0 1rem;
}
```

The box model is easiest to see when each part has a deliberate value. `box-sizing: border-box` makes the declared inline and block sizes include padding and borders, which is usually the least surprising component contract.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

.panel {
  inline-size: 20rem;
  min-block-size: 8rem;
  padding: 1rem 1.25rem;
  border: 2px solid currentColor;
  margin-block: 1rem;
  border-radius: .75rem;
}
```

Use logical properties when the component should work in different writing modes. The physical equivalents are `width`, `height`, `margin-left`, and `padding-right`; the logical forms describe the component’s intent instead.

```css
.notice {
  inline-size: min(100%, 40rem);
  block-size: auto;
  padding-block: 1rem;
  padding-inline: 1.25rem;
  margin-inline: auto;
  border-inline-start: .35rem solid rebeccapurple;
}
```

### Intrinsic sizing

Intrinsic keywords—`min-content`, `max-content`, `fit-content()`—let content participate in sizing. The most common production bug is a flex or grid child that refuses to shrink because its automatic minimum size is larger than expected. `min-width: 0` or `min-inline-size: 0` can make the intended constraint explicit.

```css
.tag-list {
  display: grid;
  grid-template-columns: minmax(min-content, 12rem) fit-content(20rem);
  inline-size: min(100%, 42rem);
  gap: .75rem;
}

.tag-list__label {
  inline-size: max-content;
  max-inline-size: 100%;
  overflow-wrap: anywhere;
}

.tag-list__value {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

For a component that should grow between a floor and a ceiling, combine `min()`, `max()`, or `clamp()` with an intrinsic or relative size.

```css
.reading-column {
  inline-size: min(100% - 2rem, 72ch);
  padding-inline: clamp(1rem, 4vw, 3rem);
}
```

### Overflow and containment

Overflow is a product decision. `overflow: clip` prevents scrolling; `overflow: auto` provides a scroll container; `overflow: hidden` may hide focus rings or content unexpectedly. `contain` and `content-visibility` can improve performance, but they alter layout, painting, or size containment and must be tested with focus, find-in-page, printing, and assistive technology.

```css
.code-preview {
  max-inline-size: 100%;
  overflow: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
}

.thumbnail-frame {
  aspect-ratio: 16 / 9;
  overflow: clip;
  contain: paint;
}

.thumbnail-frame img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

.feed-item {
  content-visibility: auto;
  contain-intrinsic-size: auto 18rem;
}
```

Prefer `clip` when content must not become a scroll container. Use `auto` when the user needs to reach content that does not fit, and preserve keyboard focus visibility when choosing any clipping strategy.

### Stacking contexts

`z-index` only competes inside a stacking context. Transforms, opacity, filters, positioned elements with a z-index, and isolation can create new contexts. Debug stacking by drawing the context tree, not by increasing numbers indefinitely.

```css
.app-shell {
  isolation: isolate;
}

.app-shell__content {
  position: relative;
  z-index: 0;
}

.app-shell__scrim {
  position: fixed;
  inset: 0;
  z-index: 10;
  background: rgb(0 0 0 / .45);
}

.app-shell__dialog {
  position: fixed;
  inset: 50% auto auto 50%;
  z-index: 20;
  translate: -50% -50%;
  max-inline-size: min(90vw, 34rem);
}
```

Create the stacking context deliberately with `isolation: isolate`, then keep a small, documented scale for layers. A high `z-index` cannot escape an ancestor stacking context.

### Compatibility and source trail

Consult the current standards, authoring guidance, browser documentation, and testing tools before shipping. Accessibility advice changes as standards, browser behavior, and assistive technologies evolve; this chapter is a teaching reference, not a frozen guarantee.

#### Standards and normative guidance

- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — testable accessibility success criteria.
- [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) — explanations, intent, benefits, and techniques.
- [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) — roles, states, and properties for custom interface semantics.
- [ARIA in HTML](https://www.w3.org/TR/html-aria/) — rules for using ARIA with HTML and when native semantics take precedence.

#### Authoring patterns and accessibility education

- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — keyboard behavior and patterns for dialogs, tabs, menus, and accordions.
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) — practical guidance for semantic HTML, CSS, JavaScript, forms, and assistive technology.
- [MDN CSS accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Accessibility) — CSS guidance for contrast, motion, focus, layout, and user preferences.
- [web.dev Accessibility](https://web.dev/accessibility/) — guidance and learning resources for accessible web experiences.
- [web.dev Learn Accessibility](https://web.dev/learn/accessibility/) — structured lessons covering semantics, focus, forms, color, responsive design, and testing.

#### Automated testing and quality tools

- [axe-core](https://github.com/dequelabs/axe-core) — automated accessibility testing for browsers and test suites.
- [Deque axe DevTools](https://www.deque.com/axe/devtools/) — browser and enterprise tooling built around axe checks.
- [Lighthouse accessibility audits](https://developer.chrome.com/docs/lighthouse/accessibility/) — automated audits integrated into Chrome tooling.
- [Accessibility Insights](https://accessibilityinsights.io/) — guided assessments and automated checks.
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) — focused foreground/background contrast checking.

Automated tools find only some classes of problems. Pair them with keyboard testing, zoom and reflow checks, forced-colors and reduced-motion checks, screen-reader testing, and task-based testing with people who use assistive technologies.
