#!/usr/bin/env bash
set -euxo pipefail  # https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/

### Variable section (might be modified later)
NUMENTRIES=100

### End variable section

# Setup
mkdir -p results

# Select dataset 
if [ ! -e results/pdb_selection.txt ]; then
  echo "FIRST PART: Select dataset"
  ../bin/select_from_pdb.py $NUMENTRIES > results/pdb_selection.txt
fi

# Download dataset
echo "SECOND PART: Download dataset"
../bin/download_from_pdb.py results/pdb_selection.txt

# Cleanup
mv pdb/* results && rmdir pdb
rmdir obsolete
#gzip results/*ent  # would be better to pack those files to save space
