# Grid lanes and masonry layout

Grid Lanes is the emerging CSS Grid Layout Module Level 3 layout model for masonry-style interfaces. A grid-lanes container keeps regular grid tracks in one axis and packs items into the shortest available lane in the other axis. This is the layout model behind waterfall and Pinterest-style galleries.

This feature is experimental and not a baseline CSS layout primitive. Current references use `display: grid-lanes` and `display: inline-grid-lanes`; earlier proposals used `display: masonry` or a `masonry` value on a Grid template axis. Do not mix those generations of syntax in production code. Treat Grid Lanes as an enhancement with a complete fallback, not as the only way to present content.

### The current Grid Lanes syntax

For a column waterfall, use `display: grid-lanes` and define the columns with `grid-template-columns`. The columns are the strict grid axis; items then pack vertically into the lane with the most available space.

```css
.masonry-gallery {
  display: grid;
  display: grid-lanes;
  grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
  gap: 1rem;
}
```

Wireframe representation:

```text
defined lanes       packed items choose the shortest lane
┌────────┬────────┬────────┐
│   A    │   B    │   C    │
│        ├────────┤        │
│        │   D    │        │
├────────┤        ├────────┤
│   E    │        │   F    │
└────────┴────────┴────────┘
```

The masonry axis is not a normal list of equal-height rows. Items are placed in source order across lanes, then packed according to the current lane lengths. This can reduce gaps, but it creates an important relationship between visual placement and reading order.

### Tracks, spans, and placement

The masonry direction still uses Grid’s track vocabulary. Define columns with fixed sizes, flexible sizes, `minmax()`, named lines, or `repeat()`. Regular grid placement and spans can be used in the grid axis, while the masonry axis packs items.

```css
.portfolio {
  display: grid;
  display: grid-lanes;
  grid-template-columns:
    [rail-start] 12rem
    [content-start] repeat(3, minmax(12rem, 1fr))
    [content-end] 12rem
    [rail-end];
  gap: 1.25rem;
}

.portfolio__feature {
  grid-column: content-start / span 2;
}
```

### Fallback with CSS columns

If the content is primarily a reading gallery and exact row alignment is not required, multi-column layout is a no-JavaScript fallback. It packs content vertically, so the visual order differs from a row-major grid. Make that tradeoff explicit and avoid it when users expect left-to-right sequence.

```css
.gallery {
  columns: 14rem;
  column-gap: 1rem;
}

.gallery > article {
  break-inside: avoid;
  margin-block-end: 1rem;
}
```

### Fallback with Flexbox

Flexbox can create a responsive row layout with wrapping. It does not provide true shortest-column masonry, but it preserves normal document order and has strong browser support.

```css
.gallery {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  gap: 1rem;
}

.gallery > article {
  flex: 1 1 14rem;
}
```

### A targeted polyfill alternative

For projects that need a masonry-like result before native support is appropriate, a small polyfill can detect `display: grid-lanes` support and adjust placement or margins. Examples include `masonry-pf` and `@prof-dev/masonry`; audit their maintenance, license, resize behavior, accessibility consequences, and performance before adopting one. A polyfill cannot reproduce every browser layout detail, and it may require JavaScript after images load or content changes.

```js
import { registerMasonry } from 'masonry-pf';

const gallery = document.querySelector('.masonry-gallery');
if (gallery && !CSS.supports('display', 'grid-lanes')) {
  registerMasonry(gallery);
}
```

Treat this as a progressive enhancement. The HTML must remain readable if JavaScript is disabled, delayed, or fails.

### Masonry.js as a library alternative

Masonry.js is a popular JavaScript grid-layout library from Desandro. It places items based on available vertical space and can be used when a project needs mature controls, callbacks, image-loading coordination, or broad support beyond experimental CSS. It is a library, not a CSS polyfill, so account for script cost, layout shifts, resize handling, and the relationship between DOM order and visual order.

```html
<div class="js-masonry-grid">
  <article class="grid-item">First card</article>
  <article class="grid-item">Second card</article>
  <article class="grid-item">Third card</article>
</div>
<script type="module">
  import Masonry from 'masonry-layout';

  const grid = document.querySelector('.js-masonry-grid');
  if (grid) {
    new Masonry(grid, {
      itemSelector: '.grid-item',
      columnWidth: '.grid-item',
      percentPosition: true,
    });
  }
</script>
```

Use `imagesLoaded` or an equivalent strategy when image dimensions are not known before layout. Reserve image space with `width`/`height` attributes or `aspect-ratio` to reduce shifts.

### A property-by-property reference

Grid Lanes keeps much of Grid’s track vocabulary, but changes how the non-grid axis is filled. The most useful mental model is “one strict axis plus one packing axis.” Define lanes with the template property for the strict axis, then let the browser place items into the lane that is currently shortest or most available.

#### Container: `display`

`display: grid-lanes` creates a block-level Grid Lanes container. `display: inline-grid-lanes` creates an inline-level container. The fallback should come before the experimental value because browsers ignore an unknown `display` value and retain the previous declaration.

