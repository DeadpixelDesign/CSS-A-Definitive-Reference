# Compatibility, fallbacks, and polyfills

Can I Use data, MDN browser-compat-data, and real-device tests answer different questions. Can I Use gives a quick feature view. MDN often adds caveats and links to specifications. Your own analytics tell you which browsers matter.

### Compatibility is a product decision

Compatibility is not a promise that every browser will render every feature identically. It is a decision about which users receive the baseline experience, which users receive an enhancement, and what happens when a browser cannot parse or implement the enhancement.

Use this chain when planning a feature:

1. Identify the audience and the browsers that matter to the product.
2. Separate required content and interaction from optional visual enhancement.
3. Choose a baseline implementation that remains useful without the enhancement.
4. Add the modern implementation after the baseline declaration or inside a feature query.
5. Test the result in representative browsers, devices, zoom levels, input modes, and writing directions.

The most robust fallback is usually not a second copy of the entire design. It is a simpler layout that preserves reading order, content, focus, and task completion.

### Baseline, MDN, and Can I Use answer different questions

Browser support labels are useful only when you know what they measure:

- **Baseline** communicates whether a Web Platform feature is interoperable across a defined set of browsers and when it became newly or widely available.
- **MDN Browser Compatibility Data** provides detailed support tables, notes, prefixes, partial support, and links to implementation caveats.
- **Can I Use** is a fast visual comparison of support across browser versions and feature-specific notes.
- **Your analytics and device testing** reveal whether the browsers represented by your actual users behave as expected.

Treat these sources as evidence for a decision, not as a substitute for the decision. A feature can be broadly supported and still be inappropriate for a required interaction if it has important semantic, accessibility, or performance caveats.

### Build a browser target policy

Write the browser policy down so that the team, build tools, and QA process use the same assumptions. Browserslist is a common way to share that policy with Autoprefixer, PostCSS, Babel, and testing tools.

```json
{
  "browserslist": {
    "production": [
      "> 0.5%",
      "last 2 versions",
      "Firefox ESR",
      "not dead"
    ],
    "development": ["last 1 chrome version", "last 1 firefox version"]
  }
}
```

Do not copy this policy blindly. A public marketing site, an internal application, an embedded webview, and a design system may have very different targets. Record exceptions explicitly when a customer, contract, or accessibility requirement needs an older engine.

### Syntax fallback versus behavior fallback

A syntax fallback helps when a browser can parse the older declaration but does not understand the newer one. A behavior fallback is needed when the browser cannot reproduce the interaction or layout semantics at all.

```css
.panel {
  /* Older engines can use this simple layout. */
  display: block;
  padding: 1rem;
}

@supports (display: grid) {
  .panel {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 18rem;
    gap: 1.5rem;
  }
}
```

The fallback preserves the content as a normal block flow. The enhancement adds columns only when the browser confirms that it understands the required declaration.

### Feature queries with `@supports`

Use `@supports` when a declaration or selector needs to be parsed before the enhanced rule can be trusted. Put the baseline outside the query and the enhancement inside it.

```css
.notice {
  padding: 1rem;
  background: #f8fafc;
}

@supports (background: linear-gradient(135deg, #fff, #000)) {
  .notice {
    background: linear-gradient(135deg, #eff6ff, #ecfeff);
  }
}

@supports selector(:has(*)) {
  .field:has(input:invalid) {
    border-color: #b42318;
  }
}
```

`@supports` answers whether the browser recognizes syntax. It does not prove that a complex layout will be visually identical to another browser, nor does it test whether a JavaScript API exists.

### JavaScript feature detection

Use JavaScript detection only for behavior that cannot be expressed as a CSS fallback. `CSS.supports()` is useful for CSS declarations; an object or method check is appropriate for a JavaScript API.

```js
if (CSS.supports('selector(:has(*))')) {
  document.documentElement.classList.add('has-has-selector');
}

if ('IntersectionObserver' in window) {
  startLazyEnhancement();
} else {
  loadContentImmediately();
}
```

Do not hide required content because an enhancement is unavailable. Detection should select an implementation, not become a new failure point.

### Fallbacks for color and visual effects

Place a broadly understood color before a newer color space or function. If the browser ignores the later declaration, the earlier value remains active.

```css
.hero {
  background: #172033;
  background: oklch(28% 0.04 260);
  color: #fff;
  color: oklch(98% 0.01 260);
}
```

The same pattern works for gradients, shadows, filters, and other visual enhancements. Avoid making text contrast depend entirely on an experimental value; verify the fallback itself.

### Fallbacks for layout features

Start with normal flow or a simple flex layout when that is sufficient. Add grid, subgrid, container queries, or other layout capabilities as enhancements rather than forcing every browser through a brittle imitation.

```css
.dashboard {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.dashboard > * {
  flex: 1 1 18rem;
}

@supports (display: grid) {
  .dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr));
  }
}
```

### Available polyfill and transform options

Use a named tool only when it matches the feature and your target browsers. PostCSS Preset Env can transform or provide fallbacks for a defined set of standard CSS features based on your Browserslist targets. For CSS custom properties in legacy browsers, `css-vars-ponyfill` provides client-side transformation with documented limitations. Treat both as targeted compatibility tools, not as replacements for testing the actual layout and interaction.

