# Motion and scroll-driven interfaces

Motion should explain state changes, preserve continuity, and never block use. Animate transform and opacity when possible, keep durations proportional to distance, and respect `prefers-reduced-motion`.

### Transitions

Transition only the properties that should change. `transition: all` makes future changes animate unexpectedly and can create performance or accessibility problems. For entry and exit, make the static state useful even if the animation is skipped.

### Keyframes

Name animations by meaning, not by appearance: `dialog-enter`, `progress-indeterminate`, `toast-exit`. Consider fill modes and cancellation behavior. Do not communicate success, error, or urgency by motion alone.

### Scroll-driven animation

Scroll-driven timelines are best for decorative progress, parallax, and reveal effects. Essential content must remain available without the timeline. Test nested scroll containers and reduced motion.

### Motion starts with a state model

Before writing a transition or animation, identify the states a component can occupy: idle, hovered, focused, pressed, expanded, entered, exiting, disabled, and reduced-motion. CSS should make each state understandable without movement. Motion then communicates the change between states rather than becoming the only signal.

```css
.disclosure__panel {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition:
    grid-template-rows 240ms ease,
    opacity 160ms ease;
}

.disclosure[data-open='true'] .disclosure__panel {
  grid-template-rows: 1fr;
  opacity: 1;
}

.disclosure__panel > div {
  min-block-size: 0;
  overflow: hidden;
}
```

The open state is represented by a data attribute, not by `:hover`, so it can be controlled by a button and remain available to keyboard and assistive-technology users. The static open and closed states should both be usable if transitions are disabled.

### Transitions in detail

The `transition` shorthand combines a property, duration, timing function, delay, and optional behavior. Prefer a property allowlist over `transition: all`; an allowlist documents what is intended to move and prevents unrelated future changes from animating.

```css
.button {
  background: var(--blue);
  color: white;
  transform: translateY(0);
  transition:
    background-color 160ms ease,
    transform 160ms ease,
    box-shadow 160ms ease;
}

.button:hover,
.button:focus-visible {
  background: color-mix(in srgb, var(--blue), black 12%);
  transform: translateY(-2px);
  box-shadow: 0 .5rem 1rem rgb(20 33 61 / .18);
}
```

Use `transition-property`, `transition-duration`, `transition-timing-function`, and `transition-delay` longhands when a component has different timings for different state changes. A delay can make a hover interaction feel unresponsive, so use it sparingly.

### Timing functions and motion quality

`ease` is a reasonable default for small UI changes, but motion often benefits from a deliberate curve. Use `linear()` for progress-like movement, `steps()` for discrete frames, and `cubic-bezier()` for a custom curve. A spring-like effect can be approximated with an overshooting cubic Bézier, but avoid overshoot for controls that must feel precise.

```css
:root {
  --ease-standard: cubic-bezier(.2, .8, .2, 1);
  --ease-emphasized: cubic-bezier(.2, 1.4, .4, 1);
}

.toast {
  transition: transform 320ms var(--ease-standard);
}

.toast--emphasis {
  transition-timing-function: var(--ease-emphasized);
}
```

Keep duration proportional to the distance and complexity of the change. A tooltip usually needs a short fade; a page-level navigation transition can justify a longer, staged sequence. Avoid making users wait for decorative motion before they can interact.

### Transforms and transform origins

Transforms change the visual position and shape without changing normal-flow geometry. `translate`, `scale`, `rotate`, and `skew` are useful for motion; `transform-origin` chooses the point around which scale and rotation occur. Transforms can create stacking contexts and affect hit testing, so inspect the result rather than treating them as purely cosmetic.

```css
.menu-icon {
  transform-origin: center;
  transition: rotate 180ms ease;
}

.menu[data-open='true'] .menu-icon {
  rotate: 45deg;
}
```

Prefer logical positioning and layout for the final geometry. Use transforms for the transition between geometries, not as a substitute for a layout model that must respond to content.

### Keyframes and animation shorthand

Keyframes describe a named sequence of styles. The `animation` shorthand controls the name, duration, timing, delay, iteration count, direction, fill mode, and play state. Give animations semantic names such as `dialog-enter` or `progress-indeterminate`, not names tied to an incidental visual detail.

