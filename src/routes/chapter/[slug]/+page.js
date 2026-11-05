import { error } from '@sveltejs/kit';
import { chapters } from '$lib/content';

const aliases = {
  '6-flexbox-and-grid': '7-flexbox',
  '6-flexbox': '7-flexbox',
  '7-grid-and-subgrid': '8-grid-and-subgrid',
  '8-grid-lanes-and-masonry-layout': '9-grid-lanes-and-masonry-layout'
};

export function entries() {
  return [
    ...chapters.map(({ slug }) => ({ slug })),
    ...Object.keys(aliases).map((slug) => ({ slug }))
  ];
}

export function load({ params }) {
  const canonicalSlug = aliases[params.slug] ?? params.slug;
  const chapter = chapters.find((item) => item.slug === canonicalSlug);
  if (!chapter) throw error(404, 'Chapter not found');
  return { chapter, slug: chapter.slug };
}
