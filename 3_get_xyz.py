import numpy as np
import os
from Bio.PDB.MMCIF2Dict import MMCIF2Dict
from math import sqrt
from tqdm import tqdm
from collections import defaultdict

class Analyze(object):
    corr_atoms = ["C5'","C4'","C3'","O3'","P","O5'"]
    def __init__(self, pdb, corr_chains):
        self.pdb = pdb
        self.corr_chains = corr_chains
        self.mmcif_dict = MMCIF2Dict('cif/{}.cif'.format(self.pdb))
        self.records, self.max_dists = self.load_records()
        self.save_records()

    @staticmethod
    def calc_dist(new_coords, old_coords):
        if None in old_coords:
            return None
        dist = np.sqrt(np.sum(np.power(new_coords-old_coords,2)))
        return dist

    def load_records(self):
        record_type_l = self.mmcif_dict.get('_atom_site.group_PDB')
        atom_type_l = self.mmcif_dict.get('_atom_site.label_atom_id')
        chain_id_l = self.mmcif_dict.get('_atom_site.auth_asym_id')
        resid_id_l = self.mmcif_dict.get('_atom_site.label_seq_id')
        atom_id_l = self.mmcif_dict.get('_atom_site.id')
        alt_id_l = self.mmcif_dict.get('_atom_site.label_alt_id')
        x_l = self.mmcif_dict.get('_atom_site.Cartn_x')
        y_l = self.mmcif_dict.get('_atom_site.Cartn_y')
        z_l = self.mmcif_dict.get('_atom_site.Cartn_z')
        records = {}
        max_dists = {}
        alt_id_corr = defaultdict(lambda: '.')
        for record_type, atom_type, chain_id, alt_id, resid_id, atom_id, x, y, z in zip(
            record_type_l, atom_type_l, chain_id_l, alt_id_l, resid_id_l, atom_id_l, x_l, y_l, z_l):
#            if record_type == 'ATOM':
            if chain_id in self.corr_chains and atom_type in Analyze.corr_atoms:
                if alt_id not in alt_id_corr[chain_id]:
                    if alt_id_corr[chain_id] == '.':
                        alt_id_corr[chain_id] += alt_id
                    else: continue
                if not chain_id in records.keys():
                    records[chain_id] = []
                    max_dists[chain_id] = 0
                    old_coords = np.array([None, None, None])
                    old_resid_id = None
                    old_atom_type = None
                if (old_resid_id, old_atom_type) == (resid_id, atom_type): continue
                label = '-'.join([atom_id, chain_id, resid_id, atom_type])
                coords = np.array([float(k) for k in [x,y,z]])
                dist = self.calc_dist(coords, old_coords)
                if dist == None: dist = -1
                elif dist == 0: continue
                elif dist > max_dists[chain_id]:
                    max_dists[chain_id] = dist
                record = (label, dist, x, y, z)
                records[chain_id].append(record)
                old_coords = coords
                old_resid_id = resid_id
                old_atom_type = atom_type
        return records, max_dists

    def save_records(self):
        for chain in self.corr_chains:
            lines = []
            lines_xyz = []
            i = 0
            for label, dist, x, y, z in self.records[chain]:
                i += 1
                line = '{:20} {:.2f} {:d} {} {} {}'.format(label, dist, i, x, y, z)
                line_xyz = '{:d} {} {} {}'.format(i, x, y, z)
                lines.append(line)
                lines_xyz.append(line_xyz)
            with open('xyz/{}_{}.xyz'.format(self.pdb, chain), 'w') as f:
                f.write('\n'.join(lines_xyz))
            with open('ext_xyz/{}_{}.xyz'.format(self.pdb, chain), 'w') as f:
                f.write('\n'.join(lines))
        with open('max_dists.txt', 'a+') as f:
            for chain, dist in self.max_dists.items():
                f.write('{}_{} {:.2f}\n'.format(self.pdb, chain, dist))

def analyze():
    with open('max_dists.txt', 'w') as f:
        pass
    pdbs = []
    with open('lists/pdbs_chains.txt', 'r') as f:
        for line in f.readlines():
            pdb, chains = line.strip().split()
            chains = chains.split(',')
            pdbs.append([pdb, chains])
    for pdb, chains in tqdm(pdbs):
#        print('>> ', pdb, chains)
        A = Analyze(pdb, chains)

if __name__ == '__main__':
    analyze()
