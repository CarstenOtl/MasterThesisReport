"""Collect cited keys from thesis/source/*.tex and copy matching entries from library.bib
(first occurrence wins) into literature.bib. Duplicate-key entries that are needed under a
different name are copied with the renamed key listed in RENAMES (flagged in TODO_draft.md)."""
import re, sys, pathlib
root = pathlib.Path('/home/carsten/code/MasterThesisReport')
tex = ''.join(p.read_text(encoding='utf-8') for p in sorted((root/'thesis/source').glob('*.tex')))
cited = set()
for m in re.finditer(r'\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}', tex):
    for k in m.group(1).split(','):
        k=k.strip()
        if k: cited.add(k)
def entries(path):
    txt = path.read_text(encoding='utf-8')
    out = {}
    for e in re.split(r'\n(?=@)', txt):
        m = re.match(r'@(\w+)\{([^,]+),', e)
        if m and m.group(2) not in out:
            out[m.group(2)] = e.strip()
    return out
lib = entries(root/'thesis/source/library.bib')
expo = entries(root/'expose/source/library.bib')
# second occurrences for duplicated keys in library.bib
txt = (root/'thesis/source/library.bib').read_text(encoding='utf-8')
dups = {}
for e in re.split(r'\n(?=@)', txt):
    m = re.match(r'@(\w+)\{([^,]+),', e)
    if m:
        dups.setdefault(m.group(2), []).append(e.strip())
RENAMES = {  # new key -> (library key, index of occurrence, title substring to verify)
    'Tang2023industreal': ('Tang2023', 'IndustReal'),
    'Tang2024screwdriving': ('Tang2024', 'Screwdriving'),
    'Pitz2024shape': ('Pitz2024', 'Shape-Conditioned'),
}
out, missing = [], []
for k in sorted(cited):
    if k in RENAMES:
        lk, sub = RENAMES[k]
        cand = [e for e in dups.get(lk, []) if sub in e]
        if cand:
            out.append(re.sub(r'^(@\w+\{)'+re.escape(lk)+',', r'\g<1>'+k+',', cand[0], count=1)); continue
    if k in lib: out.append(lib[k]); continue
    if k in expo: out.append(expo[k]); continue
    missing.append(k)
header = "% Generated from library.bib (and expose/source/library.bib for Mittal2023, Oertel2026).\n% Entries are copied unchanged; renamed keys: " + ', '.join(RENAMES) + "\n\n"
(root/'thesis/source/literature.bib').write_text(header + '\n\n'.join(out) + '\n', encoding='utf-8')
print('cited', len(cited), 'copied', len(out))
print('MISSING:', ' '.join(missing))
