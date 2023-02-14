#!/bin/bash

# generate list of xyz files sorted by file sizes
ls -l xyz/ | awk '{if ($9!="") print $5,$9}' | sort -n | awk '{print $2}' > lists/xyz_files.txt

