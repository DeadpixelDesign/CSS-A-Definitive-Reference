# Forms, content, and interaction

Native controls provide semantics, keyboard behavior, validation hooks, and assistive technology integration. Style them carefully; replacing them wholesale creates more work than it removes.

### Form controls

`accent-color` can align checkboxes, radios, and progress indicators with a theme. `appearance` should be changed only when you are prepared to rebuild the affordance and test keyboard, forced colors, and platform differences. `field-sizing: content` is useful for intrinsically sized controls but needs a minimum size.

### Generated content

`content` is appropriate for decoration, counters, and small affordances. It should not be the only place where essential text exists. Pseudo-elements can be visually present but semantically absent.

### Interaction properties

`pointer-events`, `user-select`, `touch-action`, `cursor`, and `caret-color` change interaction. Document why a component changes them, especially when disabling selection or pointer events. Keep hit targets generous and preserve visible focus.

### Start with semantic controls

The most accessible form control is usually the native element that already expresses the intended behavior: `button` for an action, `a` for navigation, `input` for a value, `select` for a choice from a list, `textarea` for longer text, and `fieldset`/`legend` for related choices. CSS can improve the presentation without rebuilding keyboard behavior, validation hooks, focus management, and platform conventions.

```html
<form class="signup" action="/subscribe" method="post">
  <div class="field">
    <label for="email">Email address</label>
    <input
      id="email"
      name="email"
      type="email"
      autocomplete="email"
      required
      aria-describedby="email-help"
    >
    <p id="email-help" class="field__help">We use this to send the monthly edition.</p>
  </div>
  <button type="submit">Subscribe</button>
</form>
```

Do not replace a button with a styled `div`, or a checkbox with a clickable `span`, merely to gain visual control. A custom widget inherits responsibility for keyboard interaction, focus, states, announcements, pointer input, touch input, and high-contrast behavior.

### Normalize form typography carefully

Form controls do not always inherit the surrounding type styles in the same way across browsers and operating systems. Set the font deliberately, but keep a reliable fallback stack and a readable minimum size.

```css
button,
input,
select,
textarea {
  font: inherit;
  color: inherit;
}

input,
select,
textarea {
  font-size: 1rem;
  line-height: 1.4;
}
```

Avoid setting a control’s height to a value that clips enlarged text. Prefer `min-block-size`, padding, and a line-height that can accommodate user zoom.

### Layout a form with Grid

Grid is useful for aligning labels and controls while allowing the layout to collapse at smaller widths. Keep the DOM order logical: label, control, help text, and error message should be encountered in the same order visually and programmatically.

```css
.signup {
  display: grid;
  gap: 1.25rem;
  inline-size: min(100%, 42rem);
}

.field {
  display: grid;
  grid-template-columns: minmax(8rem, 12rem) minmax(0, 1fr);
  align-items: baseline;
  gap: .5rem 1rem;
}

.field__help,
.field__error {
  grid-column: 2;
  margin: 0;
}

@media (max-width: 38rem) {
  .field {
    grid-template-columns: 1fr;
  }

  .field__help,
  .field__error {
    grid-column: 1;
  }
}
```

### Labels, help text, and errors

Every control needs a visible or programmatically associated label. `aria-describedby` can associate supporting instructions or an error message, while `aria-errormessage` can identify an error when the control is marked invalid. Do not rely on placeholder text as the label: it disappears while the user types and often has insufficient contrast.

```html
<div class="field" data-state="error">
  <label for="username">Username</label>
  <input
    id="username"
    name="username"
    required
    minlength="3"
    aria-invalid="true"
    aria-describedby="username-error"
  >
  <p id="username-error" class="field__error" role="alert">
    Use at least three characters.
  </p>
</div>
```

The server must validate submitted data even when the client uses HTML constraints. Client-side validation improves feedback; it is not a security boundary.

### Constraint validation pseudo-classes

CSS can style control states such as `:required`, `:optional`, `:valid`, `:invalid`, `:in-range`, `:out-of-range`, `:checked`, `:disabled`, `:enabled`, `:read-only`, and `:read-write`. Use state styling to reinforce a message, not to make color the only indication.

```css
.field input,
.field textarea,
.field select {
  border: 2px solid var(--line);
  border-radius: .5rem;
  background: white;
}

.field input:focus-visible,
.field textarea:focus-visible,
.field select:focus-visible {
  border-color: var(--blue);
  outline: 3px solid rgb(29 78 216 / .25);
  outline-offset: 2px;
}

.field input:user-invalid,
.field textarea:user-invalid {
  border-color: #b42318;
}

.field input:disabled,
.field textarea:disabled,
.field select:disabled {
  cursor: not-allowed;
  opacity: .65;
}
```

