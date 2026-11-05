<script>
  import { afterUpdate, onMount, tick } from 'svelte';
  import { base } from '$app/paths';
  import hljs from 'highlight.js/lib/common';
  export let data;
  $: chapter = data.chapter;
  let highlightReady = false;

  async function highlightChapter() {
    if (typeof window === 'undefined') return;
    if (!highlightReady) {
      window.hljs = hljs;
      await import('highlightjs-line-numbers.js');
      highlightReady = true;
    }
    const prose = document.querySelector('.prose');
    if (!prose) return;
    prose.querySelectorAll('pre.line-numbers code').forEach((block) => {
      if (!block.classList.contains('hljs')) hljs.highlightElement(block);
      if (!block.querySelector('.hljs-ln') && typeof hljs.lineNumbersBlockSync === 'function') {
        hljs.lineNumbersBlockSync(block);
      }
    });
  }

  onMount(async () => {
    await tick();
    await highlightChapter();
  });

  afterUpdate(() => {
    if (highlightReady) highlightChapter();
  });
</script>

<svelte:head>
  <title>{chapter.title} · CSS: A Definitive Reference</title>
</svelte:head>

<article class="chapter-page">
  <div class="chapter-meta"><span class="badge">Chapter</span><span>{chapter.number}</span></div>
  <div class="chapter-header">
    <h1>{chapter.title}</h1>
    <p class="chapter-summary">{chapter.summary}</p>
  </div>
  <div class="chapter-tools">
    <a class="button button-quiet" href={`${base}/chapters/${chapter.slug}.md`} download><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m0 0 4-4m-4 4-4-4M5 20h14" /></svg>Download chapter Markdown</a>
    {#if chapter.compatibility}
      <a class="button button-outline" href={chapter.compatibility} target="_blank" rel="noreferrer noopener">Open compatibility source <svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 4h6v6m0-6-9 9M19 13v6a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h6" /></svg></a>
    {/if}
  </div>
  <div class="prose" class:property-reference={chapter.isPropertyReference}>
    {@html chapter.html}
  </div>
</article>
