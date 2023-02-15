import re

max_dists = {}
with open('max_dists.txt', 'r') as f:
    for line in f.readlines():
        xyz, max_dist = line.strip().split()
        max_dists[xyz] = float(max_dist)

nontrivial = []
with open('alexander.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        xyz, topol = line.split()
        xyz = xyz.split('.')[0]
        m = re.search("'0_1':(...)", topol)
        if m:
            prob = float(m[1])
            if prob >= .5: continue
        nontrivial.append([xyz, max_dists[xyz], topol])

nontrivial = sorted(nontrivial, key=lambda x:x[1])
nontrivial_fmtd = []
for xyz, dist, topol in nontrivial:
    nontrivial_fmtd.append('{:8} {:6.2f}  {}'.format(xyz, max_dists[xyz], topol))
print('\n'.join(nontrivial_fmtd))
