from AminoAcid import AminoAcid
from Atom import Atom
from Point import Point

class StructurePDB:
  def __init__(self, filename): 
    """
    Functions that reads a simple PDB file and the necessary information about residues to compute dihedral angles
    """
    self.path_to_file = filename
    self.residues = []
    
    with open(self.path_to_file,'r') as in_file: 
      for line in in_file:
        i=1
        if len(line) < 5:
          continue
        
        if line[0:4] != "ATOM":
          continue
        
        atom_type = line[11:16].strip()
        residue_number = int(line[24:26].strip())

          
        coordX = float(line[31:38].strip())
        coordY = float(line[39:46].strip())
        coordZ = float(line[47:54].strip())
        
        if i==1:
          aa_backbone=[]
          aa_sidechain=[] 
          i=+1
          previous_residue_number = residue_number
          previous_residue_type=line[18:20]
        
        if residue_number != previous_residue_number :
          self.residues.append(AminoAcid(previous_residue_type,previous_residue_number,aa_backbone,aa_sidechain))
          previous_residue_type=line[18:20]
          previous_residue_number = residue_number
          aa_backbone=[]
          aa_sidechain=[]
        
        if residue_number == previous_residue_number:
          if atom_type in ["N","CA","C","O"]:
            aa_backbone.append(Atom(atom_type,coordX, coordY, coordZ))
          if atom_type not in ["N","CA","C","O"] and "H" not in atom_type:
            aa_sidechain.append(Atom(atom_type,coordX, coordY, coordZ))
          previous_residue_number = residue_number
        
        if line == "ENDMDL":
          break


  def compute_dihedrals(self):
    """
    Functions that computes dihedral angles
    source for definition of phi and psi
    https://proteopedia.org/wiki/index.php/Phi_and_Psi_Angles
    """
    phi = [] # list of floats
    psi = [] # list of floats
    self.phipsi = [] # list of Points (class Point...)
    for i  in range(0,len(self.residues)):
      if i > 0 :
        phi.append(self.residues[i-1].get_C()\
                  .dihedral(self.residues[i].get_N(),\
                            self.residues[i].get_CA(),\
                              self.residues[i].get_C()))
      else :
        phi.append(None)

      if i < len(self.residues) :
        psi.append((self.residues[i].get_N())\
                  .dihedral(self.residues[i].get_CA(),\
                              self.residues[i].get_C(),\
                                  self.residues[i+1].get_N()))
      else :
        psi.append(None)
      self.phipsi.append(Point(phi[-1],psi[-1]))

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
iS = StructurePDB("1TEY.pdb")
print(iS.residues[0])
print(iS.residues[1])
print(iS.residues[2])
iS.compute_dihedrals()
iS.write_dihedrals("angles_1TEY.txt")