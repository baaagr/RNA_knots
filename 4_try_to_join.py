import numpy as np

def calc_dist(new_coords, old_coords):
    dist = np.sqrt(np.sum(np.power(new_coords-old_coords,2)))
    return dist

def get_chains_to_analyze():
    pdb_chains = []
    with open('lists/eq_classes.txt', 'r') as f:
        for line in f.readlines():
            eq_class, pdb, chains = line.strip().split()
            chains = chains.split(',')
            if len(chains) > 1:
                pdb_chains.append([pdb,chains])
    return pdb_chains

def get_chain_ends(pdb, chain):
    with open('xyz/{}_{}.xyz'.format(pdb,chain), 'r') as f:
        first_line, *_, last_line = f.readlines()
    ndx1, x1, y1, z1 = first_line.strip().split()
    ndx2, x2, y2, z2 = last_line.strip().split()
    beg_coords = np.array([float(k) for k in [x1, y1, z1]])
    end_coords = np.array([float(k) for k in [x2, y2, z2]])
    return beg_coords, end_coords

def are_close(pdb, chains):
    begs = {}
    ends = {}
    close = []
    for chain in chains:
        beg_coords, end_coords = get_chain_ends(pdb, chain)
        begs[chain] = beg_coords
        ends[chain] = end_coords
    for chain1 in chains:
        for chain2 in chains:
            if chain1 == chain2: continue
            if calc_dist(ends[chain1], begs[chain2]) < 4:
                close.append((chain1, chain2))
    for close1 in close:
        for close2 in close:
            if close1 == close2: continue
            # assuming maximally two chains are near each other
            assert set(close1) && set(close2) == set()
    return close

if __name__ == '__main__':
    pdb_chains_list = get_chains_to_analyze()
    close_chains = []
    for pdb, chains in pdb_chains_list:
        close = are_close(pdb, chains)
        if close:
            close_chains.append([pdb, close])
    print(close_chains)