`:invalid` can apply as soon as a required empty control is rendered, which can make a form look broken before the user interacts. Where supported, `:user-invalid` helps delay the error presentation until the user has interacted or attempted submission. Keep a class or data-state fallback when the exact pseudo-class is not part of the support policy.

### The `:has()` form pattern

Relational selectors can style a field wrapper based on its control’s state, keeping the markup clean. Use a fallback for browsers that do not support `:has()`.

```css
.field {
  border-inline-start: .25rem solid transparent;
  padding-inline-start: .75rem;
}

@supports selector(.field:has(:invalid)) {
  .field:has(input:user-invalid),
  .field:has(textarea:user-invalid),
  .field:has(select:user-invalid) {
    border-inline-start-color: #b42318;
  }
}
```

A selector can style the wrapper, but it should not replace the error text or a proper accessible relationship.

### Checkboxes, radios, and `accent-color`

`accent-color` changes the primary tint of supported native controls while preserving their platform behavior. It is the safest first choice when a theme needs colored checkboxes, radio buttons, range inputs, or progress indicators.

```css
input[type='checkbox'],
input[type='radio'],
input[type='range'],
progress {
  accent-color: var(--teal);
}
```

For a fully custom checkbox, `appearance: none` removes the native visual treatment, which means the stylesheet must rebuild checked, unchecked, disabled, focus-visible, forced-colors, and high-contrast states.

```css
.check input {
  appearance: none;
  inline-size: 1.25rem;
  block-size: 1.25rem;
  margin: 0;
  border: 2px solid currentColor;
  border-radius: .25rem;
  display: grid;
  place-content: center;
}

.check input::before {
  content: '';
  inline-size: .65rem;
  block-size: .65rem;
  scale: 0;
  background: currentColor;
  clip-path: polygon(14% 44%, 0 59%, 39% 100%, 100% 16%, 85% 3%, 39% 73%);
}

.check input:checked::before {
  scale: 1;
}

.check input:focus-visible {
  outline: 3px solid var(--blue);
  outline-offset: 3px;
}

@media (forced-colors: active) {
  .check input {
    border: 2px solid CanvasText;
  }

  .check input::before {
    background: CanvasText;
  }
}
```

If a native appearance already communicates the state clearly, prefer `accent-color` over rebuilding the widget.

### Selects and native controls

Selects, date pickers, color pickers, file inputs, range controls, `progress`, and `meter` have browser- and operating-system-specific internal parts. `appearance: none` can make a select look consistent, but it also removes the native arrow and may change the control’s affordance.

```css
.select-wrap {
  position: relative;
}

.select-wrap select {
  inline-size: 100%;
  appearance: none;
  padding-inline: .75rem 2.5rem;
}

.select-wrap::after {
  content: '';
  position: absolute;
  inset-inline-end: 1rem;
  inset-block-start: 50%;
  inline-size: .5rem;
  block-size: .5rem;
  border-inline-end: 2px solid currentColor;
  border-block-end: 2px solid currentColor;
  rotate: 45deg;
  translate: 0 -65%;
  pointer-events: none;
}
```

The decorative arrow must not block pointer input, and the select must remain the interactive element. Test the control on touch devices, keyboard navigation, forced colors, and zoom.

### Intrinsic control sizing with `field-sizing`

`field-sizing: content` allows supported text fields and textareas to size toward their content rather than using the default preferred control size. Always add minimum and maximum constraints; otherwise an empty input can become too narrow and a long value can take over the layout.

```css
.tag-input {
  field-sizing: content;
  min-inline-size: 10rem;
  max-inline-size: 100%;
}

.comment-box {
  field-sizing: content;
  min-block-size: 6rem;
  max-block-size: 18rem;
  overflow: auto;
}
```

Keep a fixed or fluid fallback before the enhancement:

```css
.tag-input {
  inline-size: min(100%, 24rem);
}

@supports (field-sizing: content) {
  .tag-input {
    inline-size: auto;
    field-sizing: content;
  }
}
```

### Generated content and counters

The `content` property works on pseudo-elements and generated markers. It is excellent for decorative icons, quotation marks, labels that are repeated from data attributes, and counters. It should not be the only location for essential instructions, error messages, or names.

