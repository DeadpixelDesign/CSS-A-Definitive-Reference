# Grid and subgrid

CSS Grid is a two-dimensional layout system. It defines tracks in rows and columns, then places items into the resulting cells or areas. Grid is useful when alignment across both axes is part of the design contract: page shells, dashboards, card collections, editorial layouts, and forms.

### Explicit tracks and named lines

Use `grid-template-columns` and `grid-template-rows` to create explicit tracks. Named lines make placement self-documenting and support full-bleed layouts without unexplained magic numbers.

```css
.page {
  display: grid;
  grid-template-columns:
    [full-start] minmax(1rem, 1fr)
    [content-start] minmax(0, 72rem)
    [content-end] minmax(1rem, 1fr)
    [full-end];
}

.page__content {
  grid-column: content-start / content-end;
}

.page__hero {
  grid-column: full-start / full-end;
}
```

Wireframe:

```text
full-start                                      full-end
│  gutter  │          content track          │  gutter  │
└──────────┴─────────────────────────────────┴──────────┘
           content-start       content-end
```

### Repeat, `minmax()`, and responsive tracks

`repeat()` reduces repetition, `minmax()` expresses a lower and upper bound, and `auto-fit` or `auto-fill` controls how available tracks are created. `auto-fit` collapses empty tracks so existing items can expand; `auto-fill` preserves the potential tracks.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 1rem;
}
```

```text
wide:  [ card ][ card ][ card ][ card ]
mid:   [ card ][ card ][ card ]
narrow:[       card       ][       card       ]
```

### Placement, areas, and auto-placement

Use `grid-column`, `grid-row`, and their shorthands for direct placement. Named areas provide a visual map for stable page structures. `grid-auto-flow: dense` can fill earlier holes, but it may make visual order diverge from source order; use it only when that tradeoff is acceptable.

```css
.dashboard {
  display: grid;
  grid-template-areas:
    "header header"
    "nav    main"
    "footer footer";
  grid-template-columns: 14rem minmax(0, 1fr);
  gap: 1rem;
}

.dashboard__header { grid-area: header; }
.dashboard__nav { grid-area: nav; }
.dashboard__main { grid-area: main; }
.dashboard__footer { grid-area: footer; }
```

### Implicit tracks and auto sizing

Items placed outside the explicit grid create implicit tracks. Control them with `grid-auto-columns`, `grid-auto-rows`, and `grid-auto-flow`. Use `minmax(0, 1fr)` when a flexible track must be allowed to shrink below its content’s automatic minimum.

```css
.feed {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 18rem;
  grid-auto-rows: minmax(8rem, auto);
  grid-auto-flow: row;
  gap: 1rem;
}
```

### Alignment and gaps

`justify-items` and `align-items` align items within their cells. `justify-content` and `align-content` distribute the grid as a whole when there is extra space. `place-items`, `place-content`, and `place-self` are useful shorthands when their two-axis meaning remains clear.

```css
.tiles {
  display: grid;
  place-items: stretch;
  justify-content: center;
  gap: 1rem;
}
```

### Subgrid

`subgrid` lets a nested grid participate in the parent grid’s tracks. It is valuable for cards whose headings, descriptions, and actions must line up across a row even when each card has different content lengths. Subgrid can be used on rows, columns, or both.

```css
.product-list {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  grid-template-rows: auto 1fr auto;
  gap: 1rem;
}

.product-card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;
  gap: .75rem;
  padding: 1rem;
}
```

Wireframe of row subgrid:

```text
parent rows:  ───── heading ─────┼──── description ────┼──── action ────
card A:       [ title          ]  [ short copy       ]  [ button       ]
card B:       [ longer title   ]  [ longer copy      ]  [ button       ]
card C:       [ title          ]  [ medium copy      ]  [ button       ]
               aligned tracks shared by every card
```

### A property-by-property reference

Grid becomes easier to debug when its properties are divided into container properties and item properties. The container defines the tracks, gaps, auto-placement rules, and alignment defaults. A child then chooses its grid area, line spans, and individual alignment. This parent-versus-child structure is also the central organizing idea in the CSS-Tricks Grid guide.

#### Parent: `display`

`display: grid` creates a block-level grid container; `display: inline-grid` creates an inline-level grid container. Direct children become grid items, including anonymous boxes generated for text runs. A nested element is not automatically part of the ancestor’s grid: it must itself be a grid container or use `subgrid` on one of its axes.

```css
.page-grid { display: grid; }
.inline-grid { display: inline-grid; }
```

#### Parent: `grid-template-columns` and `grid-template-rows`

These properties define the explicit grid: a space-separated list of track sizes, optionally paired with line names in square brackets. Track sizes can use lengths, percentages, `auto`, intrinsic keywords, `minmax()`, `fit-content()`, and the flexible `fr` unit.

```css
.report {
  display: grid;
  grid-template-columns: [label] 12rem [data] minmax(0, 1fr);
  grid-template-rows: [header] auto [body] 1fr [footer] auto;
}
```

`fr` represents a share of leftover space after fixed and intrinsic tracks have been resolved. It is not the same as a percentage: a percentage can contribute to the container’s minimum size, while a fractional track participates in distributing free space.

#### Parent: `repeat()`, `minmax()`, and intrinsic sizing

`repeat()` generates repeated tracks. `minmax(min, max)` sets a lower and upper bound, while `min-content`, `max-content`, and `fit-content()` let content participate in track sizing.

```css
.catalog {
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
}
```

Use `minmax(0, 1fr)` for a flexible track that must shrink below a long child’s automatic minimum. Use `minmax(12rem, 1fr)` when each track should remain readable before sharing remaining space.

#### `auto-fit` versus `auto-fill`

Both keywords create as many tracks as fit. `auto-fill` preserves empty tracks when there are fewer items; `auto-fit` collapses empty tracks so occupied tracks can expand. The difference is visible when the container has spare room and only a few items.

```css
.fill-example {
  grid-template-columns: repeat(auto-fill, minmax(12rem, 1fr));
}

