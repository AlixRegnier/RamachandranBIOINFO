import sys
from PDBStructure import *

if __name__=="__main__":

    error_message="python daa.py [-d|-k] [k|e] [minpoints] [-phipsi|-chi] filename.pdb\n" + \
                    "-d : dbscan clustering / -k : kmeans clustering\n"+\
                        "[k|e] : number above 0\n"+\
                            "minpoint : number above 0 - this parameter exist only if you have selecter dbscan\n"+\
                            "-phipsi : to analyse the phi and psi angles / -chi : to analyse side chain chi angle \n" + \
                                "filename.pdb : has to be a pdb file"

    try :
        if sys.argv[1] != '-k' and sys.argv[1] != '-d':
            print(error_message)
            exit()
        if int(sys.argv[2]) <= 0:
            print(error_message)
            exit()
        
        if sys.argv[1] == "-d":
            if sys.argv[4] != "-phipsi" and sys.argv[4] !="-chi" or (int(sys.argv[3]) <= 0):
                print(error_message)
                exit()
        else:
            if sys.argv[3] != "-phipsi" and sys.argv[3] !="-chi":
                print(error_message)
                exit()
    except IndexError:
        print(error_message)
        exit()
    
    if sys.argv[1] == '-k':
        model_list=StructurePDB.readPDB(sys.argv[4])
    else:
        model_list=StructurePDB.readPDB(sys.argv[3])

    coordonates_list=[[],[]]
    for i in range(0,len(model_list)):
        a=model_list[i].compute_dihedrals()
        coordonates_list[0].extend(a[0])
        coordonates_list[1].extend(a[1])
        model_list[i].write_dihedrals(f'phi_phi_angles_model_{i+1}')
    
    if sys.argv[1]=="-k"


