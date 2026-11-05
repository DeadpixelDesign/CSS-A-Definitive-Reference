# Worked component examples

This chapter is deliberately code-heavy. Each example is complete enough to paste into a small HTML file and adapt. The examples favor native HTML, low-specificity CSS, custom properties, logical properties, progressive enhancement, and accessible interaction.

### Responsive card grid

```html
<section class="card-grid" aria-labelledby="featured-title">
  <h2 id="featured-title">Featured projects</h2>
  <article class="card">
    <img class="card__image" src="project.webp" alt="A dashboard preview">
    <div class="card__body">
      <p class="card__eyebrow">Case study</p>
      <h3 class="card__title">A resilient card component</h3>
      <p class="card__copy">The layout adapts to its container, not a device label.</p>
      <a class="card__link" href="/projects/resilient-card">Read the case study</a>
    </div>
  </article>
</section>
```

```css
.card-grid {
  --card-gap: clamp(1rem, 2vw, 1.5rem);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: var(--card-gap);
}
.card-grid > h2 { grid-column: 1 / -1; }
.card {
  display: grid;
  overflow: clip;
  border: 1px solid var(--border, #d7deea);
  border-radius: 1rem;
  background: var(--surface, white);
  box-shadow: 0 1rem 2rem rgb(15 23 42 / .08);
}
.card__image { display: block; width: 100%; aspect-ratio: 16 / 9; object-fit: cover; }
.card__body { display: grid; gap: .7rem; padding: 1rem; }
.card__copy { max-inline-size: 45ch; margin: 0; color: var(--muted, #5b6475); }
.card__link { justify-self: start; color: var(--accent, #1d4ed8); }
```

### Navigation that wraps before it scrolls

```html
<header class="site-header">
  <a class="brand" href="/">Northstar</a>
  <button class="menu-button" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav id="site-nav" class="site-nav" aria-label="Primary">
    <a href="/work">Work</a><a href="/about">About</a><a href="/contact">Contact</a>
  </nav>
</header>
```

```css
.site-header {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem 1.5rem;
  padding-block: 1rem;
  border-block-end: 1px solid var(--border, #d7deea);
}
.brand { margin-inline-end: auto; font-weight: 750; text-decoration: none; }
.site-nav { display: flex; flex-wrap: wrap; gap: .75rem 1rem; }
.site-nav a { padding: .5rem .7rem; border-radius: .5rem; }
.site-nav a:hover { background: color-mix(in srgb, currentColor 10%, transparent); }
.menu-button { display: none; }
@media (max-width: 42rem) {
  .menu-button { display: inline-flex; }
  .site-nav { inline-size: 100%; }
}
```

### Form layout with errors and focus

```html
<form class="form" novalidate>
  <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" aria-describedby="email-help email-error" required><small id="email-help">We use this only for account notices.</small><p id="email-error" class="error" role="alert">Enter a valid email address.</p></div>
  <button class="button" type="submit">Create account</button>
</form>
```

```css
.form { display: grid; gap: 1.25rem; max-inline-size: 32rem; }
.field { display: grid; gap: .4rem; }
.field small { color: var(--muted, #5b6475); }
.field input { min-block-size: 2.75rem; padding-inline: .75rem; border: 1px solid var(--border, #94a3b8); border-radius: .5rem; font: inherit; }
.field input:focus-visible, .button:focus-visible { outline: 3px solid var(--focus, #1d4ed8); outline-offset: 3px; }
.field input:invalid:not(:placeholder-shown) { border-color: var(--danger, #b42318); }
.error { margin: 0; color: var(--danger, #b42318); }
.button { min-block-size: 2.75rem; padding-inline: 1rem; border: 0; border-radius: .5rem; background: var(--accent, #1d4ed8); color: white; font: inherit; cursor: pointer; }
```

### Dialog with progressive enhancement

```html
<dialog class="dialog" id="help-dialog" aria-labelledby="help-title">
  <form method="dialog" class="dialog__panel">
    <h2 id="help-title">Keyboard shortcuts</h2>
    <p>Press <kbd>?</kbd> to reopen this help panel.</p>
    <button class="button" value="close">Close</button>
  </form>
</dialog>
```

