# Flexbox

Flexbox is a one-dimensional layout system for distributing items along a main axis and aligning them across a cross axis. It is ideal for toolbars, navigation, button groups, rows of cards, and components whose content should share available space. Chapter 10 in the web edition is dedicated to this model and its implementation details.

### The flex container and its axes

`display: flex` creates a flex formatting context. `flex-direction` chooses the main axis; `flex-wrap` decides whether items can form multiple lines; and `flex-flow` combines both settings. The cross axis is perpendicular to the main axis, so changing direction changes what `justify-content` and `align-items` mean geometrically.

```css
.toolbar {
  display: flex;
  flex-flow: row wrap;
  align-items: center;
  justify-content: space-between;
  gap: .75rem 1rem;
}
```

Wireframe of the example:

```text
main axis →
┌─────────────────────────────────────────────┐
│ [logo]   [search................] [actions] │  cross axis ↕
│ [secondary action] [status]                 │  wrapped line
└─────────────────────────────────────────────┘
```

### Container properties

The principal container properties are `flex-direction`, `flex-wrap`, `flex-flow`, `justify-content`, `align-items`, `align-content`, `gap`, `row-gap`, and `column-gap`. `align-content` affects the collection of flex lines and does nothing when the container has only one line. `align-items` aligns items within each line.

```css
.gallery-controls {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: baseline;
  align-content: start;
  row-gap: .5rem;
  column-gap: 1rem;
}
```

### Item sizing: basis, grow, and shrink

`flex` is shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`. The basis is the starting size before free space is distributed. Grow shares positive free space; shrink shares negative free space. A common readable pattern is `flex: 1 1 16rem`, which gives each card a preferred basis while allowing it to adapt.

```css
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  flex: 1 1 16rem;
  min-inline-size: 0;
}

.card--featured {
  flex-grow: 2;
}
```

Wireframe of the sizing algorithm:

```text
available width: 60rem
┌──────────────┬──────────────┬──────────────┐
│ 16rem basis  │ 16rem basis  │ 16rem basis  │ + shared free space
└──────────────┴──────────────┴──────────────┘
       grow:1          grow:1          grow:2
