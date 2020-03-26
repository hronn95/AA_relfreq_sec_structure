#!/usr/bin/bash env

# Setup (create required folder structure and symlinks)
mkdir -p data results tmpdata
rm -rf data/* results/* tmpdata/*

cd data
# In case we have packed files
#for F in ../../01_*/results/*gz; do
#  ln -s $F
#done
# Unpack files
#for F in ./*gz; do
#  gunzip -c $F > ../tmpdata/${F%%.gz}
#done

for F in ../../01_*/results/*ent; do
  ln -s $F
done

cd ..

# Do stuff

# Note: to run compiled *.pyc scripts, you need to call them like this: e.g.
#python ../bin/parse_pdb_files.cpython-37.pyc

