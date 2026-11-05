# CSSA Definitive Reference

A code-heavy, source-linked CSS reference and living web book.

## Development

```sh
npm install
npm run content
npm run dev
```

## Production build

```sh
npm run content
npm run build
```

The generated static site is written to `build/`. GitHub Actions publishes that folder to GitHub Pages whenever `main` changes.
