# RDKit

Open-Source Cheminformatics and Machine Learning

### Installation

```sh
# Creating a new conda environment with the RDKit installed requires one single command similar to the following
conda create -c conda-forge -n my-rdkit-env rdkit

# Finally, the new environment must be activated so that the corresponding python interpreter becomes available in the same shell
conda activate my-rdkit-env

# If for some reason this does not work, try
cd [anaconda folder]/bin
source activate my-rdkit-env

# Windows users will use a slightly different command
activate my-rdkit-env
```

### File Format
- PDB : Protein Data Bank (Protein, Ligand, DNA Structures)
- Smiles : Simplified Molecular Input Line Entry System (molecules to string type)
- Fasta : FAST-All (DNA, RNA, Protein Amino Acid Sequence)
- SDF : Structural Data Files
- Mol : encode chemical structures, substructures and conformations as text-based connection tables.
- Mol2 : a complete, portable representation of a SYBYL molecule
