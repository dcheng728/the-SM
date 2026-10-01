# The Standard Model

To provide compact and clean notes on the standard model, both theory, and experimentally measured quantities, that can serve as a lookup table.

## Layout

- `source/`: the physics. `data/*.yml` (every number, with a source key), `index.md` (equations).
- `build/`: the site machinery (layout, table include, CSS, validator, PDG check).

## Build & check

```sh
bundle install                                   # Jekyll as GitHub Pages runs it (pinned in Gemfile.lock)
bundle exec jekyll serve                         # site at http://127.0.0.1:4000
python3 build/validate.py                        # needs PyYAML; also run by CI

# compare masses against the local PDG database (separate Python env, pinned)
python3 -m venv .the-sm && .the-sm/bin/pip install -r build/pdg/requirements.txt
.the-sm/bin/python build/pdg/check.py
```

Edits to `build/` or `source/data/` are not picked up by a running `jekyll serve`; restart it.
