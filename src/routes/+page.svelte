<script>
  import { base } from '$app/paths';
  import { chapters, exampleCount } from '$lib/content';

  const roundedExampleCount = Math.floor(exampleCount / 100) * 100;
</script>

<svelte:head>
  <title>CSS: A Definitive Practical Reference</title>
</svelte:head>

<section class="hero-card">
  <div class="eyebrow">CSS / Edition 1.0</div>
  <h1>Before the first rule.</h1>
  <p class="hero-lede">A code-heavy, source-linked reference for learning, designing, shipping, and maintaining CSS.</p>
  <div class="hero-actions">
    <a class="button button-primary" href={`${base}/chapter/${chapters[0]?.slug}`}><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m5 4 14 8-14 8V4Z" /></svg>Start reading</a>
    <a class="button button-outline" href={`${base}/CSS_Definitive_Reference_2026.md`} download><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m0 0 4-4m-4 4-4-4M5 20h14" /></svg>Download full book Markdown</a>
  </div>
</section>

<section class="intro-grid">
  <article class="feature-card feature-card-blue">
    <span class="badge">{chapters.length} chapters</span>
    <h2>Learn the system</h2>
    <p>From the cascade and box model through Grid, typography, responsive design, CSSOM, Sass, and accessibility.</p>
  </article>
  <article class="feature-card feature-card-teal">
    <span class="badge badge-teal">{roundedExampleCount.toLocaleString()}+ code examples</span>
    <h2>See the code</h2>
    <p>Every property entry includes pasteable patterns, plus complete components for cards, navigation, forms, dialogs, themes, and print.</p>
  </article>
  <article class="feature-card feature-card-gold">
    <span class="badge badge-gold">Living reference</span>
    <h2>Check the platform</h2>
    <p>Compatibility policy, Can I Use links, progressive enhancement, and a Markdown source you can keep updating.</p>
  </article>
</section>

<section class="chapter-grid">
  <div class="section-kicker">Read the book</div>
  <h2>Choose a chapter</h2>
  <div class="chapter-cards">
    {#each chapters as chapter, index}
      <a class="chapter-card" href={`${base}/chapter/${chapter.slug}`}>
        <span class="chapter-number">{String(index + 1).padStart(2, '0')}</span>
        <span class="chapter-card-title">{chapter.title}</span>
        <span class="chapter-arrow">→</span>
      </a>
    {/each}
  </div>
</section>

<section class="quote-card">
  <p>Good CSS is not the CSS with the most rules. It is the CSS whose rules make the intended behavior obvious.</p>
  <span>Editorial principle for this book</span>
</section>
