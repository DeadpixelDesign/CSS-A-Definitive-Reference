# CSSOM and cross-language tooling

The CSS Object Model lets browser JavaScript inspect and manipulate CSS. Server-side languages do not directly manipulate a user’s rendered DOM; they emit stylesheets, templates, tokens, or build artifacts.

The most important boundary in this chapter is location. CSSOM code runs in a browser document and can inspect the document's stylesheets, rules, computed values, and inline styles. PHP and Python normally run before the response reaches the browser, so they generate HTML, CSS, JSON, or build files rather than calling `document.styleSheets`. TypeScript is browser JavaScript with a type system and a build step; it uses the same CSSOM APIs after compilation.

### CSSOM vocabulary

| Object or API | What it represents | Typical use |
|---|---|---|
| `CSSStyleDeclaration` | A collection of declarations | Read or set inline styles and computed values |
| `CSSStyleSheet` | A stylesheet and its rule list | Inspect or insert rules when access is permitted |
| `CSSRule` | One rule in a stylesheet | Read selectors, declarations, or nested rules |
| `getComputedStyle()` | The resolved style for an element | Measure the value the browser is actually using |
| `CSS.supports()` | CSS feature detection | Choose a CSS or JavaScript enhancement |
| `document adoptedStyleSheets` | Constructable stylesheets attached to a document or shadow root | Share generated styles safely across components |

Computed style is not the same as the value written in a stylesheet. It reflects the cascade, inheritance, initial values, media conditions, and browser resolution of units. Use the API for inspection and controlled interaction, not as a replacement for a maintainable stylesheet.

### JavaScript: read and update custom properties

Use `style.setProperty()` for custom properties because their names contain two hyphens. Use `getComputedStyle()` when you need the active value after inheritance and the cascade have been applied.

```html
<label>
  Accent color
  <input id="accent" type="color" value="#1d4ed8">
</label>
<button class="button" type="button">Preview</button>
```

```css
:root {
  --accent: #1d4ed8;
}

.button {
  border: 0;
  border-radius: .5rem;
  background: var(--accent);
  color: white;
  padding: .7rem 1rem;
  font: inherit;
}
```

```js
const root = document.documentElement;
const accentInput = document.querySelector('#accent');

accentInput.addEventListener('input', (event) => {
  const color = event.currentTarget.value;
  root.style.setProperty('--accent', color);
});

const activeAccent = getComputedStyle(root)
  .getPropertyValue('--accent')
  .trim();
console.log(activeAccent);
```

Prefer a class or a data attribute when a change represents a named state such as `dark`, `compact`, or `high-contrast`. Use a custom property when the value itself is the variable.

### JavaScript: inspect stylesheets safely

Same-origin stylesheets can usually be inspected through `document.styleSheets`. A stylesheet loaded from another origin may throw a security exception when its rules are read unless the server permits access with the appropriate CORS headers.

```js
for (const sheet of document.styleSheets) {
  try {
    for (const rule of sheet.cssRules) {
      if (rule.type === CSSRule.STYLE_RULE && rule.selectorText === '.button') {
        console.log(rule.style.getPropertyValue('background-color'));
      }
    }
  } catch (error) {
    console.info('Stylesheet is not readable from this origin', sheet.href);
  }
}
```

Do not make application behavior depend on being able to read every stylesheet. Prefer data attributes, custom properties, and component-owned styles when code needs a reliable contract.

### JavaScript: constructable stylesheets

Constructable stylesheets are useful for sharing generated CSS between a document and shadow roots. Keep the source string controlled by the application; do not interpolate untrusted text into a stylesheet.

```js
const themeSheet = new CSSStyleSheet();
themeSheet.replaceSync(`
  :host {
    --panel-surface: #ffffff;
    --panel-ink: #172033;
  }
`);

document.adoptedStyleSheets = [
  ...document.adoptedStyleSheets,
  themeSheet
];
```

When compatibility with older browsers matters, a regular `<style>` element or an imported stylesheet may be the simpler fallback.

### JavaScript: CSS feature detection and typed values

`CSS.supports()` tests whether the browser recognizes a declaration or selector. It does not test whether the entire design is visually correct.

```js
const supportsGrid = CSS.supports('display', 'grid');
const supportsHas = CSS.supports('selector(:has(*))');

document.documentElement.classList.toggle('supports-grid', supportsGrid);
document.documentElement.classList.toggle('supports-has', supportsHas);
```

Some browsers also expose the CSS Typed Object Model. Detect it before using it and keep a string-based CSSOM path available.

```js
const card = document.querySelector('.card');

if (card.attributeStyleMap) {
  card.attributeStyleMap.set('padding-inline', CSS.px(24));
} else {
  card.style.setProperty('padding-inline', '24px');
}
```

### TypeScript: typed CSS custom-property helpers

TypeScript does not change the browser API. It makes the contracts around that API explicit and catches mistakes before the code is shipped.

```ts
type CssVariable = `--${string}`;

export function setCssVariable(
  element: HTMLElement,
  name: CssVariable,
  value: string
): void {
  element.style.setProperty(name, value);
}

export function readCssVariable(
  element: Element,
  name: CssVariable
): string {
  return getComputedStyle(element).getPropertyValue(name).trim();
}
```

```ts
const root = document.documentElement;
setCssVariable(root, '--accent', '#0f766e');
const accent = readCssVariable(root, '--accent');
```

Keep the `CssVariable` type narrow. It prevents accidental calls such as `setCssVariable(root, 'color', 'red')`, which should instead use `element.style.color` or a property-specific helper.

### TypeScript: a typed theme controller

Represent named theme choices as a union rather than accepting arbitrary strings. The browser then receives a controlled data attribute, while CSS owns the actual theme rules.

