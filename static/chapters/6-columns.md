# Columns

CSS multi-column layout, often called multicol, divides one continuous stream of content into newspaper-style columns. It is a text-flow layout: content fills the first column, continues in the next column, and so on. This makes it fundamentally different from Grid, which aligns independent items in rows and columns, and from Flexbox, which distributes items along one axis.

Use Columns for long-form reading, glossaries, footnotes, print-oriented material, indexes, and compact lists where a continuous reading stream is the goal. Do not use it for dashboards, card grids, or navigation when each item needs a stable addressable row and column.

### The mental model: one stream, many fragmentainers

When an element becomes a multi-column container, the browser creates anonymous column boxes. The children are not assigned to “column 1” or “column 2” by ordinary placement rules. Instead, the content is fragmented and flows from one column box to the next.

```css
.article-body {
  column-width: 18rem;
  column-gap: 2rem;
}
```

Wireframe:

```text
one continuous stream of content
              ↓ fragmentation
┌──────────────────┐  gap  ┌──────────────────┐  gap  ┌──────────────────┐
│ paragraph 1      │       │ continuation     │       │ conclusion       │
│ paragraph 2      │       │ paragraph 4      │       │ paragraph 7      │
│ paragraph 3      │       │ paragraph 5      │       │ paragraph 8      │
└──────────────────┘       └──────────────────┘       └──────────────────┘
```

The visual columns are anonymous. CSS does not provide a general selector that targets “the second column” as if it were a normal element. If individual cards need independent placement, use Grid or Flexbox.

### Creating columns with `column-count`

`column-count` expresses a preferred number of columns. The browser calculates the column width from the available inline size, the requested count, and the gap.

```css
.terms {
  column-count: 3;
  column-gap: 2rem;
}
```

This is useful when the number of columns is part of the editorial design. It is less useful when the component can appear in containers of unpredictable width, because a fixed count can make columns too narrow on small screens.

```css
@media (max-width: 48rem) {
  .terms {
    column-count: 2;
  }
}

@media (max-width: 32rem) {
  .terms {
    column-count: 1;
  }
}
```

### Creating columns with `column-width`

`column-width` expresses a preferred minimum width for each column. The browser creates as many columns as fit. This is usually the most fluid choice for responsive prose.

```css
.reading-copy {
  column-width: 20rem;
  column-gap: clamp(1rem, 3vw, 3rem);
}
```

The declared width is a preference, not necessarily the used width. If the container is wide enough for four columns, the browser may create four; if it is only wide enough for one, it creates one. The result adapts without a breakpoint for every possible viewport.

### The `columns` shorthand

`columns` combines `column-width` and `column-count`. The order is flexible because one value can be recognized as a count and the other as a width, but explicit longhands are often easier to review.

```css
.handbook {
  columns: 18rem 3;
}
```

This means “prefer columns about 18rem wide, with at most three columns.” If both a width and count are specified, `column-count` acts as a maximum while `column-width` acts as the preferred minimum. The browser chooses the combination that fits the container.

```css
.handbook {
  columns: minmax(16rem, 24rem) 4; /* not valid: minmax() is Grid syntax */
}
```

Do not use Grid’s `minmax()` grammar in `columns`. For multicol, use a plain `column-width`, a count, or a responsive wrapper that controls the available width.

### `column-gap` and `column-rule`

`column-gap` controls the space between column boxes. `column-rule` paints a divider in that gap; it is shorthand for `column-rule-width`, `column-rule-style`, and `column-rule-color`.

```css
.essay {
  column-width: 19rem;
  column-gap: 2.5rem;
  column-rule: 1px solid var(--line);
}
```

The rule does not consume an additional track-sized width. It is painted in the gap, so increase the gap if the text feels too close to the divider.

```css
.essay {
  column-rule-width: .1rem;
  column-rule-style: solid;
  column-rule-color: color-mix(in srgb, currentColor 25%, transparent);
}
```