```css
.steps {
  counter-reset: step;
}

.steps > li {
  counter-increment: step;
}

.steps > li::before {
  content: counter(step);
  display: inline-grid;
  place-items: center;
  inline-size: 1.75rem;
  block-size: 1.75rem;
  margin-inline-end: .5rem;
  border-radius: 50%;
  background: var(--navy);
  color: white;
}
```

If the number is important to understanding the procedure, include it in the HTML or ensure the generated representation is not the only accessible equivalent.

### Interaction properties

`pointer-events: none` makes an element transparent to pointer hit testing, but it does not remove the element from the keyboard focus order. `user-select: none` prevents selection but should not be applied to ordinary reading content. `touch-action` controls which gestures the browser may handle natively, and `caret-color` styles the text insertion caret.

```css
.tooltip {
  pointer-events: none;
}

.drag-handle {
  touch-action: none;
  cursor: grab;
  user-select: none;
}

.editor textarea {
  caret-color: var(--teal);
}
```

Use `touch-action: none` only on a deliberately interactive surface that implements the corresponding gesture. Removing browser scrolling without providing a reliable alternative can make a page unusable.

### Focus and focus-visible

Focus is a navigation state, not a decorative outline to remove. Use `:focus-visible` for a keyboard-appropriate emphasis while retaining a usable fallback for browsers without it. Never use `outline: none` without replacing it with an equally visible indicator.

```css
:where(button, input, select, textarea, a):focus-visible {
  outline: 3px solid var(--blue);
  outline-offset: 3px;
}

:where(button, input, select, textarea, a):focus:not(:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

Check focus against the component’s background, in forced colors, at 200% zoom, and when the control is inside a sticky or clipped ancestor.

### A progressive-enhancement form script

Native validation can handle many constraints. JavaScript should add useful behavior such as inline summaries, asynchronous checks, or submission state without disabling the browser’s semantics.

```js
const form = document.querySelector('.signup');

form?.addEventListener('submit', async (event) => {
  if (!form.checkValidity()) {
    event.preventDefault();
    form.reportValidity();
    return;
  }

  // Keep the native submission path unless an enhanced request is ready.
  const submit = form.querySelector('[type="submit"]');
  submit?.setAttribute('aria-busy', 'true');
});
```

Do not call `form.submit()` when you expect constraint validation; it bypasses interactive validation. Use the submit event, `checkValidity()`, or `reportValidity()` according to the desired behavior, and keep server-side validation authoritative.

### Form states and design tokens

Centralize state colors and spacing so every control communicates success, warning, error, disabled, and focus consistently.

```css
:root {
  --form-border: #9aa4b2;
  --form-focus: #1d4ed8;
  --form-error: #b42318;
  --form-success: #087443;
  --form-disabled: #667085;
}

.field[data-state='success'] input {
  border-color: var(--form-success);
}

.field[data-state='error'] input {
  border-color: var(--form-error);
}

.field__error {
  color: var(--form-error);
}
```

Never communicate a state by color alone. Pair it with text, an icon with an accessible name, a border or outline change, or a structural message.

### Forms, zoom, and writing modes

Use logical properties so form layouts adapt to right-to-left and vertical writing modes. Avoid fixed heights, absolute-positioned labels, and placeholder-only instructions that break when text is enlarged.

```css
.form-row {
  display: grid;
  grid-template-columns: minmax(10rem, 14rem) minmax(0, 1fr);
  gap: .75rem 1rem;
  padding-block: .75rem;
  border-block-end: 1px solid var(--line);
}

.form-row label {
  margin-block-start: .5rem;
}

@media (max-width: 40rem) {
  .form-row {
    grid-template-columns: 1fr;
  }

  .form-row label {
    margin-block-start: 0;
  }
}
```

### Interaction checklist

- Use the native HTML element that matches the task.
- Associate every control with a label and relevant help or error text.
- Keep DOM order, visual order, and keyboard order aligned.
- Preserve visible focus and test `:focus-visible` with keyboard navigation.
- Use native validation as feedback, never as server-side security.
- Prefer `accent-color` before rebuilding native controls with `appearance: none`.
- Add minimum and maximum sizes to `field-sizing: content`.
- Do not hide essential information in generated content.
- Test touch, keyboard, zoom, forced colors, screen readers, and reduced motion.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- MDN styling web forms: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms
- MDN advanced form styling: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Advanced_form_styling
- MDN UI pseudo-classes: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/UI_pseudo-classes
- MDN Constraint Validation API: https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation
- MDN `field-sizing`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing
- web.dev Learn Forms: https://web.dev/learn/forms
- web.dev styling form controls: https://web.dev/learn/forms/styling-form-controls
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
