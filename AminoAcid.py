from Atom import Atom

class AminoAcid : 

  def __init__(self, res_type, res_number,list_backbone, list_side_chain = []):
    self.res_type = res_type
    self.res_number = res_number
    self.backbone = {}
    for atom_backbone in list_backbone :
      self.backbone[atom_backbone.get_name()] = atom_backbone
    self.side_chain = {}
    for atom_side_chain in list_side_chain :
      self.side_chain[atom_side_chain.get_name()] = atom_side_chain
	
  def __str__(self):
    s = "Amino acid number {} of type {} with a list of {} atoms".format(self.get_res_number(), self.get_res_type(), len(self.get_backbone()) + len(self.get_side_chain()))
    return(s)    
    
  def get_N(self):
    """
    Function that returns an Atom corresponding to the N of the current residue
    """
    return (self.get_backbone()["N"])

  def get_CA(self):
    """
    Function that returns an Atom corresponding to the CA of the current residue
    """
    return (self.get_backbone()["CA"])      

  def get_C(self):
    """
    Function that returns an Atom corresponding to the C of the current residue
    """
    return (self.get_backbone()["C"])  	

  def get_O(self):
    """
    Function that returns an Atom corresponding to the O of the current residue
    """
    return (self.get_backbone()["O"])
  
  def get_backbone(self):
    """
    Function that returns the list of Atoms of the AminoAcids
    """
    return (self.backbone)
  
  def get_res_number(self):
    """
    Function that returns the number of the current residue
    """
    return (self.res_number)
  
  def get_res_type (self):
    """
    Function that returns the type of the current residue
    """
    return (self.res_type)
  
  def get_side_chain(self):
    return (self.side_chain)

  def add(self, atom):
    """
    Function that adds a new atom in the list of atoms for the current residue
    """
    self.get_backbone()[atom.get_name()] = atom
  
  def set_res_type(self, new_type ):
    """
    Function that permit to change the type of the current residue
    """
    self.res_type = new_type
  
  def set_side_chain(self, new_chain ):
    """
    Function that permit to change the composition of the side chain
    """
    self.side_chain = new_chain

  def compute_Chi1(self):
    """
    Function that compute angle of all possible Chi.
    """
    Chi_0 = ["ALA", "GLY"]
    
    if self.get_res_type() in Chi_0 :
      return False
    
    Chi_2C =  ["THR", "ASN", "GLN", "GLU", "ASP", "LYS", "ARG", "HIS", "MET", "TRP", "PHE", "TYR", "LEU", "PRO"]
    
    if self.get_res_type() in Chi_2C :
      return Atom.dihedral(self.get_N(), self.get_CA(), self.get_side_chain()["CB"],self.get_side_chain()["CG"])
    
    Chi_CG1= ["VAL", "ILE"]

    if self.get_res_type() in Chi_CG1 :
      return Atom.dihedral(self.get_N(), self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["CG1"])
    
    if self.get_res_type() == "CYS" :
      return Atom.dihedral(self.get_N(), self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["SG"])
    
    if self.get_res_type() == "SER" :
      return Atom.dihedral(self.get_N(), self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["OG"])
    
  def compute_Chi2(self):
    Chi2_0 = ["ALA", "GLY", "VAL", "THR","SER", "CYS"]
    if self.get_res_type() in Chi2_0:
      return False
    
    Chi_2C= ["ARG", "GLN", "LYS", "GLU", "PRO","MET"]
    if self.get_res_type() in Chi_2C :
      return Atom.dihedral(self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["CD"])

    if self.get_res_type() == ["TYR","ILE", "PHE", "LEU"]:
      return Atom.dihedral(self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["CD1"])    

    if self.get_res_type() == "TRP":
      return Atom.dihedral(self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["CD2"])
    
    if self.get_res_type() == "HIS":
      return Atom.dihedral(self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["ND1"])
    
    if self.get_res_type() == "ASN":
      return Atom.dihedral(self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["ND2"])
    
    if self.get_res_type() == "ASP":
      return Atom.dihedral(self.get_CA(), self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["OD2"])
    
    
    


if __name__ == "__main__":	
  print("Testing Class AminoAcid")
  atom1 = Atom("H",18.0,9.5,192.5)
  atom2 = Atom("C",18.0,9.5,0)
  atomCG = Atom("CG",0,0,1)
  atomCB=Atom("CB",1,2,3)
  atomN=Atom("N",-1.115,8.537,7.075)
  atomCA=Atom("CA",-1.925,7.470,6.547)
  Amino = AminoAcid("ASN",2, [atomN,atomCA,atom2,atom1],[atomCB, atomCG])
  print(Amino.compute_Chi1())
  print(Amino)
  """
  Amino.add(atom2)
  print(Amino)
  print(Amino.get_CA())
  """