Use a rule sparingly. A divider on every column can create visual noise, especially in narrow reading measures or high-contrast modes.

### Balancing and sequential filling with `column-fill`

`column-fill` controls how content is distributed. `balance` attempts to keep the columns similar in height; `auto` fills one column before moving to the next. `auto` requires a constrained block size to be consistently observable across engines.

```css
.balanced-index {
  columns: 16rem 3;
  column-fill: balance;
}

.sequential-log {
  columns: 16rem 3;
  block-size: 32rem;
  column-fill: auto;
}
```

Balanced columns suit articles and reference indexes. Sequential filling suits timelines, logs, or content where the vertical extent is intentionally fixed. Always test `column-fill: auto` in the browsers and print engines that matter to the project.

### Spanning headings with `column-span`

`column-span: all` makes a block-level element span across every column. It is useful for a title, section heading, or callout that should introduce the entire row of columns. The property currently has a deliberately small conceptual model: an element either remains in the normal column flow or spans all columns.

```html
<article class="feature-article">
  <h1>Designing with constraint</h1>
  <p>Content begins below the heading and flows through the columns.</p>
  <p>More continuous reading content follows.</p>
</article>
```

```css
.feature-article {
  column-width: 19rem;
  column-gap: 2rem;
}

.feature-article > h1 {
  column-span: all;
  margin-block: 0 1.5rem;
}
```

The content before and after a spanner can be laid out in different column fragments. Give the spanner clear margins and test backgrounds, borders, and nested wrappers so the transition does not look like a misplaced block.

### Controlling breaks with the Fragmentation properties

Columns are fragmentainers, like pages in printed media. A heading at the bottom of a column, or a figure separated from its caption, creates a poor reading experience. Use the modern `break-*` properties to influence where content fragments.

```css
.article-section {
  break-inside: avoid;
}

.article-section h2 {
  break-after: avoid-column;
}

.article-section + .article-section {
  break-before: avoid-column;
}
```

Useful values include:

- `break-inside: avoid` to keep a box together when possible.
- `break-inside: avoid-column` to specifically avoid a column break.
- `break-before: column` to force a new column before an element.
- `break-after: column` to force a new column after an element.
- `auto` to allow the browser to choose.

Avoid values are requests, not guarantees. If a single figure is taller than a column, the browser must fragment or overflow it. Excessive `avoid` declarations can create large empty areas or force unexpected overflow.

```css
figure {
  margin: 0;
  break-inside: avoid;
}

figure img {
  display: block;
  max-inline-size: 100%;
  block-size: auto;
}

section h2 {
  break-before: avoid-column;
  break-after: avoid-column;
}
```

### Keep figures, captions, and code examples together

Multicol layouts are especially useful for editorial content, but editorial components should not be allowed to fragment arbitrarily.

```html
<figure class="column-figure">
  <pre><code>display: grid;</code></pre>
  <figcaption>The declaration creates a grid formatting context.</figcaption>
</figure>
```

```css
.column-figure {
  break-inside: avoid;
  margin: 0 0 1rem;
}

.column-figure pre {
  max-inline-size: 100%;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
}
```

For very large code blocks, keeping the entire block together may be impossible. In that case, provide a download or linked source and allow a controlled break rather than letting the text overflow outside the page.

### Responsive reading measures

A comfortable line length is a content constraint, not simply a fixed device breakpoint. Multicol lets the browser choose a column count based on the available width, but the container still needs a readable maximum.

```css
.documentation {
  inline-size: min(100%, 76rem);
  margin-inline: auto;
  padding-inline: clamp(1rem, 4vw, 3rem);
  column-width: 22rem;
  column-gap: clamp(1.25rem, 3vw, 3rem);
}
```

On a narrow screen, the layout becomes one column naturally. If a component is nested inside a narrow card, the column width calculation responds to the card’s available space rather than the viewport.

### Columns and writing modes

