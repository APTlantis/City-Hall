## 1. Artifact Panel

```html
<section class="rounded-xl border border-studio-cyan/25 bg-studio-panel p-5 shadow-panel hover:border-studio-cyan/50 hover:shadow-glow-soft transition">
  <div class="mb-4 flex items-center justify-between border-b border-studio-cyan/15 pb-3">
    <h2 class="font-display text-sm uppercase tracking-[0.25em] text-studio-cyan">Featured Dataset</h2>
    <span class="rounded border border-studio-green/40 px-2 py-1 text-xs text-studio-green">ACTIVE</span>
  </div>

  <h3 class="text-2xl font-bold text-studio-text">Rust Code Corpus</h3>

  <p class="mt-2 max-w-prose text-sm leading-6 text-studio-muted">
    High-quality Rust source, docs, examples, crate metadata, and structured samples prepared for small-model fine tuning.
  </p>
</section>
```

## 2. Dataset Card

```html
<article class="group rounded-xl border border-studio-violet/25 bg-studio-soft p-4 transition hover:border-studio-violet/60 hover:shadow-glow-violet">
  <div class="flex gap-4">
    <div class="grid h-20 w-20 place-items-center rounded-lg border border-studio-orange/40 bg-studio-base text-4xl text-studio-orange">
      🦀
    </div>

    <div>
      <div class="mb-2 flex flex-wrap gap-2">
        <span class="rounded border border-studio-orange/40 px-2 py-0.5 text-xs text-studio-orange">RUST</span>
        <span class="rounded border border-studio-cyan/40 px-2 py-0.5 text-xs text-studio-cyan">CODE</span>
        <span class="rounded border border-studio-violet/40 px-2 py-0.5 text-xs text-studio-violet">TRAINING</span>
      </div>

      <h3 class="text-xl font-bold text-studio-text">Rust Code Corpus</h3>
      <p class="mt-1 text-sm text-studio-muted">Curated Rust material for syntax, docs, examples, and crate-aware reasoning.</p>
    </div>
  </div>
</article>
```

## 3. Pipeline Run Card

```html
<section class="rounded-xl border border-studio-violet/50 bg-studio-panel p-5 shadow-glow-violet">
  <div class="flex items-center justify-between">
    <h3 class="font-display text-lg uppercase tracking-wider text-studio-violet">Pipeline Running</h3>
    <span class="animate-pulse rounded border border-studio-violet/50 px-2 py-1 text-xs text-studio-violet">GENERATING</span>
  </div>

  <div class="mt-5 space-y-3">
    <div class="flex justify-between text-sm">
      <span class="text-studio-muted">rust_corpus_pipeline</span>
      <span class="text-studio-cyan">72%</span>
    </div>

    <div class="h-2 overflow-hidden rounded bg-studio-base">
      <div class="h-full w-[72%] rounded bg-studio-violet shadow-glow-violet"></div>
    </div>

    <p class="text-xs text-studio-faint">Normalizing examples, docs, crate metadata, and instruction pairs.</p>
  </div>
</section>
```

## 4. Stat Tile

```html
<div class="rounded-lg border border-studio-cyan/20 bg-studio-base p-4">
  <p class="text-xs uppercase tracking-widest text-studio-muted">Total Tokens</p>
  <p class="mt-2 text-2xl font-bold text-studio-cyan">18.7B</p>
</div>
```

## 5. Dataset Status Language

```html
<div class="rounded-xl border border-studio-faint/30 bg-studio-panel p-4">Idle / archived</div>

<div class="rounded-xl border border-studio-cyan/40 bg-studio-panel p-4 shadow-glow-soft">Active dataset</div>

<div class="rounded-xl border border-studio-violet/50 bg-studio-panel p-4 shadow-glow-violet">Running pipeline</div>

<div class="rounded-xl border border-studio-magenta/50 bg-studio-panel p-4 shadow-glow-magenta">Featured / new</div>

<div class="rounded-xl border border-studio-red/50 bg-studio-panel p-4 shadow-glow-danger">Failed validation</div>
```

## 6. Hero Panel

```html
<section class="relative overflow-hidden rounded-2xl border border-studio-cyan/30 bg-studio-base p-8 shadow-panel">
  <div class="absolute inset-0 bg-gradient-to-br from-studio-cyan/10 via-studio-violet/10 to-studio-magenta/10"></div>

  <div class="relative max-w-3xl">
    <p class="mb-3 font-mono text-sm uppercase tracking-[0.3em] text-studio-cyan">// Aptlantis Studio</p>

    <h1 class="font-display text-5xl font-black uppercase tracking-tight text-studio-text">
      Unique datasets.<br>
      <span class="text-studio-cyan">Small models.</span><br>
      <span class="text-studio-violet">Local power.</span>
    </h1>

    <p class="mt-5 max-w-xl text-studio-muted">
      Curated and generated datasets for niche domains, creative projects, and practical small-model fine tuning.
    </p>

    <div class="mt-6 flex gap-3">
      <a class="rounded border border-studio-cyan/50 px-4 py-2 text-studio-cyan hover:bg-studio-cyan/10 hover:shadow-glow-soft" href="#">
        Browse Datasets →
      </a>

      <a class="rounded border border-studio-violet/50 px-4 py-2 text-studio-violet hover:bg-studio-violet/10 hover:shadow-glow-violet" href="#">
        Launch Pipeline →
      </a>
    </div>
  </div>
</section>
```

## 7. “Panels as Artifacts” Rule

Use this mental model:

| Component     | Meaning             |
| ------------- | ------------------- |
| Panel         | Artifact container  |
| Border color  | Artifact type       |
| Glow          | Artifact state      |
| Badge         | Dataset role        |
| Progress bar  | Pipeline activity   |
| Muted text    | Metadata            |
| Cyan links    | Navigation/indexing |
| Violet links  | Process/action      |
| Magenta links | Discovery/featured  |

This gives the site a real design language: **the UI behaves like an archive of living artifacts**, not just a dashboard.
