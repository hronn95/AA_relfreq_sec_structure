#!/usr/bin/env python

'''
Get pdb index and randomly select a number of sequences.

More info: https://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ,
https://github.com/biopython/biopython/blob/master/Bio/PDB/PDBList.py; e.g.
>>>os.system("python PDBList.py all /data/pdb")  # download whole database
'''

import sys, os
import random
from Bio.PDB import PDBList

try:
  DATASIZE = int(sys.argv[1])
except:
  print('Usage:', os.path.basename(sys.argv[0]), '''N
  
  N - number of entries to be randomly selected from all PDB entries.
  Output written to stdout.''', file=sys.stderr)
  sys.exit(1)

# Get index file
pdbl = PDBList()
#print(f"Downloading PDB index file, this takes a while.", file=sys.stderr)
all_entries = pdbl.get_all_entries()

# Select random subset
selected = random.sample(all_entries, DATASIZE)
print(f"Randomly selected %d entries from {len(all_entries)} entries." % DATASIZE, file=sys.stderr)

# Write results to stdout
for entry in selected:
  print(entry, file=sys.stderr)

# Get data files
#for entry in selected:
#  pdbl.retrieve_pdb_file(entry, file_format="pdb", pdir="pdb")