```css
.gallery {
  display: grid;
  display: grid-lanes;
}

.inline-gallery {
  display: inline-grid;
  display: inline-grid-lanes;
}
```

This declaration order is a deliberate progressive-enhancement pattern. A browser that understands only `grid` uses a regular grid; a browser that understands Grid Lanes replaces it with the packing layout.

#### Column lanes: `grid-template-columns`

Defining columns creates the common vertical waterfall: the columns are the grid axis and the rows are packed. Each new item is considered in source order and placed where it best advances toward the top of the layout.

```css
.photo-wall {
  display: grid;
  display: grid-lanes;
  grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr));
  gap: 1rem;
}
```

Wireframe:

```text
HTML order:  1 → 2 → 3 → 4 → 5 → 6

lane 1       lane 2       lane 3
┌───────┐    ┌───────┐    ┌───────┐
│   1   │    │   2   │    │   3   │
│       │    ├───────┤    │       │
│       │    │   4   │    │       │
├───────┤    └───────┘    ├───────┤
│   5   │                 │   6   │
└───────┘                 └───────┘
```

The visual position is not a new DOM order. Keep the markup order meaningful, especially for article lists, search results, and interactive cards.

#### Row lanes: `grid-template-rows`

Defining rows creates a horizontal brick layout: rows are the grid axis and items pack across the inline direction. This is useful for interfaces where the horizontal bands are the stable structure and each item has a variable inline size.

```css
.brick-wall {
  display: grid;
  display: grid-lanes;
  grid-template-rows: repeat(3, 8rem);
  gap: 1rem;
}
```

With columns, items pack toward the block-start edge of the shortest column. With rows, they pack toward the inline-start edge of the shortest row. Choose the axis that matches the reading direction and the visual rhythm of the design.

#### Lane sizing values

Grid Lanes uses Grid’s track sizing language. The following values are particularly useful:

- `fr` shares available space proportionally, such as `1fr 2fr 1fr`.
- Fixed lengths such as `12rem`, `20ch`, or `240px` establish predictable lane widths.
- Percentages describe a fraction of the container, but they do not account for gaps as naturally as fractional tracks.
- `auto` sizes from content and can stretch when extra space is available.
- `min-content` chooses the narrowest size that avoids content overflow.
- `max-content` chooses the size required to keep content on one line where possible.
- `fit-content()` provides a content-sized track with a ceiling.
- `minmax()` expresses a lower and upper constraint and is the usual responsive choice.

```css
.mixed-lanes {
  display: grid-lanes;
  grid-template-columns:
    minmax(8rem, 1fr)
    minmax(16rem, 2fr)
    minmax(8rem, 1fr);
}
```

Use `minmax(min(100%, 15rem), 1fr)` when a single lane must remain usable on a narrow viewport without forcing horizontal scrolling.

#### `repeat()`, `auto-fill`, and `auto-fit`

`repeat()` expresses a track pattern without manually listing every lane. `auto-fill` creates every track that can fit, including empty potential tracks. `auto-fit` collapses empty tracks so the lanes containing items can expand.

```css
.responsive-lanes {
  display: grid-lanes;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  gap: 1rem;
}
```

This is one of the most important Grid Lanes patterns because the number of lanes changes with available space without a sequence of viewport breakpoints or container queries. The minimum must be constrained with `min()` if the component can become narrower than the preferred lane width.

#### `gap`, `row-gap`, and `column-gap`

`gap` applies between lanes and between packed items within a lane. `column-gap` is most visible in a column waterfall; `row-gap` controls the separation between items stacked in those columns. In a row-based brick layout, the visual roles reverse.

```css
.gallery {
  gap: 1rem;
  column-gap: clamp(.5rem, 2vw, 1.5rem);
  row-gap: 1rem;
}
```

The gap is part of the packing calculation. Keep it consistent unless the design deliberately distinguishes lane separation from item separation.

#### `flow-tolerance`

`flow-tolerance` is an emerging Grid Lanes control for deciding how much difference between lane lengths can be treated as a tie. A tolerance can keep source order visually closer when two lanes are nearly equal, reducing surprising jumps between columns. Because it is new, feature-query it and provide a sensible default.

```css
.gallery {
  display: grid;
  display: grid-lanes;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: 1rem;
}

@supports (flow-tolerance: 1em) {
  .gallery {
    flow-tolerance: 1em;
  }
}
```

Do not use tolerance to promise a fixed visual order. The layout still packs items according to available lane space, and a browser’s implementation may evolve while the feature is experimental.

#### Spanning lanes

Because Grid Lanes retains Grid placement on the grid axis, an item can span multiple lanes. The remaining auto-placed items are packed around it.

```css
.news-grid {
  display: grid;
  display: grid-lanes;
  grid-template-columns: repeat(auto-fill, minmax(18ch, 1fr));
  gap: 1.5rem;
}

.news-grid__lead {
  grid-column: span 3;
}

@media (max-width: 48rem) {
  .news-grid__lead {
    grid-column: span 2;
  }
}
```

Use a span only when the item’s prominence is part of the design. A very large span can dominate the lane packing and create a less predictable sequence for the items that follow.