```css
.dialog { max-inline-size: min(90vw, 36rem); padding: 0; border: 0; border-radius: 1rem; box-shadow: 0 2rem 5rem rgb(15 23 42 / .3); }
.dialog::backdrop { background: rgb(15 23 42 / .55); backdrop-filter: blur(3px); }
.dialog__panel { display: grid; gap: 1rem; padding: clamp(1.25rem, 4vw, 2rem); }
@starting-style { .dialog[open] { opacity: 0; transform: translateY(1rem) scale(.98); } }
.dialog[open] { opacity: 1; transform: none; transition: opacity .2s ease, transform .2s ease; }
@media (prefers-reduced-motion: reduce) { .dialog[open] { transition: none; } }
```

### Modal dialog with the native `<dialog>` element

The previous example shows the dialog markup. This version includes the complete open-and-close interaction. `showModal()` creates a modal top-layer experience, makes the rest of the document inert, and gives the browser a defined place to return focus. Keep a visible close button and close on cancel so keyboard users are not trapped.

```html
<button id="open-settings" type="button">Open settings</button>

<dialog id="settings-dialog" aria-labelledby="settings-title">
  <form method="dialog" class="dialog__panel">
    <button class="dialog__close" value="cancel" aria-label="Close settings">×</button>
    <h2 id="settings-title">Settings</h2>
    <label>
      <span>Display name</span>
      <input name="display-name" autocomplete="name">
    </label>
    <button class="button" value="save">Save settings</button>
  </form>
</dialog>
```

```js
const openSettings = document.querySelector('#open-settings');
const settingsDialog = document.querySelector('#settings-dialog');

openSettings.addEventListener('click', () => {
  settingsDialog.showModal();
});

settingsDialog.addEventListener('close', () => {
  openSettings.focus();
});
```

```css
#settings-dialog {
  inline-size: min(92vw, 34rem);
  padding: 0;
  border: 0;
  border-radius: 1rem;
  color: var(--ink);
  background: var(--surface);
  box-shadow: 0 2rem 6rem rgb(15 23 42 / .3);
}

#settings-dialog::backdrop {
  background: rgb(15 23 42 / .58);
  backdrop-filter: blur(3px);
}

.dialog__panel { display: grid; gap: 1rem; padding: 1.5rem; }
.dialog__close { justify-self: end; border: 0; background: none; font-size: 1.5rem; cursor: pointer; }
```

### Accordion with `<details>` and `<summary>`

For independent expandable sections, `<details>` is the most direct native component. It provides disclosure semantics and keyboard behavior without a custom button-and-panel state machine. Use a group of details elements when more than one item may remain open.

```html
<section class="accordion" aria-labelledby="faq-title">
  <h2 id="faq-title">Frequently asked questions</h2>
  <details>
    <summary>What browsers does the book support?</summary>
    <div class="accordion__content">
      <p>Use the compatibility sources and your own target policy before shipping.</p>
    </div>
  </details>
  <details>
    <summary>Can I use the examples in a component library?</summary>
    <div class="accordion__content">
      <p>Yes. Keep the native semantics and adapt the tokens to your system.</p>
    </div>
  </details>
</section>
```

```css
.accordion { display: grid; gap: .75rem; max-inline-size: 48rem; }
.accordion details { border-block-end: 1px solid var(--border); }
.accordion summary { cursor: pointer; padding: 1rem 2rem 1rem 0; font-weight: 700; }
.accordion summary::marker { color: var(--accent); }
.accordion__content { padding: 0 1rem 1rem 0; color: var(--muted); }
```

If the design requires “only one panel open,” add a small controller that closes sibling details after the user opens one. Do not recreate disclosure behavior with a clickable `div`.

### Exclusive accordion with the `name` attribute

Modern HTML supports grouping details elements with the same `name` so that opening one closes the others. This is useful for a true accordion, but keep a fallback if your browser targets do not support the behavior.

