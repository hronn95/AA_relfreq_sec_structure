#!/usr/bin/env python

'''Get pdb contents, randomly select some sequences, download them'''

import sys, os
import random
from Bio.PDB import PDBList

try:
  FILE = sys.argv[1]
except:
  print('Usage:', os.path.basename(sys.argv[0]), '''FILE
  
  FILE - text file with entries to be downloaded from PDB.''', file=sys.stderr)
  sys.exit(1)

# Get data files
pdbl = PDBList()
counter = 0
with open(FILE) as fin:
  for entry in fin:
    outfile = pdbl.retrieve_pdb_file(entry.strip(), file_format="pdb", pdir="pdb")
    # In case you are wondering: to know what the `retrieve_pdb_file` method returns,
    # you should read the documentation,
    # https://biopython.org/DIST/docs/api/Bio.PDB.PDBList%27.PDBList-class.html#retrieve_pdb_file
    # Otherwise, the next two lines might not make a lot of sense
    if os.path.exists(outfile):
      counter += 1

# Problem: some structures might not exist ("Desired structure doesn't exists")
print(f'---\nDownloaded {counter} entries from PDB.', file=sys.stderr)