.fit-example {
  grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
}
```

Wireframe with two items in a wide container:

```text
auto-fill: [item][item][empty][empty]
auto-fit:  [item]       [item]       
            tracks collapse and occupied items grow
```

#### Parent: `grid-template-areas`

`grid-template-areas` is a text representation of the layout. Each quoted string describes a row; repeated names form a rectangular area; a period creates an empty cell. Every row must have the same number of cells, and each named area must form a rectangle.

```css
.application {
  display: grid;
  grid-template-columns: 15rem minmax(0, 1fr);
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header"
    "sidebar content"
    "footer footer";
}

.application__header { grid-area: header; }
.application__sidebar { grid-area: sidebar; }
.application__content { grid-area: content; }
.application__footer { grid-area: footer; }
```

The declaration itself acts as a wireframe:

```text
┌──────────────────────────────┐
│            header            │
├──────────────┬───────────────┤
│    sidebar    │    content    │
├──────────────┴───────────────┤
│            footer            │
└──────────────────────────────┘
```

Changing the areas at a breakpoint can rearrange the composition without changing the HTML order:

```css
@media (max-width: 42rem) {
  .application {
    grid-template-columns: 1fr;
    grid-template-areas:
      "header"
      "content"
      "sidebar"
      "footer";
  }
}
```

#### Parent: `grid-template` and `grid`

`grid-template` combines the explicit row tracks, column tracks, and areas. `grid` is a larger shorthand that can also set implicit track sizes and auto-flow. Shorthands reset omitted subproperties, so use longhands when preserving an existing implicit-grid configuration matters.

```css
.dashboard {
  grid-template:
    "header header" auto
    "nav main" 1fr
    "footer footer" auto
    / 14rem minmax(0, 1fr);
}
```

The slash separates row definitions from column definitions. Align multi-line shorthands so the visual structure remains readable to the next person maintaining the layout.

#### Parent: implicit tracks and `grid-auto-*`

The explicit grid is the structure you define. When auto-placement needs more rows or columns, the browser creates implicit tracks. `grid-auto-rows` and `grid-auto-columns` control their sizing; `grid-auto-flow` controls whether new items are placed by row or column.

```css
.timeline {
  display: grid;
  grid-template-columns: 8rem minmax(0, 1fr);
  grid-auto-rows: minmax(4rem, auto);
  grid-auto-flow: row;
  gap: 1rem;
}
```

`grid-auto-flow: dense` allows later smaller items to fill earlier holes. It can improve packing, but the visual sequence may no longer follow source order. Never use dense packing for a layout where spatial order communicates chronology or priority unless the result has been tested with keyboard and assistive technology.

#### Parent: `gap`, `row-gap`, and `column-gap`

`gap` inserts space between tracks without adding space around the outside of the grid. `row-gap` and `column-gap` control the two axes separately.

```css
.metric-grid {
  display: grid;
  row-gap: 1.5rem;
  column-gap: 1rem;
}
```

Use `gap` for track relationships and padding for the grid’s relationship to its container. This separation makes responsive changes easier to reason about.

#### Parent: `justify-items`, `align-items`, and `place-items`

These properties set the default alignment of grid items inside their individual grid areas. `justify-items` addresses the inline axis; `align-items` addresses the block axis; `place-items` is the two-value shorthand.

```css
.icon-grid {
  display: grid;
  place-items: center;
}
```

The default `stretch` behavior can make a child fill its grid area. Use `start`, `end`, `center`, or `baseline` when the item should retain its intrinsic size or align with text.

#### Parent: `justify-content`, `align-content`, and `place-content`

These properties align the entire grid inside its container when the grid is smaller than the available space. They do not align the contents of each cell. `justify-content` works in the inline axis; `align-content` works in the block axis.

```css
.compact-grid {
  display: grid;
  grid-template-columns: repeat(2, 12rem);
  justify-content: center;
  align-content: start;
  gap: 1rem;
}
```

When the grid tracks already fill the container, there is no extra space for these properties to distribute.

#### Child: `grid-column` and `grid-row`

These shorthands place an item between grid lines or make it span a number of tracks. A slash separates the start line from the end line. `span` counts tracks rather than naming an end line.

```css
.feature {
  grid-column: 1 / span 2;
  grid-row: 1 / 3;
}
```

Named lines make this more durable:

```css
.feature {
  grid-column: content-start / content-end;
}
```

Negative line numbers count from the end of the explicit grid. `grid-column: 1 / -1` is a useful full-width pattern, but named lines communicate intent better in a reusable component.

#### Child: `grid-area`

`grid-area` can refer to a named area or act as a four-part placement shorthand for row-start, column-start, row-end, and column-end.

```css
.notice {
  grid-area: sidebar;
}

