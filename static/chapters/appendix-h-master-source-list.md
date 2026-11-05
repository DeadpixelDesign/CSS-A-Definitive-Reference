# Appendix H: Master source list

This appendix is a compact accessibility reference for CSS authors and component developers. “A11y” is a short form of “accessibility”: the first and last letters of the word with the 11 letters between them. The abbreviation is useful, but the work is concrete: preserve semantics, make states perceivable, support multiple input methods, and test with people and tools.

### The four questions for every component

Before reviewing CSS, ask:

1. **Can I find it?** Is the component in a sensible reading and focus order?
2. **Can I understand it?** Does it have a clear name, role, state, value, and result?
3. **Can I operate it?** Can keyboard, touch, voice, switch, and assistive-technology users complete the task?
4. **Can I recover?** Are errors, focus changes, and unavailable enhancements explained and reversible?

### Semantic HTML first

Use the element that already expresses the intended behavior:

| Need | Prefer |
|---|---|
| Navigate somewhere | `<a href>` |
| Perform an action | `<button>` |
| Submit data | `<form>` and `<button type="submit">` |
| Expand content | `<details>` and `<summary>` |
| Modal decision | `<dialog>` |
| Choose one option | Radio group or `<select>` |
| Choose several options | Checkboxes |
| Progress toward a goal | `<progress>` |
| Measurement within a range | `<meter>` |
| Page regions | `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>` |

ARIA can describe a custom implementation, but it does not automatically supply keyboard behavior, focus management, validation, or state changes. The first rule of ARIA is to avoid adding it when native HTML already provides the required semantics.

### Focus and keyboard checklist

- Every interactive element is reachable with `Tab` or the component's documented arrow-key model.
- Focus is visible against every supported surface and in forced-colors mode.
- Focus is not moved unexpectedly during ordinary reading.
- Opening a dialog or menu moves focus to a logical destination.
- Closing an overlay returns focus to its trigger when possible.
- A keyboard user can escape a modal, popover, drawer, or menu.
- No element is keyboard-focusable while hidden or inert.
- Skip links or equivalent landmarks let users bypass repeated navigation.

```css
.skip-link {
  position: absolute;
  inset-inline-start: 1rem;
  inset-block-start: 1rem;
  transform: translateY(-200%);
  z-index: 10;
}

.skip-link:focus-visible {
  transform: none;
  padding: .7rem 1rem;
  background: #172033;
  color: #fff;
}
```

```html
<a class="skip-link" href="#main-content">Skip to main content</a>
<main id="main-content">...</main>
```

### A11y smoke test for a new component

Run this short test before opening a pull request:

1. Find the component without a mouse.
2. Operate its primary action with `Enter` and `Space` where appropriate.
3. Inspect the accessibility tree and confirm its name, role, and state.
4. Zoom to 200% and look for clipping or hidden controls.
5. Enable reduced motion and confirm that the task still works.
6. Enable forced colors or high contrast and confirm that state remains visible.
7. Replace sample text with a long translation.
8. Turn off JavaScript and confirm the baseline behavior.

### Common CSS failure patterns

| Failure | Why it harms users | Safer alternative |
|---|---|---|
| `outline: none` everywhere | Removes keyboard orientation | Use `:focus-visible` with a strong outline |
| Fixed height around text | Clips zoomed or translated content | Use `min-block-size` and natural height |
| `overflow: hidden` on articles | Hides content and focus targets | Use `overflow: clip` only when intentional, or allow flow |
| Color-only status | Excludes color-blind and forced-color users | Add text, icons, borders, or patterns |
| `pointer-events: none` on controls | Makes a control unreachable | Fix layering and hit areas instead |
| Reordered form fields | Creates a different reading sequence | Change the source order |
| Placeholder as a label | Disappears during input | Use a persistent `<label>` |
| Auto-playing motion | Can trigger discomfort and distraction | Pause, provide controls, respect reduced motion |
| Tiny touch targets | Makes activation difficult | Provide a generous hit area |
| Custom `div` controls | Missing keyboard and semantics | Start with native HTML |

### A11y test record

Keep a short record with each release. It should identify the page or component, the browsers and assistive technologies tested, the zoom and preference settings, discovered issues, severity, owner, and retest date. This turns accessibility from an informal hope into a repeatable quality practice.

```md
Accessibility test record

- Component or page:
- Release:
- Browser and version:
- Screen reader or accessibility tree tool:
- Keyboard path tested:
- Zoom/text-size setting:
- Reduced motion:
- Forced colors/high contrast:
- Touch or mobile device:
- Findings:
- Follow-up owner:
- Retest date:
```

### Severity and triage

Prioritize issues by user impact, not by how easy they are to fix. A missing keyboard path for a required task, inaccessible form error, or content hidden at zoom deserves urgent attention. A minor spacing inconsistency in a non-essential decorative region may wait.

When triaging, record the affected users, task, workaround if any, reproducibility, and whether the issue blocks completion. This gives product and engineering a shared basis for deciding what ships.

### Useful references

- WAI-ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN accessibility: https://developer.mozilla.org/en-US/docs/Web/Accessibility
- web.dev accessibility: https://web.dev/accessibility/
- axe-core: https://github.com/dequelabs/axe-core
- Lighthouse accessibility audits: https://developer.chrome.com/docs/lighthouse/accessibility/
