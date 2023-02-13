from collections import defaultdict

pdb_chains_dict = defaultdict(list)
classes = []
with open('bgsu_3269_4A.csv', 'r') as f:
    for line in f.readlines():
        eq_class, representative, *_ = line.replace('"','').split(',')
        representative = representative.split('+')
        chains = []
        for rep in representative:
            pdb, _, chain = rep.split('|')
            pdb_chains_dict[pdb].append(chain)
            chains.append(chain)
        classes.append('{} {} {}'.format(eq_class, pdb, ','.join(chains)))

pdb_chains = []
for pdb, chains in sorted(pdb_chains_dict.items()):
    pdb_chains.append('{} {}'.format(pdb, ','.join(chains)))

with open('lists/pdbs_chains.txt', 'w') as f:
    f.write('\n'.join(pdb_chains))
with open('lists/eq_classes.txt', 'w') as f:
    f.write('\n'.join(classes))
