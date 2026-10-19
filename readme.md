# The Standard Model

To provide compact and clean notes on the standard model, both theory, and experimentally measured quantities, that can serve as a lookup table.

## Layout

- `source/`: the physics. One markdown file per page; equations, numbers and their citations all live in the page.
- `build/`: the site machinery (layout, CSS).

## Build

```sh
bundle install
bundle exec jekyll serve    # http://127.0.0.1:4000/the-SM/
```

Edits to `build/` are not picked up by a running `jekyll serve`; restart it.
