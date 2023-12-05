### conda environment
### conda activate my-rdkit-env

import os
import sys
from rdkit import Chem
from rdkit.Chem import Descriptors

f = open("result.csv","w")
f.write("MW,HBA,HDA,LogP\n")

data = open("list.csv","r")
list = data.readlines()
for i in list:
    id = i.split()[0]
    smiles = i.split()[1]
    
    # smiles to mol
    m = Chem.MolFromSmiles(smiles)
    # Add Hydrogen
    mol = Chem.AddHs(m)
    
    # Molecular weight
    MW = Descriptors.MolWt(mol)
    
    HBA = Descriptors.NOCount(mol)
    HBD = Descriptors.NHOHCount(mol)
    LogP = Descriptors.MolLogP(mol)
    
    #Yun
    mw_y = Descriptors.ExactMolWt(mol)
    hba_y = Descriptors.NumHAcceptors(mol)
    hbd_y = Descriptors.NumHDonors(mol)
    logp_y = Descriptors.MolLogP(mol)
    ring_y = len(Chem.GetSymmSSSR(mol))
    
    
    f.write(str(mw_y) + "," + str(hba_y) + "," + str(hbd_y) + "," + str(LogP) + "\n")

f.close()