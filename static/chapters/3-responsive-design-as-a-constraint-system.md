# Responsive design as a constraint system

Responsive CSS is more than breakpoints. A resilient component has a minimum viable size, a maximum readable size, and behavior that changes when its available space or input environment changes.

### Media queries

Use media queries for environment state: viewport size, pointer precision, hover capability, color scheme, contrast, forced colors, and motion preference. Start with a content-driven layout and add a query when the content stops fitting—not because a device name suggests a breakpoint.

### Container queries

Container queries make components portable. A card should respond to its own inline size rather than to the viewport of the page that happens to contain it.

```css
.card-list { container-type: inline-size; }
@container (min-width: 42rem) {
  .card { grid-template-columns: 10rem 1fr; }
}
```

### Fluid sizing

Use `min()`, `max()`, and `clamp()` to encode constraints in the property value. A fluid scale should have a floor and a ceiling. Avoid values that make content unreadably small or cause touch targets to collapse.

### Mobile viewport units

`svh`, `lvh`, and `dvh` describe different viewport states. A full-height app shell often needs a safe baseline plus a dynamic enhancement. Test with browser chrome expanded and collapsed, with an on-screen keyboard, and in landscape.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
