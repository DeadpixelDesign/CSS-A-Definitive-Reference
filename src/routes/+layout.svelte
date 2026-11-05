<script>
  import '../app.css';
  import 'highlight.js/styles/monokai.css';
  import { base } from '$app/paths';
  import { chapters } from '$lib/content';

  export let data;
  let menuOpen = false;
</script>

<svelte:head>
  <title>CSS: A Definitive Practical Reference</title>
  <meta name="description" content="A source-linked, code-heavy CSS reference for learning, designing, and shipping CSS." />
</svelte:head>

<div class="site-shell">
  <header class="topbar">
    <button class="menu-toggle" type="button" aria-label="Open chapter menu" aria-expanded={menuOpen} onclick={() => (menuOpen = !menuOpen)}>
      <svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16" /></svg>
      <span>Chapters</span>
    </button>
    <a class="brand" href={base || '/'}>
      <span class="brand-mark">CSS</span>
      <span><strong>A Definitive Reference</strong><small>Edition 1.0 · 2026</small></span>
    </a>
    <nav class="top-actions" aria-label="Book actions">
      <a class="button button-quiet" href={`${base}/CSS_Definitive_Reference_2026.md`} download><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m0 0 4-4m-4 4-4-4M5 20h14" /></svg>Download full book Markdown</a>
      <a class="button button-primary" href={base || '/'}><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="m3 11 9-8 9 8M5 10v10h14V10M9 20v-6h6v6" /></svg>Book home</a>
    </nav>
  </header>

  <div class="book-layout">
    {#if menuOpen}
      <button class="drawer-backdrop" type="button" aria-label="Close chapter menu" onclick={() => (menuOpen = false)}></button>
    {/if}
    <aside class:open={menuOpen} class="sidebar" aria-label="Book chapters">
      <div class="sidebar-topline">
        <div class="sidebar-heading">Contents</div>
        <button class="drawer-close" type="button" aria-label="Close chapter menu" onclick={() => (menuOpen = false)}>×</button>
      </div>
      <nav>
        {#each chapters as item, index}
          <a class:active={data?.slug === item.slug} href={`${base}/chapter/${item.slug}`} onclick={() => (menuOpen = false)}>
            <span class="chapter-index">{String(index + 1).padStart(2, '0')}</span>
            <span>{item.title}</span>
          </a>
        {/each}
      </nav>
    </aside>
    <main class="main-content">
      <slot />
    </main>
  </div>

  <footer class="site-footer">
    <span>CSS: A Definitive Practical Reference</span>
    <span>Sources: MDN · web.dev · W3Schools · Sass · Can I Use</span>
  </footer>
</div>
