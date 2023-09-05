from AminoAcid import AminoAcid
from Atom import Atom
from Point import Point

class StructurePDB:
  def __init__(self, AminoAcidlist): 
    """
    Functions that reads a simple PDB file and the necessary information about residues to compute dihedral angles
    """
    self.residues=AminoAcidlist
    self.phipsi=[]


  def compute_dihedrals(self):
    """
    Functions that computes dihedral angles
    source for definition of phi and psi
    https://proteopedia.org/wiki/index.php/Phi_and_Psi_Angles
    """
    phi = [] # list of floats
    psi = [] # list of floats
    self.phipsi = [] # list of Points (class Point...)
    #for i  in range(0,len(self.residues)):

    return [phi,psi]
  

  def write_dihedrals(self, filename):
    """
    Functions that writes a file with 2 columns phi and psi separated by a tabulation, with one line per residue. Values of phi and psi angles are given with a precision of 6 decimals.
    """
    phi_psi=self.compute_dihedrals()
    with open (filename, "w") as output_file:
      if len(phi_psi[0]) == len(phi_psi[1]):
        for i in range (len(phi_psi[0])):
          output_file.write(phi_psi[0][i] + "\t" + phi_psi[1][i] + "\n") 
    
  @staticmethod
  def readPDB(filename):
    model_list=[]
    with open(filename,"r") as in_file:
      new_model=[]
      backbone=[]
      sidechain=[]
      i=0
      for line in in_file:
        if line[0:4] != "ATOM":
          continue
        
        residue_number=line[24:26].strip()
        residue_type=line[17:20].strip()

        coordX = float(line[31:38].strip())
        coordY = float(line[39:46].strip())
        coordZ = float(line[47:54].strip())

        if i==0:
          residue_type=line[17:20].strip()
          old_residue_type=residue_type
          old_residue_number=residue_number
          i+=1
        
        if residue_number != old_residue_number:
          new_model.append(AminoAcid(old_residue_type,old_residue_number,backbone,sidechain))

          old_residue_number=residue_number
          old_residue_type=residue_type
          backbone=[]
          sidechain=[]
        
        elif residue_number == old_residue_number:
          if line[11:16].strip() in ["N","CA","C","O"]:
            backbone.append(Atom(line[11:16].strip(),coordX,coordY,coordZ))
          
          elif "H" not in line[11:16].strip():
            sidechain.append(Atom(line[11:16].strip(),coordX,coordY,coordZ))
        
        if line=="ENDMDL":
          new_model.sort(key=lambda x:x.res_number)
          model_list.append(StructurePDB(new_model))
          new_model=[]
          backbone=[]
          sidechain=[]
          i=0
        
      if new_model:
        new_model.sort(key=lambda x:x.res_number)
        model_list.append(StructurePDB(new_model))

      return model_list
          





#	public static void main(String[] args) throws FileNotFoundException{
#		StructurePDB tey = new StructurePDB("D:/workspace/Enseignement/src/ramachandran/1TEY.pdb");
#		tey.readPDBFile();
#		tey.computeDihedrals();
#		
#		KMeans k4 = new KMeans(tey.phipsi,4);
#		System.out.println(k4);
#		k4.clusterize();
#		System.out.println(k4);
		
#		k4.printOutput();
#	}
iS = StructurePDB.readPDB("1TEY.pdb")

print(iS)
#iS.compute_dihedrals()
#iS.write_dihedrals("angles_1TEY.txt")