.hero {
  grid-area: 1 / 1 / 3 / -1;
}
```

Prefer named areas for page-level compositions and line-based placement for reusable components that should not depend on an ancestor’s area vocabulary.

#### Child: `justify-self`, `align-self`, and `place-self`

These properties override the container’s item-alignment defaults for one grid item.

```css
.status-badge {
  justify-self: end;
  align-self: start;
}
```

`place-self` is the shorthand for `align-self` followed by `justify-self`. Keep the two values explicit when the component has different inline and block alignment requirements.

### Grid placement and overlapping layers

Grid items can occupy the same cells. This is useful for image overlays, badges, and hero content without absolute-positioning every element. Use `z-index` only after the placement is correct, and create stacking contexts intentionally when blending or clipping is involved.

```css
.hero {
  display: grid;
  isolation: isolate;
}

.hero > * {
  grid-area: 1 / 1;
}

.hero__image { z-index: -1; }
.hero__content { z-index: 1; }
```

Wireframe:

```text
same grid cell
┌─────────────────────────┐
│ image layer             │
│     ┌──────────────┐    │
│     │ content      │    │
│     └──────────────┘    │
└─────────────────────────┘
```

Ensure the content remains readable when the image fails, loads slowly, or is suppressed by a user preference.

### Grid versus Flexbox

Choose Grid when the layout has a two-dimensional relationship or when tracks must align across rows and columns. Choose Flexbox when the layout is fundamentally one-dimensional and items should distribute along one axis. They compose well: a Grid page can contain Flexbox toolbars, and a Flexbox card can contain a small nested Grid.

```css
.page { display: grid; }
.page__toolbar { display: flex; }
.page__card { display: grid; }
```

Do not force Grid to behave like a wrapping flex row or Flexbox to simulate shared column tracks with arbitrary widths. The shortest, clearest layout model is usually the most resilient.

### A complete responsive dashboard

```html
<section class="dashboard" aria-labelledby="dashboard-title">
  <header class="dashboard__header">
    <h2 id="dashboard-title">Team activity</h2>
  </header>
  <aside class="dashboard__sidebar">Filters</aside>
  <div class="dashboard__main">
    <article class="stat-card">Completed</article>
    <article class="stat-card">In review</article>
  </div>
</section>
```

```css
.dashboard {
  display: grid;
  grid-template:
    "header header" auto
    "sidebar main" 1fr
    / 15rem minmax(0, 1fr);
  min-block-size: 24rem;
  gap: 1rem;
}

.dashboard__header { grid-area: header; }
.dashboard__sidebar { grid-area: sidebar; }
.dashboard__main {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  align-content: start;
  gap: 1rem;
  min-inline-size: 0;
}

@media (max-width: 42rem) {
  .dashboard {
    grid-template:
      "header" auto
      "main" auto
      "sidebar" auto
      / 1fr;
  }
}
```

### Subgrid in depth

Subgrid does not create a fresh set of independent tracks. It borrows the relevant tracks from the parent grid so descendants can align with siblings outside their own subtree. The nested grid can still add its own tracks on the other axis.

```css
.results {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  grid-template-rows: auto 1fr auto;
}

.result-card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;
}
```

Use subgrid when alignment is a real requirement, not merely because it is available. A component should retain a sensible fallback when the target support policy includes browsers without the feature:

```css
.result-card {
  display: grid;
  gap: .75rem;
}

@supports (grid-template-rows: subgrid) {
  .result-card {
    grid-row: span 3;
    grid-template-rows: subgrid;
  }
}
```

The fallback is still a valid card; it simply does not align its internal rows with its siblings.

### Grid sizing pitfalls

Watch for automatic minimum sizes, overflowing long content, percentage tracks in indefinite containers, and `1fr` tracks that refuse to shrink because their minimum is `auto`. Use `minmax(0, 1fr)`, `min-inline-size: 0`, and explicit container constraints when the content contract permits it.

### Grid checklist

- Choose Grid when rows and columns both matter.
- Name lines or areas when placement is part of the design language.
- Use `minmax()` and `repeat()` to encode responsive constraints.
- Use `subgrid` to align nested content with parent tracks.
- Keep source order meaningful even when areas change visual placement.
- Test implicit tracks, long content, zoom, and writing modes.

### Compatibility and source trail

- MDN CSS Grid layout: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout
- MDN `subgrid`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/subgrid
- CSS-Tricks, “A Complete Guide to CSS Grid”: https://css-tricks.com/complete-guide-css-grid-layout/
- web.dev Learn CSS Grid: https://web.dev/learn/css/grid
- W3Schools CSS Grid: https://www.w3schools.com/css/css_grid.asp
