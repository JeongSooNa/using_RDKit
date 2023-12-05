import os
import sys
from csv import reader
#from tqdm import tqdm
from rdkit import Chem
from rdkit.Chem import Draw

#############################
# Smiles to Images(png) file#
# to using RDKit Packages   #
# Create At 2023.02.01      #
# Update At 2023.02.02      #
# JSNA                      #
# smiles format is in csv   #
#############################

### input parameter
### input smiles csv
### column : index / name / smiles
# input = sys.argv[1]
### output path
# output = sys.argv[2]


# if not os.path.exists(output):
#         os.mkdir(output)



# with open("zinc_smiles.csv",'r') as csv:
#         data = reader(csv)
#         header = next(data)
#         for row in data:
#                 zinc = row[0] # zinc
#                 smiles = row[1] # smiles
#                 print(smiles)
#                 mol = Chem.MolFromSmiles(smiles)
#                 if mol != None:
#                         img = Draw.MolToImage(mol,size=(300,300))
#                         img.save(zinc)

f = open("zinc_smiles.csv","r")
data = f.readlines()
print(len(data))
for i in data:
    zinc = i.split()[0]
    smiles = i.split()[1]
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol,size=(300,300))
    img.save("STAT3_smiles_to_images/"+zinc+".png")
    # if mol != None:
    #     img = Draw.MolToImage(mol,size=(300,300))
    #     img.save("IMG/"+zinc+".png")

##########################################################
####### When this Error Massage pops up, Complete! #######
##########################################################
#       Traceback (most recent call last):               #
#         File "SmilesToImages.py", line 31, in <module> #
#           index = row[0].split('\t')[0] # index        #
#       IndexError: list index out of range              #
##########################################################