```html
<details name="shipping-faq">
  <summary>How long does shipping take?</summary>
  <p>Standard shipping takes three to five business days.</p>
</details>
<details name="shipping-faq">
  <summary>Can I change my address?</summary>
  <p>Contact support before the order is dispatched.</p>
</details>
```

### Popover for lightweight actions and help

The Popover API is useful for non-modal overlays such as help panels, command surfaces, and small menus. A popover is not a replacement for a modal dialog: it does not represent a blocking decision and should not contain a required multi-step form.

```html
<button popovertarget="share-popover" type="button">Share</button>

<div id="share-popover" popover class="popover">
  <p>Copy the link or choose a service.</p>
  <button type="button" id="copy-link">Copy link</button>
</div>
```

```css
.popover {
  inset: auto;
  margin: .5rem;
  padding: 1rem;
  border: 1px solid var(--border);
  border-radius: .75rem;
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 1rem 3rem rgb(15 23 42 / .18);
}

@starting-style {
  .popover:popover-open { opacity: 0; transform: translateY(-.5rem); }
}

.popover:popover-open {
  opacity: 1;
  transform: none;
  transition: opacity .15s ease, transform .15s ease;
}
```

Use `popover="manual"` when several popovers may remain open, and the default auto behavior when the browser should manage light-dismiss behavior. Check target support and provide a button-driven disclosure fallback when the popover is not essential.

### Tabs: a composite widget that needs JavaScript

Tabs are not the same as an accordion. Only one tab panel is visible, and the tablist has an expected keyboard model. Use buttons for tabs, connect them with `aria-controls` and `aria-labelledby`, and manage the selected state.

```html
<div class="tabs" data-tabs>
  <div role="tablist" aria-label="Account sections">
    <button id="profile-tab" role="tab" aria-selected="true" aria-controls="profile-panel">Profile</button>
    <button id="security-tab" role="tab" aria-selected="false" aria-controls="security-panel" tabindex="-1">Security</button>
  </div>
  <section id="profile-panel" role="tabpanel" aria-labelledby="profile-tab">Profile settings</section>
  <section id="security-panel" role="tabpanel" aria-labelledby="security-tab" hidden>Security settings</section>
</div>
```

```js
const tabs = [...document.querySelectorAll('[role="tab"]')];

function activateTab(nextTab) {
  for (const tab of tabs) {
    const selected = tab === nextTab;
    tab.setAttribute('aria-selected', String(selected));
    tab.tabIndex = selected ? 0 : -1;
    document.getElementById(tab.getAttribute('aria-controls')).hidden = !selected;
  }
}

tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => activateTab(tab));
  tab.addEventListener('keydown', (event) => {
    if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
    event.preventDefault();
    const direction = event.key === 'ArrowRight' ? 1 : -1;
    const next = tabs[(index + direction + tabs.length) % tabs.length];
    next.focus();
    activateTab(next);
  });
});
```

For long content or mobile layouts, an accordion may be more usable than tabs. Do not force tabs into a narrow viewport if the panels are difficult to discover or compare.

### Tooltip and description text

Use the native `title` attribute only for simple, non-essential hints. For important explanations, put the text in the document and connect it with `aria-describedby`. A tooltip should never be the only place where essential content appears.

```html
<button class="icon-button" aria-describedby="save-hint" type="button">
  <span aria-hidden="true">⌘</span>
  <span class="visually-hidden">Save</span>
</button>
<span id="save-hint" class="hint">Save a draft without publishing it.</span>
```

```css
.hint { max-inline-size: 28ch; color: var(--muted); font-size: .875rem; }
.visually-hidden {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

### Toast and status messages

Toasts should communicate a short-lived result without stealing focus. Use `role="status"` for a non-urgent update and `role="alert"` for an urgent error that needs immediate announcement. Keep a persistent status or inline error for information that users must be able to find later.

```html
<button id="save-button" type="button">Save</button>
<div id="toast" class="toast" role="status" aria-live="polite" hidden></div>
```

```js
const toast = document.querySelector('#toast');
let toastTimer;