Multicol follows the writing mode of its container. In horizontal writing, columns commonly progress across the inline axis while content flows down the block axis. In vertical writing modes, the physical orientation changes. Test `writing-mode`, `direction`, and `text-orientation` if the component supports international layouts.

```css
.vertical-essay {
  writing-mode: vertical-rl;
  column-width: 20rem;
  column-gap: 2rem;
}
```

Prefer logical properties such as `inline-size`, `block-size`, `margin-block`, and `padding-inline` around the multicol container. Do not assume that “left column” or “top of the page” describes every writing system.

### Columns versus Grid, Flexbox, and Grid Lanes

Choose based on the content relationship:

```text
Columns:    one content stream → fragmented text columns
Flexbox:    one axis → items distribute or wrap
Grid:       two axes → rows and columns align
Grid Lanes: one strict axis → the other axis packs variable items
```

Use Columns for paragraphs that should continue from one column to the next. Use Grid for independently addressable cards that need row alignment. Use Flexbox for a toolbar or a row of controls. Use Grid Lanes for variable-height items that should pack into lanes without a JavaScript measurement pass.

### Print and paged media

Columns are closely related to printing because both columns and pages fragment content. A print stylesheet can use multicol for indexes, glossaries, or compact reference material, but avoid forcing a screen-oriented component into columns merely to reduce page count.

```css
@media print {
  .reference-index {
    column-count: 2;
    column-gap: 2rem;
    column-fill: balance;
  }

  .reference-index a {
    color: inherit;
    text-decoration: none;
  }
}
```

Test print previews and generated PDFs. A forced break, an oversized heading, or a `break-inside: avoid` figure can move more content than expected when the available fragmentainer height changes.

### Accessibility and user control

Multiple columns can make reading and keyboard navigation harder when the column height is too tall or the content order is not obvious. Avoid narrow columns with tiny type, avoid fixed heights unless necessary, and respect zoom and text enlargement. WCAG guidance warns against layouts that require excessive horizontal scanning or become unusable when text is enlarged.

```css
.long-form {
  column-width: min(22rem, 100%);
  font-size: 1rem;
  line-height: 1.6;
}

@media (prefers-reduced-motion: reduce) {
  .long-form {
    scroll-behavior: auto;
  }
}
```

Do not use columns to hide content, create an inaccessible horizontal reading carousel, or force a user to jump between columns to complete a form. For interactive content, regular block flow or Grid is usually clearer.

### A complete editorial pattern

```html
<article class="chapter-copy">
  <h1>How the cascade makes decisions</h1>
  <p class="dek">A short introduction remains visible before the reading stream begins.</p>
  <section>
    <h2>Start with the selector</h2>
    <p>The browser first determines which elements match.</p>
  </section>
  <figure>
    <pre><code>.card { color: navy; }</code></pre>
    <figcaption>A declaration belongs to a rule.</figcaption>
  </figure>
  <section>
    <h2>Then resolve the cascade</h2>
    <p>Declarations compete according to origin, layer, specificity, and order.</p>
  </section>
</article>
```

```css
.chapter-copy {
  max-inline-size: 78rem;
  margin-inline: auto;
  column-width: 22rem;
  column-gap: clamp(1.5rem, 4vw, 3.5rem);
}

.chapter-copy > h1,
.chapter-copy > .dek {
  column-span: all;
}

.chapter-copy h1 {
  margin-block: 0 .5rem;
}

.chapter-copy .dek {
  max-inline-size: 48rem;
  margin-block: 0 2rem;
}

.chapter-copy section,
.chapter-copy figure {
  break-inside: avoid;
}

@media (max-width: 42rem) {
  .chapter-copy {
    column-width: auto;
    columns: 1;
  }
}
```

### Compatibility and source trail

- MDN CSS multi-column layout: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout
- MDN using multi-column layouts: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Using
- MDN handling content breaks: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Handling_content_breaks
- MDN column layouts cookbook: https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Column_layouts
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS columns: https://www.w3schools.com/css/css3_multiple_columns.asp
