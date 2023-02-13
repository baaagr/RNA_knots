#!/bin/bash

while read line
do
    pdb=`echo $line | cut -d ' ' -f 1`
    wget https://files.rcsb.org/download/${pdb}.cif -P pdbs_aa/
done < lists/pdbs_chains.txt
