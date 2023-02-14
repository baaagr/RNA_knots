#!/bin/bash

ls -l xyz/ | awk '{if ($9!="") print $9}' > lists/xyz_files.txt