```css
@keyframes dialog-enter {
  from {
    opacity: 0;
    scale: .96;
    translate: 0 .75rem;
  }
  to {
    opacity: 1;
    scale: 1;
    translate: 0 0;
  }
}

.dialog[open] {
  animation: dialog-enter 220ms var(--ease-standard) both;
}
```

`animation-fill-mode: both` applies the first keyframe during the delay and the last keyframe after the animation completes. This is convenient for entry animations, but the resting style should still be declared outside the animation so the component remains understandable when animation is disabled.

```css
.spinner {
  animation:
    spinner-rotate 900ms linear infinite;
}

@keyframes spinner-rotate {
  to { rotate: 1turn; }
}
```

Use `animation-iteration-count: infinite` only for ongoing status or ambient decoration. A looping animation must not be the only way a user discovers that work is in progress.

### Animation controls and cancellation

`animation-play-state` can pause and resume a CSS animation, while the Web Animations API can expose imperative controls. A component should have a clear cancellation or completion state when motion is interrupted by navigation, a preference change, or a component unmount.

```css
.marquee {
  animation: marquee-scroll 18s linear infinite;
}

.marquee:hover,
.marquee:focus-within {
  animation-play-state: paused;
}
```

Pausing on hover is not enough for touch or keyboard users. Provide an explicit pause control for long-running or attention-demanding motion.

### The Web Animations API

JavaScript is useful when an animation must be coordinated with application state, measured geometry, a promise, or a user gesture. The Web Animations API provides `element.animate()` without requiring a third-party library.

```js
const panel = document.querySelector('.panel');

const animation = panel?.animate(
  [
    { opacity: 0, transform: 'translateY(0.75rem)' },
    { opacity: 1, transform: 'translateY(0)' },
  ],
  {
    duration: 220,
    easing: 'cubic-bezier(.2, .8, .2, 1)',
    fill: 'both',
  },
);

animation?.finished.then(() => {
  panel?.removeAttribute('data-entering');
});
```

Respect reduced motion before starting non-essential effects:

```js
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

if (!reduceMotion.matches) {
  panel?.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 180 });
}
```

The Web Animations API is a browser API, not a full choreography system. For timelines, springs, gestures, or cross-framework coordination, a library may provide useful abstractions; see Appendix G.

### Motion paths

CSS motion paths can move an element along a geometric path. `offset-path` defines the path, `offset-distance` controls progress, and `offset-rotate` controls orientation. Keep the path decorative unless the moving object’s route is essential and remains understandable without animation.

```css
.delivery-dot {
  offset-path: path('M 0 80 C 80 0 180 160 280 40');
  animation: delivery-progress 2s ease-in-out both;
}

@keyframes delivery-progress {
  from { offset-distance: 0%; }
  to { offset-distance: 100%; }
}
```

Provide a static route or progress indicator for users who reduce motion. Avoid motion paths that move focusable content away from the user’s current reading position.

### Scroll-driven animation terminology

Scroll-driven animation links an animation timeline to scroll progress rather than wall-clock time. There are two common timeline types:

- A **scroll progress timeline** advances as a scroll container moves from one end to the other.
- A **view progress timeline** advances as an element enters, crosses, and exits a scrollport.

The animation can be driven by CSS using `animation-timeline`, or by JavaScript and a library that provides a compatible abstraction.

```css
@keyframes reading-progress {
  from { scale: 0 1; }
  to { scale: 1 1; }
}

.reading-progress {
  transform-origin: left center;
  animation: reading-progress linear both;
  animation-timeline: scroll(root block);
}
```

The `linear` timing function is appropriate here because scroll position is already the progress signal. A time-based easing curve can make the indicator lag or jump relative to the user’s scroll.

### Named scroll timelines

Named timelines make a relationship explicit. `scroll-timeline-name` names a scroll progress timeline on a scroller; `scroll-timeline-axis` selects the axis. The consuming element refers to the name with `animation-timeline`.

```css
.article-shell {
  scroll-timeline-name: --article-scroll;
  scroll-timeline-axis: block;
  overflow-y: auto;
}

.article-progress {
  animation: reading-progress linear both;
  animation-timeline: --article-scroll;
}
```

If the timeline is not available, the progress bar should not imply a value it cannot calculate. A static brand or a normal progress control is safer than a broken indicator.

