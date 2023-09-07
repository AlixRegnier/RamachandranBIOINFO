from ..AminoAcid import AminoAcid
from ..Atom import Atom
from ..Point import Point
import os
from ..PDBStructure import StructurePDB

try :
    iS = StructurePDB.readPDB("1TEY.pdb")
    #iS[1].compute_dihedrals()
    iS[1].write_dihedrals("angles_1TEY.txt")
    assert(os.path.exists("angles_1TEY.txt"))
    print("File exists")
except :
    print("file doesn't exist")