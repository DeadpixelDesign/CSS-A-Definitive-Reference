# Accessibility and quality

CSS quality is user quality. Test zoom, keyboard navigation, forced colors, reduced motion, contrast, print, touch, and content extremes.

### Accessibility checklist

- Never remove focus indication without providing a stronger replacement.
- Do not use color as the only signal.
- Keep text zoomable and avoid clipping essential content.
- Test at 200% zoom and with long translated strings.
- Respect `prefers-reduced-motion`, `prefers-contrast`, and `forced-colors`.
- Avoid generated content for essential instructions.
- Preserve native semantics and interaction whenever possible.

Accessibility is not a final polish pass. It is a set of constraints that shape HTML semantics, CSS layout, interaction states, content order, motion, contrast, and testing. CSS can improve access, but it can also hide content, destroy reading order, remove focus, create motion sickness, or make a control unusable at high zoom.

### The accessibility contract

For every component, define these five parts before styling it:

1. **Name:** what the control or region is called by assistive technology.
2. **Role:** what it does: link, button, dialog, navigation, status, tab, and so on.
3. **State:** whether it is expanded, selected, checked, disabled, invalid, busy, or hidden.
4. **Value:** the information a user can read or change.
5. **Response:** what happens after keyboard, pointer, touch, voice, or assistive-technology input.

If the HTML element already provides that contract, prefer it. A native button is usually a better starting point than a styled `div` with a click handler. A native `<details>` often provides a better disclosure than a custom accordion with incomplete keyboard behavior.

### Source order, visual order, and reading order

CSS can make elements appear in a different order from the document. Use visual reordering only when the source order remains understandable for keyboard and assistive-technology users.

```html
<article class="product">
  <h2>Keyboard</h2>
  <p class="product__price">$99</p>
  <p class="product__description">A compact mechanical keyboard.</p>
  <a class="product__action" href="/keyboard">View keyboard</a>
</article>
```

```css
.product { display: grid; gap: .75rem; }
.product__price { grid-row: 2; }
.product__description { grid-row: 3; }
.product__action { grid-row: 4; }
```

Do not use `order`, grid placement, or transforms to create a different reading sequence for a form, checkout, article, or navigation system. If sequence matters, fix the HTML order first.

### Focus visibility and focus management

Every keyboard-operable element needs a visible focus indicator. `:focus-visible` lets pointer users avoid an unnecessary ring while preserving a strong indicator for keyboard navigation.

```css
:where(a, button, input, select, textarea, summary):focus-visible {
  outline: 3px solid var(--focus, #1d4ed8);
  outline-offset: 3px;
}

:where(a, button, input, select, textarea, summary):focus:not(:focus-visible) {
  outline: none;
}
```

When opening a dialog, move focus into the dialog. When closing it, return focus to the trigger unless the trigger no longer exists. When opening a menu or tab panel, follow the component's expected keyboard model rather than moving focus arbitrarily.

### Contrast is more than text color

Check text, icons, borders that communicate state, placeholder text, focus indicators, disabled-state communication, and text over images. A color token that passes on a white surface may fail on a dark surface or over a gradient.

```css
.error {
  border-inline-start: .25rem solid #b42318;
  background: #fef3f2;
  color: #7a271a;
}

.error::before {
  content: "Error: ";
  font-weight: 700;
}
```

The label and border reinforce the message without depending on red alone. Never put essential meaning only in a pseudo-element; keep the actual message in the DOM.

### Zoom, text scaling, and reflow

Test at 200% browser zoom and with increased text size. Avoid fixed heights around text, `overflow: hidden` on reading content, and layouts that require horizontal scrolling at ordinary content widths.

```css
.article {
  max-inline-size: 70rem;
  padding-inline: clamp(1rem, 4vw, 3rem);
}

.article__body {
  max-inline-size: 70ch;
  overflow-wrap: anywhere;
}

.article img,
.article video {
  max-inline-size: 100%;
  block-size: auto;
}
```

Test long headings, translated strings, user-generated content, large form values, and narrow viewports. A layout that works only with the author’s sample text is not resilient.

### Motion and vestibular safety

Motion should explain a state change, not compete with the task. Respect `prefers-reduced-motion` and avoid animations that flash, zoom, or move the viewport unexpectedly.

```css
.drawer {
  transform: translateX(100%);
  transition: transform .2s ease;
}

.drawer[data-open="true"] { transform: translateX(0); }

@media (prefers-reduced-motion: reduce) {
  .drawer { transition: none; }
}
```