```js
// postcss.config.cjs
const postcssPresetEnv = require('postcss-preset-env');
module.exports = {
  plugins: [postcssPresetEnv({ stage: 2 })]
};
```

```js
import cssVars from 'css-vars-ponyfill';
cssVars({ watch: true });
```

### Polyfills: when they are appropriate

A polyfill is a runtime implementation of a platform feature that the browser does not provide. CSS polyfills are less common than JavaScript polyfills because a CSS feature often depends on the browser's layout engine, style system, painting pipeline, or accessibility tree. A script can sometimes rewrite styles, but it cannot always reproduce native behavior reliably.

Use a polyfill when all of these conditions are true:

- the feature materially improves the experience for a target browser;
- the polyfill has a maintained, documented implementation;
- its performance and failure modes are understood;
- the baseline remains usable if the polyfill fails;
- the added payload is justified by the users who need it.

Do not add a polyfill simply because a feature is new. Prefer a simpler CSS fallback when the requirement is visual rather than structural. For example, use a solid background before a gradient, normal flow before a masonry-like layout, and a fixed spacing value before a newer interpolation function.

### PostCSS, Autoprefixer, and transformed CSS

Build-time tools are useful when the source syntax can be translated without changing the product's meaning. PostCSS Preset Env can convert selected modern CSS features according to a Browserslist target. Autoprefixer can add vendor prefixes where its compatibility data indicates that they are needed.

```js
// postcss.config.cjs
module.exports = {
  plugins: {
    'postcss-preset-env': {
      stage: 3,
      features: {
        'custom-media-queries': true
      },
      preserve: true
    },
    autoprefixer: {}
  }
};
```

`preserve: true` can keep the modern rule alongside the generated fallback. Review the output rather than assuming that a transform is semantically perfect. A tool can rewrite syntax; it cannot decide whether a fallback has the right content order, interaction model, or contrast.

### Custom properties in older targets

Custom properties are runtime values. That makes them powerful for theming, but also means a purely build-time transform may not reproduce runtime changes. If an older target must receive a static version, provide an explicit fallback or use a targeted tool such as `css-vars-ponyfill` after reviewing its documented limitations.

```css
:root {
  --brand: #1d4ed8;
}

.button {
  background: #1d4ed8;
  background: var(--brand);
  color: #fff;
}
```

The first declaration is useful when the browser does not understand `var()`. The second declaration lets modern browsers use the theme token. Keep the fallback close to the enhanced declaration so that future edits do not accidentally separate them.

### Vendor prefixes and legacy engines

Prefixes are historical compatibility mechanisms, not a design strategy. Write the unprefixed standard property first and add a prefix only when a supported target actually needs it.

```css
.glass-panel {
  background: rgb(255 255 255 / .72);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
}
```

The translucent background remains useful when backdrop filtering is unavailable. Never make the prefixed declaration the only implementation, and do not carry prefixes indefinitely without checking current target data.

### Compatibility testing matrix

Test a feature at more than one browser width. A compatibility bug may appear only with a particular engine, input method, zoom level, writing mode, or reduced-motion preference.

| Dimension | Minimum coverage to consider |
|---|---|
| Engine | Chromium, Firefox, WebKit |
| Form factor | Desktop, small phone, large phone, tablet |
| Input | Mouse, keyboard, touch, screen reader where relevant |
| Display | Narrow viewport, wide viewport, zoomed text, high pixel density |
| Preferences | Dark mode, reduced motion, forced colors, increased contrast |
| Direction | Left-to-right and right-to-left when the interface supports both |
| Network | Cached load, slow load, JavaScript delayed or unavailable |

Record what “supported” means for the feature: parsed, visually acceptable, keyboard accessible, screen-reader understandable, and performant enough for the product. These are separate checks.

### Automated checks for fallbacks

Automated browser tests can verify that the baseline remains present and that the enhancement activates when supported. Keep assertions about user outcomes instead of asserting a particular internal CSS implementation.

```ts
import { test, expect } from '@playwright/test';

test('dashboard remains readable at a narrow width', async ({ page }) => {
  await page.setViewportSize({ width: 360, height: 800 });
  await page.goto('/dashboard');

  await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
  await expect(page.getByText('Recent activity')).toBeVisible();
});
```

Add a visual comparison only when the layout is stable enough to make that comparison meaningful. For feature detection, test the fallback path deliberately rather than relying only on the newest local browser.

### A release checklist for new CSS

Before shipping a feature with compatibility implications, ask:

1. What is the required baseline experience?
2. Which declaration or API provides the enhancement?
3. What happens when the browser ignores the new syntax?
4. Does the fallback preserve content order and keyboard access?
5. Is the feature available in the browsers represented by current users?
6. Are there partial-support notes or known implementation bugs?
7. Does the feature need `@supports`, JavaScript detection, or neither?
8. Can a build-time transform safely help the target browsers?
9. Is a maintained polyfill available and justified, if one is actually needed?
10. Has the result been tested with zoom, reduced motion, forced colors, and slow loading?

This checklist turns “browser support” into an observable engineering decision. It also makes future removal easier: when the baseline changes, you can identify which fallback, transform, prefix, or polyfill can be retired.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- Can I Use: https://caniuse.com/
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
