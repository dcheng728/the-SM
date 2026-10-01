"""Compare masses in source/data with the PDG published values. Reports only, never edits.

Compares against PDG's published (rounded) value, not the database's numeric field,
which can lag behind (e.g. W: published 80.3692, numeric field still 80.377).

Setup: python3 -m venv .the-sm && .the-sm/bin/pip install -r build/pdg/requirements.txt
Run:   .the-sm/bin/python build/pdg/check.py
"""
import glob, re, sys, yaml, pdg

TO_GEV = {"eV": 1e-9, "MeV": 1e-3, "GeV": 1}
# data id -> PDG name; ids not listed (photon, gluon, constants, neutrinos) are not checked
NAMES = {"u": "u", "d": "d", "s": "s", "c": "c", "b": "b", "t": "t",
         "e": "e-", "mu": "mu-", "tau": "tau-", "W": "W+", "Z": "Z", "H": "H"}
api = pdg.connect()


def published(i):
    """(mass, error) in GeV as PDG prints them, or None if not a symmetric value."""
    sums = (x.best_summary() for x in api.get_particle_by_name(NAMES[i]).properties() if x.data_type == "M")
    b = next(s for s in sums if s and s.units in TO_GEV)  # skips e.g. the electron mass in atomic mass units
    m = re.match(r"([\d.]+)\+-([\d.]+)", b.display_value_text)  # ponytail: asymmetric errors unsupported
    if not m:
        return None
    k = TO_GEV[b.units]
    lag = abs(b.value - float(m[1])) > 0.5 * 10 ** -len(m[1].partition(".")[2])
    return float(m[1]) * k, float(m[2]) * k, lag


def same(ours, theirs):
    """Equal to the precision we wrote: within half a unit of our last digit."""
    return abs(float(ours) - theirs) <= 0.5 * 10 ** -len(ours.partition(".")[2])


bad = 0
print(f"PDG edition {api.edition}")
for f in sorted(glob.glob("source/data/*.yml")):
    if f.endswith("sources.yml"):
        continue
    for e in yaml.safe_load(open(f)):
        if e["id"] not in NAMES:
            continue
        pub = published(e["id"])
        if pub is None:
            print(f"skip {e['id']}: asymmetric error")
            continue
        k = TO_GEV[e["unit"]]
        m, err, lag = pub[0] / k, pub[1] / k, pub[2]
        ok = same(e["value"], m) and ("err" not in e or same(e["err"], err))
        bad += not ok
        ours = e["value"] + (f" ± {e['err']}" if "err" in e else "")
        print(f"{'ok  ' if ok else 'DIFF'} {e['id']:4} ours {ours:28} pdg {m:.10g} ± {err:.3g} {e['unit']}"
              + ("  (db numeric field differs from published)" if lag else ""))
sys.exit(bool(bad))