function showToast(message) {
  toast.textContent = message;
  toast.hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { toast.hidden = true; }, 4000);
}

document.querySelector('#save-button').addEventListener('click', () => {
  showToast('Draft saved.');
});
```

```css
.toast {
  position: fixed;
  inset: auto 1rem 1rem auto;
  max-inline-size: min(90vw, 24rem);
  padding: .8rem 1rem;
  border-radius: .6rem;
  background: var(--ink);
  color: var(--surface);
  box-shadow: 0 1rem 2rem rgb(15 23 42 / .2);
}
```

### Menus and command buttons

Use a real `<button>` to open a menu and real links or buttons for its commands. A menu is not simply a row of links styled to look like a dropdown; if you use `role="menu"`, implement its keyboard model. For ordinary site navigation, a `<nav>` with links is usually the more accessible choice.

```html
<details class="menu">
  <summary>Account</summary>
  <div class="menu__items">
    <a href="/profile">Profile</a>
    <a href="/settings">Settings</a>
    <button type="button" id="sign-out">Sign out</button>
  </div>
</details>
```

```css
.menu { position: relative; inline-size: max-content; }
.menu summary { cursor: pointer; list-style: none; }
.menu summary::-webkit-details-marker { display: none; }
.menu__items {
  position: absolute;
  inset-block-start: calc(100% + .5rem);
  inset-inline-end: 0;
  display: grid;
  min-inline-size: 12rem;
  padding: .4rem;
  border: 1px solid var(--border);
  border-radius: .6rem;
  background: var(--surface);
  box-shadow: 0 1rem 2rem rgb(15 23 42 / .16);
}
.menu__items :is(a, button) { padding: .65rem .75rem; text-align: start; }
```

### Native controls before custom controls

Before writing a component from scratch, check whether HTML already provides the semantics and interaction: `<dialog>` for modal decisions, `<details>` for disclosure, `<select>` for a closed list of options, `<input type="date">` for dates, `<progress>` for task progress, and `<meter>` for a bounded measurement. Native controls inherit browser accessibility, keyboard, and platform behavior that a custom recreation must reproduce.

If the native control cannot meet a genuine product requirement, document the missing behavior and test the replacement with keyboard, touch, screen readers, zoom, forced colors, and reduced motion.

### Theme tokens and user preference

```css
:root {
  color-scheme: light dark;
  --surface: light-dark(#ffffff, #111827);
  --ink: light-dark(#172033, #f8fafc);
  --muted: light-dark(#5b6475, #cbd5e1);
  --border: light-dark(#d7deea, #334155);
  --accent: light-dark(#1d4ed8, #93c5fd);
}
@media (prefers-color-scheme: dark) {
  :root { --surface: #111827; --ink: #f8fafc; --muted: #cbd5e1; --border: #334155; --accent: #93c5fd; }
}
body { background: var(--surface); color: var(--ink); }
```

### CSSOM: live theme switch

```html
<button id="theme-toggle" type="button">Toggle theme</button>
<script type="module">
  const button = document.querySelector('#theme-toggle');
  const root = document.documentElement;
  button.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    root.style.colorScheme = next;
  });
</script>
```

### Scroll-driven progress with a fallback

```css
.reading-progress { position: fixed; inset: 0 0 auto; block-size: .25rem; transform-origin: left; background: var(--accent); animation: reading-progress linear; animation-timeline: scroll(root); }
@keyframes reading-progress { from { transform: scaleX(0); } to { transform: scaleX(1); } }
```

```js
const bar = document.querySelector('.reading-progress');
if (!CSS.supports('animation-timeline: scroll(root)')) {
  addEventListener('scroll', () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.transform = `scaleX(${max ? scrollY / max : 0})`;
  }, { passive: true });
}
```

### Print stylesheet

```css
@media print {
  nav, button, video, .no-print { display: none !important; }
  a { color: inherit; text-decoration: none; }
  a[href^="http"]::after { content: " (" attr(href) ")"; font-size: .8em; }
  h1, h2, h3 { break-after: avoid; }
  pre, table, figure { break-inside: avoid; }
}
```

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
