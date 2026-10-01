"""Compare masses in source/data with the local PDG database. Reports only, never edits.

Setup: python3 -m venv .the-sm && .the-sm/bin/pip install -r build/pdg/requirements.txt
Run:   .the-sm/bin/python build/pdg/check.py
"""
import glob, sys, yaml, pdg

TO_GEV = {"eV": 1e-9, "MeV": 1e-3, "GeV": 1}
QUARKS = ("u", "d", "s", "c", "b")  # masses are properties, not p.mass
# data id -> PDG name; ids not listed (photon, gluon, constants, neutrinos) are not checked
NAMES = {"u": "u", "d": "d", "s": "s", "c": "c", "b": "b", "t": "t",
         "e": "e-", "mu": "mu-", "tau": "tau-", "W": "W+", "Z": "Z", "H": "H"}
api = pdg.connect()


def pdg_mass(i):
    """(mass, error) in GeV. Quark errors: positive side only (ponytail: asymmetric errors ignored)."""
    p = api.get_particle_by_name(NAMES[i])
    if i in QUARKS:
        b = next(x for x in p.properties() if x.description == f"{i}-QUARK MASS").best_summary()
        k = TO_GEV[b.units]
        return b.value * k, b.error_positive * k
    return p.mass, p.mass_error


def same(ours, theirs):
    """Equal to the precision we wrote: within half a unit of our last digit."""
    d = len(ours.split(".")[1]) if "." in ours else 0
    return abs(float(ours) - theirs) <= 0.5 * 10 ** -d


bad = 0
print(f"PDG edition {api.edition}")
for f in sorted(glob.glob("source/data/*.yml")):
    if f.endswith("sources.yml"):
        continue
    for e in yaml.safe_load(open(f)):
        if e["id"] not in NAMES:
            continue
        k = TO_GEV[e["unit"]]
        m, err = (x / k for x in pdg_mass(e["id"]))
        ok = same(e["value"], m) and ("err" not in e or same(e["err"], err))
        bad += not ok
        ours = e["value"] + (f" ± {e['err']}" if "err" in e else "")
        print(f"{'ok  ' if ok else 'DIFF'} {e['id']:4} ours {ours:28} pdg {m:.10g} ± {err:.3g} {e['unit']}")
sys.exit(bool(bad))
