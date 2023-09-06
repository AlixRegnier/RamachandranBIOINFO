from Atom import Atom

class AminoAcid : 
  """
  Class to represent Amino Acid.

  Attributes :
  ------------
  res_type : string
    The type of amino acid.
  res_nomber : int
    The position of the amino acid in chain of amino acid.
  list_backbone : list
    The list of atoms composing the backbone of the amino acid.
  list_side_chain : list
    The list of atom(s) composing the side chain. The default is an empty list.
  """

  def __init__(self, res_type, res_number,list_backbone, list_side_chain = []):
    """
    Initialize the class amino acid.

    Parameters
    ----------
    res_type : string
      The type of amino acid.
    res_nomber : int
      The position of the amino acid in chain of amino acid.
    list_backbone : list
      The list of atoms composing the backbone of the amino acid.
    list_side_chain : list
      The list of atom(s) composing the side chain. The default is an empty list.
    """
    self.res_type = res_type
    self.res_number = res_number
    self.backbone = {}
    for atom_backbone in list_backbone :
      self.backbone[atom_backbone.get_name()] = atom_backbone
    self.side_chain = {}
    for atom_side_chain in list_side_chain :
      self.side_chain[atom_side_chain.get_name()] = atom_side_chain
	
  def __str__(self):
    """
    Method that returns a string with the position of the amino acid, his type and the number of atoms.
    
    Return
    ------
    s : string
        String  with the position of the amino acid, his type and the number of atoms.
    """
    s = "Amino acid number {} of type {} with a list of {} atoms".format(self.get_res_number(), self.get_res_type(), len(self.get_backbone()) + len(self.get_side_chain()))
    return(s)    
    
  def get_N(self):
    """
    Function that returns an Atom corresponding to the N of the current residue

    Return
    ------
    self.get_backbone()["N"] : atom
      object atom corresponding to N
    """
    return (self.get_backbone()["N"])

  def get_CA(self):
    """
    Function that returns an Atom corresponding to the CA of the current residue

    Return
    ------
    self.get_backbone()["CA"] : atom
      object atom corresponding to CA
    """
    return (self.get_backbone()["CA"])      

  def get_C(self):
    """
    Function that returns an Atom corresponding to the C of the current residue

    Return
    ------
    self.get_backbone()["C"] : atom
      object atom corresponding to C
    """
    return (self.get_backbone()["C"])  	

  def get_O(self):
    """
    Function that returns an Atom corresponding to the O of the current residue

    Return
    ------
    self.get_backbone()["O"] : atom
      object atom corresponding to O
    """
    return (self.get_backbone()["O"])
  
  def get_backbone(self):
    """
    Function that returns the list of Atoms of the AminoAcids

    Return
    ------
    self.backbone : dictionnary
      Dictionnary of atom composing backbone
    """
    return (self.backbone)
  
  def get_res_number(self):
    """
    Function that returns the number of the current residue

    return
    ------
    self.res_number : int
      Position of the amino acid in the chain
    """
    return (self.res_number)
  
  def get_res_type (self):
    """
    Function that returns the type of the current residue

    Return
    ------
    self.res_type : string
      type of the amino acid
    """
    return (self.res_type)
  
  def get_side_chain(self):
    """
    Getter that permits to recuperate the side chain.

    Return
    ------
      self.side_chain : dictionnary
      Dictionnary of atoms composing the side chain
    """
    return (self.side_chain)

  def add(self, atom):
    """
    Function that adds a new atom in the list of atoms for the current residue
    """
    self.get_backbone()[atom.get_name()] = atom
  
  def set_res_type(self, new_type ):
    """
    Stter that permit to change the type of the current residue
    """
    self.res_type = new_type
  
  def set_side_chain(self, new_chain ):
    """
    setter that permit to change the composition of the side chain
    """
    self.side_chain = new_chain

  def compute_Chi1(self):
    """
    Function that computes Chi1 for the current amino acid.

    return
    ------
      False : Boolean
      False if there is no Chi1 for the current amino acid

      atom.dihedral() : Int
      The value of Chi1 of the current amino acid
    """
    Chi_0 = ["ALA", "GLY"]
    
    if self.get_res_type() in Chi_0 or len(self.get_side_chain()) == 0 :
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
    """
    Function that computes Chi2 for the current amino acid.

    return
    ------
      False : Boolean
      False if there is no Chi2 for the current amino acid

      atom.dihedral() : Int
      The value of Chi2 of the current amino acid
    """
    Chi2_0 = ["ALA", "GLY", "VAL", "THR","SER", "CYS"]
    if self.get_res_type() in Chi2_0 or len(self.get_side_chain()) == 0 :
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

  def compute_chi3(self):
    """
    Function that computes Chi3 for the current amino acid.

    return
    ------
      False : Boolean
      False if there is no Chi3 for the current amino acid

      atom.dihedral() : Int
      The value of Chi3 of the current amino acid
    """
    Chi2_0 = ["ALA", "GLY", "VAL", "THR","SER", "CYS", "GLU", "PRO", "TYR","ILE", "PHE", "LEU", "TRP", "HIS", "ASN", "ASP"]
    if self.get_res_type() in Chi2_0 or len(self.get_side_chain()) == 0:
      return False
    
    if self.get_res_type() == "LYS":
      return Atom.dihedral(self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["CD"], self.get_side_chain()["CE"])
    
    if self.get_res_type() == "MET":
      return Atom.dihedral(self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["SD"], self.get_side_chain()["CE"])
    
    if self.get_res_type() == "ARG":
      return Atom.dihedral(self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["CD"], self.get_side_chain()["NE"])
    
    if self.get_res_type() == "GLN":
      return Atom.dihedral(self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["CD"], self.get_side_chain()["NE2"])
    
    if self.get_res_type() == "GLU":
      return Atom.dihedral(self.get_side_chain()["CB"], self.get_side_chain()["CG"], self.get_side_chain()["CD"], self.get_side_chain()["OE2"])
    

  def compute_Chi4(self):
    """
    Function that computes Chi4 for the current amino acid.

    return
    ------
      False : Boolean
      False if there is no Chi4 for the current amino acid

      atom.dihedral() : Int
      The value of Chi4 of the current amino acid
    """
    Chi2_0 = ["ALA", "GLY", "VAL", "THR","SER", "CYS", "GLU", "PRO","MET", "GLN", "TYR","ILE", "PHE", "LEU", "TRP", "HIS", "ASN", "ASP"]
    if self.get_res_type() in Chi2_0 or len(self.get_side_chain()) == 0:
      return False
    
    if self.get_res_type() == "LYS":
      return Atom.dihedral(self.get_side_chain()["CG"], self.get_side_chain()["CD"], self.get_side_chain()["CE"], self.get_side_chain()["NZ"])
      
    if self.get_res_type() == "ARG":
      return Atom.dihedral(self.get_side_chain()["CG"], self.get_side_chain()["CD"], self.get_side_chain()["NE"], self.get_side_chain()["CZ"])
    
  def compute_Chi5(self):
    """
    Function that computes Chi5 for the current amino acid.

    return
    ------
      False : Boolean
      False if there is no Chi5 for the current amino acid

      atom.dihedral() : Int
      The value of Chi5 of the current amino acid
    """
    Chi2_0 = ["ALA", "GLY", "VAL", "THR","SER", "CYS", "GLU", "PRO","MET", "GLN", "TYR","ILE", "PHE", "LEU", "TRP", "HIS", "ASN", "ASP", "LYS"]
    if self.get_res_type() in Chi2_0 or len(self.get_side_chain()) == 0:
      return False

    if self.get_res_type() == "ARG":
      return Atom.dihedral(self.get_side_chain()["CD"], self.get_side_chain()["NE"], self.get_side_chain()["CZ"], self.get_side_chain()["NH2"])
    



if __name__ == "__main__":	
  print("Testing Class AminoAcid")
  atomCD = Atom("ND2",18.0,9.5,192.5)
  atom2 = Atom("C",18.0,9.5,0)
  atomCG = Atom("CG",0,0,1)
  atomCB=Atom("CB",1,2,3)
  atomN=Atom("N",-1.115,8.537,7.075)
  atomCA=Atom("CA",-1.925,7.470,6.547)
  Amino = AminoAcid("ALA",2, [atomN,atomCA,atom2,atom2])
  print(Amino.compute_Chi2())
  print(Amino)
  """
  Amino.add(atom2)
  print(Amino)
  print(Amino.get_CA())
  """