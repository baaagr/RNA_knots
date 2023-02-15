# RNA_knots

# Pipeline programs:

```
0_prep_folders.sh
1_prepare.py
2_download_cifs.sh
3_get_xyz.py
4_try_to_join.py
5_gen_xyz_list.sh
6_find_knots.py
7_find_nontrivial.py
```
`0_prep_folders.sh` -- generates folders required for other prgrams;\
`1_prepare.py` -- loads bgsu database csv file and creates `lists/pdbs_chains.txt` and `lists/eq_classes.txt` files;/
`2_download_cifs.sh` -- downloads cif files (into cif folder) based on `lists/pdbs_chains.txt` file;/
`3_get_xyz.py` -- creates xyz files (into `xyz/` and `ext_xyz/` folders) from cif files (using `lists/pdbs_chains.txt`) and `max_dists.txt` file, to create a file whole backbone is used (C5',C4',C3',O3',P,O5' atoms);/
`4_try_to_join.py` -- checks if chains from same equivalence class (`lists/eq_classes.txt`) are so close that actually could create one chain and if yes then joins them and create new xyz file;/
`5_gen_xyz_list.sh` -- creates sorted (by file size) list of xyz files (`lists/xyz_files.txt`);/
`6_find_knots.py` -- identifies knots using [topoly.alexander()]{https://topoly.cent.uw.edu.pl/documentation.html#topoly.alexander} in files listed in `lists/xyz_files.txt` and outputs results into `alexander.txt`;/
`7_find_nontrivial.py` -- checks `alexander.txt` for chains with >50% probability of having a knot and outputs them with their maximal gap.

## Input
```
bgsu_3269_4A.csv
```
Main input is `bgsu_3269_4A.csv` file downloaded from [BGSU RNA database]{http://rna.bgsu.edu/rna3dhub/nrlist/release/3.269}. This file is 3.269 version of database with representants with 4.0 Angstrom resolution or better. Files from other versions also can be used, just pass the file as a first argument to the 1st pipeline program: `python3 1_prepare.py <filename> `.

## Outputs
```
alexander.txt
max_dists.txt
lists/pdbs_chains.txt
lists/eq_classes.txt
lists/xyz_files.txt
cif/*.cif
xyz/*.xyz
ext_xyz/*.xyz
```

`alexander.txt` -- file with knot probabilites for each RNA class representant; probabilities often do not sum to 100% because knots with probabilities <10% (this can be changed in 6th pipeline file by changing `hide_rare` parameter of `topoly.alexander` function);/
`max_dists.txt` -- file with maximal distances of gaps in RNA class representants;/
`lists/pdbs_chains.txt` -- file with pdb and chain codes of RNA class representants;/
`lists/eq_classes.txt` -- file with RNA class names and their representants;/
`lists/xyz_files.txt` -- file with xyz file names sorted by their size;/
`cif/*.cif` -- downloaded cif files of RNA class representants;/
`xyz/*.xyz` -- created xyz files of RNA class representants, coordinates are based on C5',C4',C3',O3',P,O5' atoms;/
`ext_xyz/*.xyz` -- same as `xyz/*.xyz` but with some extra information: label (`atom_id-chain_id-resid_id-atom_type`) and distance between a atom and previous atom.
