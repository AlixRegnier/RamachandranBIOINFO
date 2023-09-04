from Atom_Student import Atom

class AminoAcid : 

  def __init__(self, res_type, res_number, list_atoms):
    self.res_type = res_type
    self.res_number = res_number
    self.atoms = list_atoms
	
  def __str__(self):
    s = "Amino acid number {} of type {} with a list of {} atoms".format(self.get_res_number(), self.get_res_type(), len(self.get_list_atom()))
    return(s)    
    

  def add(self, atom):
    """
    Function that adds a new atom in the list of atoms for the current residue
    """
    self.get_list_atom().append(atom)
    
  def get_N(self):
    """
    Function that returns an Atom corresponding to the N of the current residue
    """
    for i in self.get_list_atom() :
      if i.get_name() == "N" :
        return (i)


  def get_CA(self):
    """
    Function that returns an Atom corresponding to the CA of the current residue
    """
    for i in self.get_list_atom() :
      if i.get_name() == "CA" :
        return (i)      

  def get_C(self):
    """
    Function that returns an Atom corresponding to the C of the current residue
    """
    for i in self.get_list_atom() :
      if i.get_name() == "C" :
        return (i)  	

  def get_O(self):
    """
    Function that returns an Atom corresponding to the O of the current residue
    """
    for i in self.get_list_atom():
      if i.get_name() == "O" :
        return (i)
  
  def get_list_atom(self):
    """
    Function that returns the list of Atoms of the AminoAcids
    """
    return(self.atoms)
  
  def get_res_number(self):
    """
    Function that returns the number of the current residue
    """
    return(self.res_number)
  
  def get_res_type (self):
    """
    Function that returns the type of the current residue
    """
    return(self.res_type)

if __name__ == "__main__":	
  print("Testing Class AminoAcid")
  atom1 = Atom("H",18.0,9.5,192.5)
  atom2 = Atom("C",18.0,9.5,0)
  atom3 = Atom("O",0,0,1)
  atom4=Atom("X",1,2,3)
  atomN=Atom("N",-1.115,8.537,7.075)
  atomCA=Atom("CA",-1.925,7.470,6.547)
  Amino = AminoAcid("Stérique",2, [atom2,atomCA,atom2,atom3])
  print(Amino)
  Amino.add(atom2)
  print(Amino)
  print(Amino.get_CA())