#### Explicit placement

Items with definite placement on the grid axis are placed before the remaining auto-placement algorithm runs. This makes it possible to reserve a lane range for a masthead, a featured card, or a persistent sidebar.

```css
.museum {
  display: grid;
  display: grid-lanes;
  grid-template-columns: repeat(8, minmax(10rem, 1fr));
  gap: 1rem;
}

.museum__intro {
  grid-column: 7 / 9;
}
```

Combine explicit placement with responsive line counts carefully. A placement such as `7 / 9` assumes at least eight columns; use a media query or named layout variant when fewer lanes are possible.

### Waterfall, brick, and traditional Grid compared

These three models solve different problems:

```text
regular Grid:     fixed rows and columns; gaps may remain under short items
Grid Lanes:       fixed columns OR rows; the other axis packs to reduce gaps
CSS columns:      vertical packing; visual order can run top-to-bottom per column
```

Grid Lanes is a good fit for independent cards, photos, recipes, and search results where item heights vary. Regular Grid is better when row alignment conveys relationships. CSS columns remain a useful fallback when a pure-CSS packed appearance matters more than row-major reading order.

### Content, images, and layout stability

Grid Lanes reduces the need for JavaScript measurement, but content still needs stable sizing practices. Give images intrinsic `width` and `height` attributes or an `aspect-ratio`, use `object-fit` when cropping is acceptable, and do not allow late-loading media to change the meaning of the content order.

```html
<figure class="photo-card">
  <img src="lake.jpg" width="1200" height="900" alt="A lake at sunrise">
  <figcaption>Morning light over the lake</figcaption>
</figure>
```

```css
.photo-card {
  margin: 0;
  overflow: clip;
  border-radius: .75rem;
}

.photo-card img {
  display: block;
  inline-size: 100%;
  block-size: auto;
}
```

Unlike a JavaScript Masonry library that often needs to wait for images before measuring, native layout can continuously participate in sizing. That is not a reason to omit intrinsic dimensions: reserving space still improves loading stability, accessibility, and performance.

### Source order, tab order, and lazy loading

Grid Lanes is designed to preserve a row-major or lane-aware tab sequence better than a CSS-columns fallback. The browser can place each item in the lane that advances it furthest while the DOM remains the source of truth. Test this behavior with the actual browser implementation and with the interactive “play tab order” controls in the Grid Lanes field guide.

Infinite scrolling can be paired with Grid Lanes without a layout library measuring every card. Still, use semantic pagination or an accessible “Load more” control, preserve focus when new items are appended, and announce loading state to assistive technology. A layout feature does not solve the interaction design of an infinite feed.

### Responsive patterns

#### Equal flexible lanes

```css
.equal-gallery {
  display: grid;
  display: grid-lanes;
  grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
  gap: 1rem;
}
```

#### Alternating narrow and wide lanes

```css
.alternating-gallery {
  display: grid;
  display: grid-lanes;
  grid-template-columns:
    repeat(auto-fill, minmax(8rem, 1fr) minmax(16rem, 2fr))
    minmax(8rem, 1fr);
  gap: 1rem;
}
```

#### Sidebar and main content

```css
.lane-page {
  display: grid;
  display: grid-lanes;
  grid-template-columns: 14rem minmax(0, 1fr);
  gap: 2rem;
}

.lane-page__main {
  display: grid;
  display: grid-lanes;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: 1rem;
}
```

If the sidebar should not participate in packing, keep it as a separately placed grid item and apply Grid Lanes only to the content collection. One container should have one clear packing responsibility.

### Accessibility and source order

Masonry creates an especially important accessibility constraint: visual proximity can differ from DOM order. Keep the DOM order logical, make each item independently reachable by keyboard, avoid using absolute positioning to rewrite the reading sequence, and test with keyboard navigation, screen readers, zoom, and reduced motion. If the visual arrangement becomes confusing when linearized, choose Flexbox or a regular Grid fallback.

### Compatibility policy

Use a feature query for the exact masonry syntax and retain the fallback outside the query. Do not treat experimental browser flags as production support. Recheck the working draft, implementation notes, and target-browser data before shipping.

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: 1rem;
}

@supports (display: grid-lanes) {
  .gallery {
    display: grid-lanes;
  }
}
```

### Compatibility and source trail

- W3C CSS Grid Layout Module Level 3 working draft: https://www.w3.org/TR/css-grid-3/
- MDN Grid lanes layout: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_lanes
- WebKit, “Introducing CSS Grid Lanes”: https://webkit.org/blog/17660/introducing-css-grid-lanes/
- The Field Guide to CSS Grid Lanes: https://gridlanes.webkit.org/
- Modern CSS, “CSS Grid Lanes: Masonry Layout Without JavaScript”: https://modern-css.com/css-grid-lanes/
- Masonry.js documentation: https://masonry.desandro.com/
- `masonry-pf` polyfill: https://github.com/Sam-Apostel/masonry-pf
- `@prof-dev/masonry` polyfill: https://www.npmjs.com/package/@prof-dev/masonry
- MDN CSS Grid layout: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout
