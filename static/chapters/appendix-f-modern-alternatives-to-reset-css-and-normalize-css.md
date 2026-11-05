# Appendix F: Modern alternatives to `reset.css` and `normalize.css`

Native CSS and the Web Animations API should be the first tools considered for straightforward transitions, keyframes, and progressive enhancements. Libraries become useful when a project needs reusable motion presets, timelines, springs, scroll coordination, SVG or canvas control, gesture handling, sequencing, or framework integration.

The right library is determined by the problem, not by how many effects its marketing page demonstrates. Evaluate bundle size, licensing, module format, accessibility guidance, cleanup behavior, server-side rendering support, and whether it respects reduced-motion preferences.

### CSS libraries and collections

#### Animate.css

[Animate.css](https://animate.style/) is a familiar collection of ready-made CSS keyframe animations. It is useful for quickly adding entrance, exit, attention, and emphasis effects without writing each `@keyframes` block yourself.

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/animate.css@4/animate.min.css">

<h2 class="animate__animated animate__fadeInUp">
  A softly introduced heading
</h2>
```

Use a class-based library selectively. Importing a large catalog for one effect can add unnecessary CSS, and a class that automatically animates on page load can create motion for users who have requested less of it. Wrap the use in a reduced-motion policy when the library does not provide one globally.

```css
@media (prefers-reduced-motion: reduce) {
  .animate__animated {
    animation: none !important;
  }
}
```

#### Hover.css

[Hover.css](https://ianlunn.github.io/Hover/) is a collection of CSS transitions and hover effects for links, buttons, icons, and other interactive elements. Hover effects should have a keyboard equivalent: apply the same visual state to `:focus-visible` when the effect communicates interaction.

```html
<a class="button hvr-grow" href="/learn">Learn CSS</a>
```

```css
.hvr-grow:hover,
.hvr-grow:focus-visible {
  transform: scale(1.04);
}
```

#### Animista

[Animista](https://animista.net/) is a visual generator and collection of CSS animations. It is especially useful for exploring timing, transforms, and keyframes before copying a small, project-owned result into the stylesheet. Treat generated code as a starting point: rename keyframes, remove unused declarations, and add reduced-motion behavior.

#### Motion UI and component-system utilities

Design systems and component libraries often include motion tokens rather than a standalone animation library. A useful system defines durations, easing curves, distance scales, and reduced-motion alternatives as tokens.

```css
:root {
  --motion-duration-fast: 120ms;
  --motion-duration-standard: 220ms;
  --motion-ease-standard: cubic-bezier(.2, .8, .2, 1);
}

.popover {
  transition:
    opacity var(--motion-duration-fast) var(--motion-ease-standard),
    translate var(--motion-duration-standard) var(--motion-ease-standard);
}
```

The benefit is consistency and governance. A smaller set of tokens is easier to audit than hundreds of unrelated animation classes.

### JavaScript animation libraries

#### GSAP

[GSAP](https://gsap.com/docs/v3/) is a mature, framework-agnostic animation platform with tweens, timelines, easing, staggered animations, and optional plugins for scroll animation, dragging, motion paths, morphing, and more. It is a strong choice for complex choreography or projects that need precise sequencing and broad browser support.

```js
import { gsap } from 'gsap';

const context = gsap.context(() => {
  gsap.from('.card', {
    opacity: 0,
    y: 24,
    duration: 0.45,
    stagger: 0.08,
    ease: 'power2.out',
  });
});

// In a component teardown, revert the context to remove inline styles and listeners.
context.revert();
```

GSAP is powerful enough to become an application architecture. Use timelines for coordinated sequences, but keep semantic state in the DOM or application model rather than encoding state only in animation progress.

#### Motion

[Motion](https://motion.dev/) provides JavaScript, React, and Vue APIs for transforms, springs, gestures, scroll animations, sequences, and staggered effects. Its JavaScript API can animate HTML, SVG, and other values.

```js
import { animate, stagger } from 'motion';

animate(
  '.menu-item',
  { opacity: [0, 1], y: [12, 0] },
  { delay: stagger(0.06), duration: 0.3 }
);
```

For a scroll-linked effect, use the library’s scroll API or native CSS scroll timelines where the browser support and behavior are sufficient. Avoid maintaining two independent sources of truth for the same effect.

```js
import { scroll } from 'motion';

const progress = document.querySelector('.progress');
if (progress) {
  scroll((progressValue) => {
    progress.style.transform = `scaleX(${progressValue})`;
  });
}
```

Add a reduced-motion guard and ensure the progress indicator has an accessible alternative, such as a native `<progress>` element or a text status.

#### anime.js

[anime.js](https://animejs.com/documentation/) is a lightweight animation engine for CSS properties, transforms, DOM and SVG attributes, JavaScript objects, keyframes, timelines, callbacks, and easing. It is a good fit for self-contained effects that do not need the full plugin ecosystem of a larger timeline platform.

```js
import anime from 'animejs';

anime({
  targets: '.dot',
  translateX: 180,
  rotate: '1turn',
  duration: 900,
  easing: 'easeOutElastic(1, .7)',
});
```

Check the version-specific API before copying examples. Major versions may change import paths and method signatures.

#### AOS (Animate On Scroll)

[AOS](https://michalsnik.github.io/aos/) applies data attributes to trigger predefined reveal animations as elements enter the viewport. It can be convenient for static marketing pages with simple entrance effects.

```html
<section data-aos="fade-up" data-aos-duration="500">
  <h2>Progressive enhancement</h2>
</section>
```

```js
import AOS from 'aos';
import 'aos/dist/aos.css';

AOS.init({
  once: true,
  disable: window.matchMedia('(prefers-reduced-motion: reduce)').matches,
});
```

For application interfaces with frequent DOM updates, inspect cleanup and mutation behavior carefully. An IntersectionObserver-based solution or native view timeline may be simpler.

#### ScrollReveal

[ScrollReveal](https://scrollrevealjs.org/) provides a small API for revealing elements as they enter the viewport. It is useful when the desired behavior is “animate this group when it becomes visible,” rather than a continuous scroll-linked relationship.

```js
import ScrollReveal from 'scrollreveal';

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!reduceMotion) {
  ScrollReveal().reveal('.feature', {
    distance: '1rem',
    duration: 500,
    interval: 80,
    origin: 'bottom',
  });
}
```

#### Lottie

[Lottie](https://airbnb.io/lottie/) renders animations exported as JSON from motion-design tools. It is useful for illustrated status, onboarding, and brand motion when CSS shapes are not expressive enough. It is not a replacement for CSS transitions on ordinary controls.

```js
import lottie from 'lottie-web';

const animation = lottie.loadAnimation({
  container: document.querySelector('.empty-state__art'),
  renderer: 'svg',
  loop: false,
  autoplay: true,
  path: '/animations/empty-state.json',
});

// Stop or destroy it when the component leaves the page.
animation.addEventListener('complete', () => animation.pause());
```

Use a static image or a reduced-motion version when animation is not appropriate. Audit JSON size, SVG complexity, color contrast, and whether the animation communicates meaningful information.

### Choosing a library

Use this decision guide:

| Need | First option | Why |
| --- | --- | --- |
| One hover or entrance effect | Native CSS | Smallest dependency and easiest progressive enhancement |
| A catalog of simple preset effects | Animate.css or Hover.css | Fast class-based setup |
| Visual experimentation before writing CSS | Animista | Generates editable CSS starting points |
| Complex sequences and timelines | GSAP | Mature timeline and plugin ecosystem |
| Springs, gestures, and framework motion | Motion | Modern APIs for JavaScript, React, and Vue |
| Lightweight CSS/SVG/object animation | anime.js | Compact API with broad target types |
| Simple viewport reveals | AOS or ScrollReveal | Declarative intersection-triggered effects |
| Designer-authored illustrations | Lottie | JSON-based motion assets |

### Library integration rules

1. Keep semantic state independent of animation progress.
2. Provide a no-library baseline that still exposes all content and controls.
3. Respect `prefers-reduced-motion` before initializing expensive effects.
4. Clean up observers, timelines, event listeners, and inline styles on teardown.
5. Reserve space for media and avoid layout shifts during animation setup.
6. Keep focus visible while elements move, fade, or scale.
7. Avoid animating large numbers of nodes when a parent transform or CSS timeline can express the same effect.
8. Pin dependency versions and read the current license and release documentation before shipping.

### Appendix source trail

- Animate.css: https://animate.style/
- Hover.css: https://ianlunn.github.io/Hover/
- Animista: https://animista.net/
- GSAP documentation: https://gsap.com/docs/v3/
- Motion documentation: https://motion.dev/docs
- anime.js documentation: https://animejs.com/documentation/
- AOS documentation: https://michalsnik.github.io/aos/
- ScrollReveal documentation: https://scrollrevealjs.org/
- Lottie documentation: https://airbnb.io/lottie/
