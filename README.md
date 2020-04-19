# Short description

This project aims at identifying and determining the relative frequency of constituent amino acids for three protein secondary structural classes: helix, sheet, and other. This is achieved by downloading PDB files from PDBList, parsing the files and calculating the relative frequency, and lastly plotting the results for visualization purposes.

# This was my approach

I approached this project by firstly educating myself on PDB (databank, files, format) and Biopython.
I then started the initial planning phase and was next able to use bash script 01run.sh to select 100 random PDB files and download them.
Using the downloaded files they were parsed and the relative frequency for amino acids determined using bash script 02run.sh.
I was then able to use the output file with the calculated relative frequency to plot the results using bash script 03run.sh.

# Installation/usage instructions

Required environment: 
- Online access to PDB database
- Python (3.7.6)
- Biopython (1.76)
- xssp (`mkdssp` executable, 3.0.5)
- numpy (1.18.1)
- matplotlib (3.1.1)
- pandas (1.0.3)

Complete list of the environment this project was developed in is provided as `requirements.txt` file.

---
Project author: Hrönn Kjartansdóttir