### View timelines and reveal effects

View timelines are useful for revealing or emphasizing content as it enters the scrollport. `view-timeline-name` names the subject’s view timeline; `view-timeline-axis` selects the axis. The subject and the animated descendant must be related in a way the browser can resolve.

```css
.chapter-section {
  view-timeline-name: --section-view;
  view-timeline-axis: block;
}

.chapter-section__body {
  animation: section-reveal linear both;
  animation-timeline: --section-view;
  animation-range: entry 0% cover 35%;
}

@keyframes section-reveal {
  from {
    opacity: 0;
    translate: 0 1rem;
  }
  to {
    opacity: 1;
    translate: 0 0;
  }
}
```

Keep the initial state readable if the animation is unsupported or skipped. A reveal that leaves content permanently transparent is a progressive-enhancement bug.

### `animation-range` and named range points

`animation-range`, `animation-range-start`, and `animation-range-end` limit which part of a scroll or view timeline drives the animation. Named range points such as `entry`, `cover`, `contain`, and `exit` express the relationship in terms of the subject’s visibility rather than arbitrary pixel offsets.

```css
.card {
  animation: card-lift linear both;
  animation-timeline: view(block);
  animation-range: entry 10% cover 30%;
}

@keyframes card-lift {
  from { opacity: 0; scale: .94; }
  to { opacity: 1; scale: 1; }
}
```

Use ranges to prevent an effect from starting too early or continuing after the element is already fully visible. Verify the exact syntax in the browsers you support because scroll-driven animation remains newer than ordinary transitions and keyframes.

### Scroll-driven animation with `@supports`

Keep the fallback outside the feature query and gate only the enhancement. Do not hide essential content in anticipation of a timeline.

```css
.story-card {
  opacity: 1;
}

@supports (animation-timeline: view()) {
  .story-card {
    animation: story-card-enter linear both;
    animation-timeline: view(block);
    animation-range: entry 0% cover 30%;
  }
}
```

If the feature query is false, the card remains fully visible. That is the correct baseline.

### Performance: animate the right things

Transform and opacity are often good candidates for compositor-friendly animation, but “GPU accelerated” is not a guarantee and excessive layers can also cost memory. Layout properties such as `width`, `height`, `top`, and `left` can trigger more work when animated. Sometimes a layout property is the correct choice; measure before optimizing.

```css
/* Prefer a transform for a visual slide. */
.drawer {
  translate: 100% 0;
}

.drawer[data-open='true'] {
  translate: 0 0;
}
```

Avoid adding `will-change` permanently. It is a resource hint for a short-lived anticipated change, not a general performance switch.

### Reduced motion is a behavior policy

`prefers-reduced-motion` is not a request to remove every transition. It asks the interface to reduce unnecessary movement, spatial travel, and parallax while preserving state clarity and feedback.

```css
.hero-image {
  animation: hero-drift 12s ease-in-out infinite alternate;
}

@media (prefers-reduced-motion: reduce) {
  .hero-image {
    animation: none;
  }

  *,
  *::before,
  *::after {
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}
```

Do not apply a global motion reset without checking dialogs, focus movement, loading indicators, and other feedback. Replace an elaborate effect with a shorter, opacity-only transition when that remains helpful.

### Motion checklist

- Define the static states before defining the transition between them.
- Prefer transform and opacity for visual movement, but measure real performance.
- Use explicit transition properties instead of `transition: all`.
- Keep DOM order and focus order independent of visual motion.
- Keep content visible when scroll timelines, JavaScript, or animations are unsupported.
- Respect `prefers-reduced-motion` and provide a way to pause long-running motion.
- Test keyboard, touch, zoom, high contrast, slow devices, and interrupted navigation.

### Compatibility and source trail

Consult the live compatibility data before shipping. This chapter is a teaching reference, not a frozen guarantee.

- MDN CSS reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties
- MDN CSS animations: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations
- MDN CSS transitions: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions
- MDN scroll-driven animations: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations
- MDN Web Animations API: https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API
- web.dev scroll-driven animations: https://developer.chrome.com/docs/css-ui/scroll-driven-animations
- web.dev Learn CSS: https://web.dev/learn/css
- W3Schools CSS reference: https://www.w3schools.com/cssref/