```

### Alignment, auto margins, and order

`align-self` overrides the container’s `align-items` value for one item. An auto margin absorbs free space on its axis, which makes it useful for pushing a control to the far edge. `order` changes visual placement but not DOM reading order, so it should not be used to repair semantic structure.

```css
.nav {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav__actions {
  margin-inline-start: auto;
}

.nav__badge {
  align-self: flex-start;
}
```

### Wrapping and multi-line behavior

With `flex-wrap: wrap`, each line is laid out independently and `align-content` distributes the lines inside the container. Use `align-content: start` when the wrapped rows should stay together at the start. Do not assume wrapped items form a two-dimensional grid; if rows and columns must align, Grid is usually the better model.

```css
.tags {
  display: flex;
  flex-wrap: wrap;
  align-content: start;
  gap: .5rem;
  max-inline-size: 32rem;
}
```

### Intrinsic sizing and overflow

Flex items have an automatic minimum size that can prevent shrinking. Long URLs, code, and unbroken identifiers often need `min-inline-size: 0` on the item and `overflow-wrap: anywhere` on the content. This is one of the most important Flexbox overflow fixes.

```css
.media-row {
  display: flex;
  gap: 1rem;
}

.media-row__body {
  min-inline-size: 0;
}

.media-row__title {
  overflow-wrap: anywhere;
}
```

### A complete responsive Flexbox pattern

```html
<nav class="site-nav" aria-label="Primary">
  <a class="site-nav__brand" href="/">CSS Reference</a>
  <div class="site-nav__links">
    <a href="/chapters">Chapters</a>
    <a href="/examples">Examples</a>
    <a class="site-nav__cta" href="/download">Download</a>
  </div>
</nav>
```

```css
.site-nav {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
}

.site-nav__brand {
  font-weight: 700;
}

.site-nav__links {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem 1rem;
  margin-inline-start: auto;
}

@media (max-width: 36rem) {
  .site-nav__links {
    inline-size: 100%;
    margin-inline-start: 0;
  }
}
```

Wireframe:

```text
wide:  [CSS Reference]                 [Chapters] [Examples] [Download]
small: [CSS Reference]
       [Chapters] [Examples] [Download]
```

### A property-by-property reference

The most useful way to study Flexbox is to separate properties applied to the parent from properties applied to the direct children. This is also the organizing principle used by the CSS-Tricks guide: the parent establishes the flex formatting context and its axes; the children participate in sizing, ordering, and individual alignment. A declaration on the wrong element can be perfectly valid CSS and still have no effect.

#### Parent: `display`

`display: flex` creates a block-level flex container. `display: inline-flex` creates an inline-level flex container. In both cases, only the direct children become flex items; grandchildren remain in their normal formatting context unless the child is also made a flex container.

```css
.block-toolbar {
  display: flex;
}

.inline-toolbar {
  display: inline-flex;
}
```

Flex items are blockified, so a child’s `display: inline` does not preserve inline formatting inside the flex container. CSS multi-column properties do not turn a flex container into columns; choose Grid or multicolumn layout when that is the actual requirement.

#### Parent: `flex-direction`

`flex-direction` establishes the main axis and the direction in which items are placed: `row`, `row-reverse`, `column`, or `column-reverse`. `row` follows the inline direction, so its physical left-to-right result changes in right-to-left writing modes. Prefer logical language such as “main start” and “cross start” over assuming that the main axis is horizontal.

```css
.row { flex-direction: row; }
.reverse-row { flex-direction: row-reverse; }
.column { flex-direction: column; }
.reverse-column { flex-direction: column-reverse; }
```

`row-reverse` and `column-reverse` change visual order, not the order of nodes in the DOM. For a meaningful sequence, keep the source order correct and use direction only for presentation.

#### Parent: `flex-wrap` and `flex-flow`

The default `flex-wrap: nowrap` keeps all items on one line, which can produce overflow. `wrap` creates additional flex lines in the cross-axis direction; `wrap-reverse` reverses the cross-start direction. `flex-flow` is the shorthand for direction followed by wrapping.

```css
.toolbar {
  flex-flow: row wrap;
}

.vertical-list {
  flex-flow: column nowrap;
}
```

Flex lines are not independent two-dimensional grid rows. Each line distributes its own free space. If columns on separate lines must line up, use Grid instead.

#### Parent: `justify-content`

`justify-content` distributes free space along the main axis after flex items have been sized. Common values include `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, and `space-evenly`. The modern `start` and `end` values express logical alignment more directly; test them against the browser support policy when targeting older engines.

```css
.actions {
  display: flex;
  justify-content: space-between;
}
```

If the items consume all available space, there is nothing to distribute and several values appear identical. `justify-content` also cannot override an item’s intrinsic minimum size; fix sizing or overflow first.

#### Parent: `align-items`

`align-items` sets the default alignment of items along the cross axis. Useful values include `stretch`, `flex-start`, `flex-end`, `center`, and `baseline`. The initial `stretch` value makes items fill the cross size when their cross-axis size is `auto`, which explains why cards in a row can appear equal in height even when their content differs.

```css
.card-row {
  display: flex;
  align-items: stretch;
}

.icon-row {
  display: flex;
  align-items: center;
}

.text-row {
  display: flex;
  align-items: baseline;
}
```

`baseline` aligns the text baselines of the items rather than their border boxes. It is often the right choice for controls that combine different font sizes.

#### Parent: `align-content`

`align-content` distributes free space between or around multiple flex lines on the cross axis. It has no visible effect on a single-line flex container. The distinction is important: use `align-items` for items inside a line, and `align-content` for the lines as a group.

```css
.wrapped-palette {
  display: flex;
  flex-wrap: wrap;
  align-content: space-between;
  block-size: 14rem;
}
```

#### Parent: `gap`, `row-gap`, and `column-gap`

`gap` inserts consistent spacing between flex items and between flex lines. `row-gap` controls the cross-axis separation of wrapped lines, while `column-gap` controls the inline separation in a row-oriented layout. Unlike margins, gaps do not add space at the outer edges of the container.

```css
.filter-list {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1rem;
}
```

Use margins when an item intentionally owns its external spacing; use `gap` when the container owns the relationship between siblings.

#### Child: `order`

Every flex item has an order value of `0` by default. Items are sorted by that value and ties retain source order. Negative values are allowed. Because this can make the visual sequence differ from the reading and focus sequence, reserve `order` for decorative rearrangement or carefully tested responsive presentation.

```css
.summary { order: -1; }
.actions { order: 2; }
```

Do not use `order` to make a badly structured document appear correct. Screen readers and keyboard users may encounter the DOM order rather than the visual order.

#### Child: `flex-grow`

`flex-grow` is a unitless ratio for distributing positive free space. With values `1 1 1`, the remaining space is shared equally. With `1 2 1`, the middle item receives twice the share of the other items, subject to minimums and maximums.

```css
.sidebar { flex-grow: 1; }
.main { flex-grow: 2; }
```

Negative values are invalid. A grow factor does not mean “make this item twice as wide”; it means “give this item twice the share of the free space that remains after the flex base sizes are considered.”

#### Child: `flex-shrink`

`flex-shrink` distributes negative free space when the items’ base sizes are larger than the container. The default is `1`, so items can shrink. A value of `0` protects an item from this distribution, but it can cause overflow if the container cannot accommodate the protected size.

```css
.avatar {
  flex: 0 0 3rem;
}

.message {
  flex: 1 1 auto;
  min-inline-size: 0;
}
```

Shrink factors are weighted by the flex base size, so two items with the same shrink factor do not necessarily lose the same number of pixels.

#### Child: `flex-basis`

`flex-basis` sets the initial main size used before free space is distributed. It accepts a length, percentage, `auto`, or intrinsic sizing value such as `content` where supported. `auto` uses the corresponding `width` or `height` when one is provided; otherwise it uses the item’s content size.

```css
.result {
  flex-basis: 20rem;
}

.result--fluid {
  flex-basis: 0;
}
```

`flex-basis: 0` asks the algorithm to distribute space without giving the item’s content size a head start. This is why `flex: 1` is often used to create equal-width columns, although the exact shorthand expansion should be understood rather than guessed.

#### Child: `flex`

`flex` is the recommended shorthand for the three sizing components: grow, shrink, and basis. The common forms are `flex: none` (`0 0 auto`), `flex: auto` (`1 1 auto`), `flex: initial` (`0 1 auto`), and a positive number such as `flex: 1`.

```css
.fixed { flex: 0 0 12rem; }
.fluid { flex: 1 1 18rem; }
.equal { flex: 1; }
.intrinsic { flex: auto; }
```

Use the complete three-value form when the sizing contract matters. It makes clear whether the item can grow, can shrink, and what size it prefers before distribution.

#### Child: `align-self`

`align-self` overrides the parent’s `align-items` value for one item. `auto` means “use the parent’s value.” Other values include `stretch`, `flex-start`, `flex-end`, `center`, and `baseline`.

```css
.card__badge {
  align-self: flex-start;
}
```

`float`, `clear`, and `vertical-align` do not control a flex item’s placement. Remove those declarations when debugging a flex layout; they can distract from the properties that actually participate in the algorithm.

### The flex formatting algorithm, step by step

For difficult layouts, think of Flexbox as a constrained calculation rather than a collection of alignment tricks:

1. The container establishes its main and cross axes.
2. Items are collected into one or more flex lines according to `flex-wrap`.
3. Each item receives a flex base size from `flex-basis`, its main-size property, or its content.
4. The browser compares the base sizes with the available main-axis space.
5. Positive free space is distributed using grow factors; negative space is distributed using shrink factors.
6. Minimum and maximum sizes freeze items that cannot grow or shrink further.
7. The remaining space is aligned with `justify-content`.
8. Items and lines are aligned on the cross axis with `align-items`, `align-self`, and `align-content`.

```text
base sizes → available space → grow/shrink → min/max constraints → alignment
   12rem         40rem           ratios          clamp sizes          gaps
```

This model explains why changing `width` alone may not change the result: the width can become the basis, then be modified by flex factors, minimum sizes, and alignment.

### Common patterns from the guide, adapted for production

#### Center one item on both axes

```css
.empty-state {
  display: flex;
  min-block-size: 16rem;
  align-items: center;
  justify-content: center;
  text-align: center;
}
```

#### Push one item to the far edge

```css
.split-row {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.split-row__end {
  margin-inline-start: auto;
}
```

#### Equal-height cards with a bottom-aligned action

```css
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  display: flex;
  flex: 1 1 18rem;
  min-inline-size: 0;
  flex-direction: column;
}

.card__action {
  margin-block-start: auto;
}
```

The card becomes both a flex item in the list and a flex container for its internal content. This nested use is a strength of Flexbox: each component can establish a local one-dimensional layout without changing the parent’s layout model.

#### A media object that does not overflow

```css
.media {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.media__image {
  flex: 0 0 5rem;
  aspect-ratio: 1;
  object-fit: cover;
}

.media__content {
  min-inline-size: 0;
}
```

#### A full-width footer action on wrapped controls

```css
.form-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem;
}

.form-actions__primary {
  margin-inline-start: auto;
}

@media (max-width: 30rem) {
  .form-actions__primary {
    inline-size: 100%;
    margin-inline-start: 0;
  }
}
```

### Legacy syntax and prefixing

Older Flexbox implementations used incompatible syntaxes, including an early `-webkit-box` model and a 2012-era `-ms-flexbox` model. Do not write a new stylesheet around those models. If maintaining a legacy bundle, isolate the compatibility declarations, test the actual target browsers, and keep the modern unprefixed rules as the source of truth.

```css
/* Only retain these lines when a documented legacy target requires them. */
.legacy-toolbar {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
}
```

Autoprefixer can generate targeted compatibility declarations from a Browserslist configuration, but it cannot make every historical Flexbox behavior equivalent. Verify layout rather than assuming generated prefixes solve the old implementation’s algorithm differences.

### Flexbox checklist

- Choose the main axis before choosing alignment values.
- Use `gap` for spacing between items and lines.
- Use `flex-basis` to express the preferred size, not only `width`.
- Add `min-inline-size: 0` to shrinkable content columns.
- Keep source order semantic; treat `order` as a visual tool only.
- Switch to Grid when independent row and column alignment is required.
- Test wrapping, zoom, long content, keyboard focus, and right-to-left writing modes.

### Compatibility and source trail

- MDN Flexbox guide: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout
- MDN Flexbox properties: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- CSS-Tricks, “A Complete Guide to Flexbox”: https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS Flexbox: https://www.w3schools.com/css/css3_flexbox.asp
