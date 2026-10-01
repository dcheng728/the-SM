"""Fail if any _data entry lacks id/symbol/value/source, repeats an id, or cites an unknown source."""
import glob, sys, yaml

src = yaml.safe_load(open("source/data/sources.yml"))
bad = []
for f in glob.glob("source/data/*.yml"):
    if f.endswith("sources.yml"):
        continue
    seen = set()
    for e in yaml.safe_load(open(f)):
        for k in ("id", "symbol", "value", "source"):
            if not e.get(k) and e.get(k) != 0:
                bad.append(f"{f}: {e.get('id')}: missing {k}")
        if e["id"] in seen:
            bad.append(f"{f}: duplicate id {e['id']}")
        seen.add(e["id"])
        if e["source"] not in src:
            bad.append(f"{f}: {e['id']}: unknown source {e['source']}")
        if not isinstance(e["value"], str):
            bad.append(f"{f}: {e['id']}: value must be a quoted string")
print("\n".join(bad) or "ok")
sys.exit(bool(bad))
