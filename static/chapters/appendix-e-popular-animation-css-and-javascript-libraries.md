# Appendix E: Popular animation CSS and JavaScript libraries

Vendor prefixes are historical compatibility markers such as `-webkit-`, `-moz-`, `-ms-`, and `-o-`. Browsers used them to expose experimental or non-standard behavior before a feature was standardized. New CSS features generally ship unprefixed now, so a prefix should not be added automatically and should never be used as a substitute for checking current browser support.

The table below records prefixed properties that can still appear in production stylesheets or legacy code. It is intentionally selective: it focuses on properties a maintainer may need to recognize, migrate, or retain for a documented target rather than listing every historical engine extension.

| Standard or related property | Prefixed form | Current guidance |
| --- | --- | --- |
| `appearance` | `-webkit-appearance`, `-moz-appearance` | Put the standard property first. Keep a prefixed declaration only when testing shows that a specific legacy control-rendering target requires it. |
| `backdrop-filter` | `-webkit-backdrop-filter` | Use the unprefixed declaration first, then the WebKit fallback when supporting older Safari versions. Always provide an opaque or translucent background fallback. |
| `text-size-adjust` | `-webkit-text-size-adjust` | Use the standard property first and the prefixed alias only for older mobile WebKit behavior. Avoid disabling text adjustment unless the responsive layout has been tested carefully. |
| `mask-*` | `-webkit-mask-*` | Treat prefixed mask declarations as a targeted Safari compatibility layer. Keep a non-mask fallback when the effect is decorative or affects contrast. |
| `text-stroke` | `-webkit-text-stroke`, `-webkit-text-stroke-width`, `-webkit-text-stroke-color` | This remains a WebKit extension rather than a broadly standardized property. Use it only as a progressive visual enhancement and preserve readable filled text beneath it. |
| — | `-webkit-tap-highlight-color` | WebKit/Blink mobile UI extension. Use sparingly; do not remove the tap indication without supplying another visible pressed or focus state. |
| — | `-webkit-touch-callout` | WebKit interaction extension. Avoid relying on it for functionality; it only changes a platform gesture affordance. |
| — | `-webkit-box-reflect` | Non-standard visual reflection. Do not use it for essential content or layout. |

### The standard-first declaration pattern

When a prefixed declaration is genuinely required, place the unprefixed declaration first and the prefixed form immediately after it. The later declaration can override the standard one in an older engine without hiding the intended standard behavior from current browsers.

```css
.glass-panel {
  background: rgb(255 255 255 / .72);
  backdrop-filter: blur(1rem);
  -webkit-backdrop-filter: blur(1rem);
}
```

Do not copy this pattern blindly. Verify the exact target browsers, test the fallback, and remove the prefix when it no longer serves a supported audience.

### Feature-querying a prefixed fallback

If the enhancement is optional, feature-query both the standard and prefixed forms. The condition should describe the capability the component needs, not the brand of the browser.

```css
.surface {
  background: #f4f7fb;
}

@supports (backdrop-filter: blur(1rem)) or
          (-webkit-backdrop-filter: blur(1rem)) {
  .surface {
    background: rgb(244 247 251 / .72);
    backdrop-filter: blur(1rem);
    -webkit-backdrop-filter: blur(1rem);
  }
}
```

The fallback remains useful when neither declaration is supported. A feature query does not make a non-standard property standard; it only prevents unsupported syntax from becoming part of the active enhancement path.

### Migrating legacy prefixed code

When reviewing an older stylesheet:

1. Search for each prefix and group declarations by the feature they implement.
2. Check whether an unprefixed standard property now covers the use case.
3. Put the standard declaration first and retain a prefix only with a documented browser requirement.
4. Replace prefixed selectors and pseudo-elements with standard equivalents when available, such as `::file-selector-button` or `::placeholder`.
5. Test visual behavior, keyboard focus, touch feedback, and reduced-motion or high-contrast modes.
6. Remove the compatibility line after the support policy no longer includes the affected browser.

```css
/* Legacy stylesheet: migrate toward the standard property. */
.control {
  -webkit-appearance: none;
  appearance: none;
}

/* Keep the native focus signal visible after changing appearance. */
.control:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 2px;
}
```

Changing `appearance` can remove important platform affordances. Rebuild the control's focus, disabled, invalid, and pressed states before shipping a custom appearance.

### What not to do

Do not write a long list of every historical prefix “just in case,” use user-agent sniffing to choose a prefix, or assume a prefix is harmless because the browser ignores unknown declarations. A prefix can change rendering, accessibility, or interaction behavior in only one engine.

```css
/* Avoid: a historical prefix pile with no support policy. */
/*
.box {
  -webkit-transform: translateZ(0);
  -moz-transform: translateZ(0);
  -ms-transform: translateZ(0);
  -o-transform: translateZ(0);
  transform: translateZ(0);
}
*/

/* Prefer the standard property when current targets support it. */
.box {
  transform: translateZ(0);
}
```

### Source trail

- MDN CSS properties reference, including non-standard prefixed properties: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- MDN WebKit extensions: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions
- MDN CSS FAQ on vendor prefixes: https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Solve_CSS_problems/CSS_FAQ
- MDN `appearance`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance
- MDN `text-size-adjust`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust
