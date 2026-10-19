# AGENTS.md

Conventions for working on this repo. The site is a compact, equation- and number-driven Standard Model lookup, published with GitHub Pages at `dcheng728.github.io/the-SM`.

## Layout

- `source/` is physics only: pages (`*.md`) holding equations, numbers (as markdown tables) and their citations. Self-contained: no data files, no scripts.
- `build/` is site machinery only: `layouts/`, `assets/`.
- Root holds config only (`_config.yml`, `Gemfile`, `readme.md`, this file). Keep `source/` and `build/` separate.
- A page joins the nav bar by setting `nav:` and `nav_order:` in its front matter and a `permalink`. The home page is the brand link (the site title), so it needs no nav fields.

## Visual consistency with the main site

- This site must look like the owner's main site (`dcheng728.github.io`, repo `dcheng728/dcheng728.github.io`). It loads the main site's stylesheet (`https://dcheng728.github.io/assets/css/main.css`) and uses its `topbar` / `nav-links` pattern and its footer art (identical SVG). Do not copy that CSS into this repo.
- `build/assets/css/dense.css` holds only the overrides this site needs (dense multi-column layout, tables, KaTeX, figures). To change fonts, colours, links, nav or footer, change the main site, not this repo.
- Match the main site's conventions: system font, `#e5e5e5` rules, headings with a thin top rule (no shaded bars), `{{ page.title }} · {{ site.title }}` page titles, KaTeX 0.16.11. Only the type size is deliberately denser here.

## Writing math

- Use `$$...$$` for all math (kramdown turns it into `\(...\)` / `\[...\]` for KaTeX). Display math goes on its own line with blank lines around it.
- **Avoid `\,` and `\;`** (thin and medium math spaces): drop them by default. In units write `\mathrm{km}\ \mathrm{s}^{-1}` style or `\ `, never `\,`. Use `\;` only occasionally, where it is the right spacing (e.g. between list items on one line), not as a habit.
- KaTeX does not support `\slashed`; write `\gamma^\mu D_\mu`.
- Never fuse a control word with the next letter after deleting a space command (`\gamma c`, not `\gammac`). Browser checks must count KaTeX error spans by their red colour (`color:#cc0000`), not only the `.katex-error` class.
- The layout is dense multi-column (about 330px per column). Split any equation that would be wider than a column; check with the browser, not by eye.
- Section labels are real headings (`###`), not bold paragraphs, so they cannot be stranded at a column break. Likewise avoid lead-in paragraphs ending in a colon ("Comoving observers:"): they strand at the bottom of a column; turn them into a heading or fold them into the equation.
- Units upright (`\mathrm{...}`); keep the page equation-first with minimal prose.

## Content scope

- Only established material: things standard in the field and used in practice (for statistics, the methods used in the Higgs discovery). No speculative or frontier methods unless asked.
- Include only what the owner has studied and understands; their course notes (Standard Model, Relativity and Cosmology, and Astrophysics) define the scope.
- Notation: stay close to the standard literature, PDG reviews first, then standard textbooks. Where the course notes use idiosyncratic symbols, prefer the literature's and tell the owner. Use one symbol per quantity across all pages (e.g. `M_W`, `M_Z`, `m_H`), and say which sign and metric conventions a page uses.
- If a course note looks wrong (e.g. mislabelled curvature sign), follow the correct physics and tell the owner.

## Images

- Images live in `source/images/`, web-sized (about 900px wide or less, compressed), referenced with `{{ '/source/images/<file>' | relative_url }}`. Never hotlink.
- Use only the owner's own images or ones with a free licence (public domain, CC BY, CC BY-SA). Check the licence metadata on the source page before adding.
- Every image gets descriptive `alt` text and a caption crediting the author and licence, with links to the licence and the source page.
- If you modify an image (resize, crop, recolour, transparency), say so in the caption; CC BY requires indicating changes. Prefer WebP with alpha for transparent images.

## Numbers and sources

- Numbers go in markdown tables in the page, with a `Source:` line under each table linking the PDG review / CODATA / paper. Keep significant figures as written in the source.
- Never write constants from memory. Read them from the cited source and say where.
- In table cells write `\lvert V\rvert`, not `|V|` (a pipe breaks the table).

## Build and verify

- Build with the pinned Jekyll: `bundle exec jekyll build -d <scratch>` or `bundle exec jekyll serve`. The site is under `/the-SM/` (`baseurl`).
- `_config.yml` `exclude` replaces Jekyll's defaults, so add new non-site files (docs, tooling) to it.
- Edits under `build/` are not picked up by a running `jekyll serve`; restart it.
- Check pages in a real browser at several widths (no horizontal overflow, no clipped equations, no KaTeX errors, no headings stranded at a column break).

## Git

- Do not commit or push unless asked. Stage the files for one logical commit at a time and suggest a message; keep `source/` and `build/` changes in separate commits. The owner's shorthand "SGMM" means "stage and give me message": stage the next logical commit and suggest its message.