For a reduced-motion mode, preserve the state change while removing the travel. Do not leave content permanently off-screen when animation is disabled.

### Forced colors and high contrast

Forced-colors modes may replace author colors with a system palette. Avoid using background images, subtle shadows, or color-only borders as the only way to communicate state.

```css
.button {
  border: 2px solid transparent;
  background: var(--accent);
  color: white;
}

.button[aria-pressed="true"] { border-color: currentColor; }

@media (forced-colors: active) {
  .button {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

### Forms and error recovery

Associate every control with a visible label. Connect help and error text with `aria-describedby`, preserve the user's input after validation, and place the error where it can be discovered without forcing a pointer-only scan.

```html
<div class="field">
  <label for="postal-code">Postal code</label>
  <input id="postal-code" name="postal-code" inputmode="numeric"
         aria-describedby="postal-help postal-error" aria-invalid="true">
  <small id="postal-help">Use five digits.</small>
  <p id="postal-error" class="error" role="alert">Enter a valid postal code.</p>
</div>
```

Use `aria-invalid="true"` only after validation has identified an error. Do not mark every empty required field invalid before the user has interacted with the form.

### Tables, overflow, and data density

Do not turn a complex data table into a collection of unrelated cards without preserving headers and relationships. For a wide table, allow horizontal scrolling on the table wrapper while keeping the page itself stable.

```css
.table-wrap {
  max-inline-size: 100%;
  overflow-x: auto;
  overscroll-behavior-inline: contain;
}

table { min-inline-size: 42rem; border-collapse: collapse; }
th, td { padding: .75rem; border-block-end: 1px solid var(--border); text-align: start; }
```

Give tables captions, header cells, and appropriate `scope` attributes. A scrollable table is preferable to clipped data.

### Quality beyond accessibility

Accessibility and quality overlap with resilience. Test these dimensions together:

| Dimension | Questions |
|---|---|
| Content | What happens with long, empty, translated, or user-generated content? |
| Layout | Does it work at narrow widths, zoom, print, and writing-mode changes? |
| Input | Can a user complete the task with keyboard, touch, switch, and voice input? |
| Preferences | Does it respect dark mode, reduced motion, forced colors, and contrast settings? |
| Performance | Does it remain usable on slow devices and delayed networks? |
| Compatibility | Is the baseline useful when the enhancement is unavailable? |
| Maintainability | Can another person find the source of the component's state and styles? |

### A practical test sequence

1. Use the page with only a keyboard.
2. Zoom to 200% and increase text size.
3. Turn on dark mode, reduced motion, forced colors, and high contrast where available.
4. Navigate with a screen reader or accessibility tree inspector.
5. Test at a narrow viewport and with long strings.
6. Disable JavaScript and confirm that essential content and navigation remain available.
7. Test touch targets and pointer cancellation on a real device.
8. Print the page and inspect page breaks, focus artifacts, and missing content.
9. Run automated checks, then manually verify the reported issues.

Automated tools are excellent at finding missing labels, invalid contrast combinations, duplicate IDs, and structural issues. They cannot decide whether a custom widget has a sensible interaction model or whether the content order makes sense.

### Performance and rendering quality

Measure before optimizing. Avoid layout thrashing when using CSSOM, reduce expensive filters and large shadows, reserve space for media, and use containment only when it does not hide content from find-in-page, printing, or assistive technology.

```css
.media-card {
  content-visibility: auto;
  contain-intrinsic-size: 0 18rem;
}
```

Use content visibility for long, independent sections after testing find-in-page, focus navigation, and screen-reader behavior in the target browsers. Progressive rendering must not make essential content unreachable.

### Accessibility acceptance criteria

For each component, write acceptance criteria in user terms:

- A keyboard user can reach, operate, and leave every control.
- The focused element is visible and not covered by fixed UI.
- A screen reader user can identify the component, its state, and its result.
- The component remains usable at 200% zoom and with long text.
- Color is not the only signal for status or error.
- Reduced motion removes unnecessary movement without removing the state change.
- The baseline remains useful when CSS enhancement or JavaScript is unavailable.

### Performance checklist

Measure before optimizing. Avoid layout thrashing when using CSSOM, use stable dimensions for media, limit expensive filters, and verify that containment does not hide content from find-in-page, printing, or assistive technology.

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
