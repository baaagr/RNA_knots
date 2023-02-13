

def calc_dist(new_coords, old_coords):                                       
    dist = np.sqrt(np.sum(np.power(new_coords-old_coords,2)))                
    return dist   

def get_chains_to_analyze():
    pdb_chain_dict = {}
    with open('lists/eq_classes.txt', 'r') as f:
        for line in f.readlines():
            eq_class, pdb, chains = line.strip().split()
            chains = chains.split(',')
            if len(chains) > 1:
                pdb_chain_dict[pdb] = chains
    return pdb_chain_dict

if __name__ == '__main__':
    print(get_chains_to_analyze())
        