```ts
type Theme = 'light' | 'dark' | 'system';

export function applyTheme(theme: Theme): void {
  const root = document.documentElement;
  root.dataset.theme = theme;
}

const themeSelect = document.querySelector<HTMLSelectElement>('#theme');
themeSelect?.addEventListener('change', () => {
  const value = themeSelect.value;
  if (value === 'light' || value === 'dark' || value === 'system') {
    applyTheme(value);
  }
});
```

```css
:root[data-theme="light"] { color-scheme: light; }
:root[data-theme="dark"] { color-scheme: dark; }
```

### TypeScript: observing layout changes

Use `ResizeObserver` when a component needs to respond to its own rendered size. Prefer container queries for purely presentational changes; use the observer when JavaScript must change behavior or data.

```ts
const panel = document.querySelector<HTMLElement>('.panel');

if (panel && 'ResizeObserver' in window) {
  const observer = new ResizeObserver(([entry]) => {
    panel.dataset.density = entry.contentRect.inlineSize < 420
      ? 'compact'
      : 'comfortable';
  });

  observer.observe(panel);
}
```

### PHP: generate a safe CSS response

PHP can generate CSS on the server. Treat every value that enters a stylesheet as untrusted input, allow-list the permitted values, and send the correct content type.

```php
<?php
$allowed = [
    'blue' => '#1d4ed8',
    'teal' => '#0f766e',
    'gold' => '#a16207',
];

$choice = $_GET['theme'] ?? 'blue';
$accent = $allowed[$choice] ?? $allowed['blue'];

header('Content-Type: text/css; charset=utf-8');
header('Cache-Control: public, max-age=3600');

echo ":root { --accent: {$accent}; }\n";
```

Allow-listing is stronger than escaping alone because it ensures the value belongs to the grammar your design expects. In many applications, static CSS plus a data attribute is simpler and easier to cache than a per-request stylesheet.

### PHP: emit design tokens as CSS

A server can render tokens from configuration or a database, but the output should still be constrained to known CSS values.

```php
<?php
$tokens = [
    '--brand' => '#1d4ed8',
    '--radius-md' => '0.75rem',
    '--content-max' => '72rem',
];

header('Content-Type: text/css; charset=utf-8');
echo ":root {\n";
foreach ($tokens as $name => $value) {
    echo "  {$name}: {$value};\n";
}
echo "}\n";
```

For a production endpoint, validate both token names and values against explicit patterns or configuration objects. Never write arbitrary request parameters directly into CSS.

### Python: generate a stylesheet from tokens

Python is commonly used for static-site generation, build pipelines, and server responses. It can generate CSS, but it does not have access to a visitor's live CSSOM unless browser automation is involved.

```python
from html import escape

TOKENS = {
    "brand": "#1d4ed8",
    "radius-md": "0.75rem",
    "content-max": "72rem",
}

css = ":root {\n"
for name, value in TOKENS.items():
    css += f"  --{escape(name)}: {escape(value)};\n"
css += "}\n"

print(css)
```

For a build tool, validate token names and values before escaping them. Escaping protects the output format; validation protects the design contract.

### Python: serve CSS with a web framework

A Python web framework can return generated CSS with an explicit media type. The exact response helper varies by framework; this Flask example shows the boundary.

```python
from flask import Flask, Response

app = Flask(__name__)

TOKENS = {
    "brand": "#1d4ed8",
    "surface": "#ffffff",
}

@app.get("/theme.css")
def theme_css():
    body = ":root {\n" + "".join(
        f"  --{name}: {value};\n"
        for name, value in TOKENS.items()
    ) + "}\n"
    return Response(body, mimetype="text/css")
```

In a real service, cache the response when tokens are stable and use a strict source of truth for values. Do not accept arbitrary CSS from a query parameter.

### Cross-language token contract

When JavaScript, TypeScript, PHP, and Python all participate in one application, define a small token contract rather than letting each language invent names independently.

```json
{
  "color": {
    "brand": "#1d4ed8",
    "surface": "#ffffff",
    "ink": "#172033"
  },
  "radius": {
    "md": "0.75rem"
  }
}
```

From that source, a build step can emit CSS custom properties, TypeScript types, PHP configuration, and Python constants. Keep the generated artifacts reproducible and review the CSS output, because the browser only receives the final CSS.

### CSSOM performance and maintainability

Batch style changes where possible. Repeatedly reading layout information after writing styles can force the browser to recalculate styles or layout. Prefer toggling a class or setting a small number of custom properties over creating hundreds of inline declarations.

```js
const panel = document.querySelector('.panel');

// One state change is easier for the browser and for maintainers.
panel.classList.toggle('is-expanded', shouldExpand);
```

When measurements are necessary, group reads together and writes together. Disconnect observers when components are removed, and keep generated styles scoped to the component that owns them.

```js
const root = document.documentElement;
root.style.setProperty('--accent', 'rebeccapurple');
const value = getComputedStyle(root).getPropertyValue('--accent').trim();
const supported = CSS.supports('display', 'grid');
```

```ts
function setCssVar(el: HTMLElement, name: `--${string}`, value: string) {
  el.style.setProperty(name, value);
}
```

```php
<?php
$brand = htmlspecialchars($_GET['brand'] ?? '#1d4ed8', ENT_QUOTES, 'UTF-8');
header('Content-Type: text/css; charset=utf-8');
echo ":root { --brand: {$brand}; }";
```

```python
from html import escape
tokens = {'brand': '#1d4ed8', 'radius': '1rem'}
css = ':root {\n' + ''.join(f'  --{k}: {escape(v)};\n' for k, v in tokens.items()) + '}\n'
```

Validate and allow-list values before putting them in CSS. Escaping is not a substitute for a property-aware input policy.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
