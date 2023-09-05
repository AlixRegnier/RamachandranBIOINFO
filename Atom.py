from math import sqrt, acos

class Atom:
  def __init__(self, name, px = 0.00, py = 0.00, pz = 0.00):
    self.name = name
    self.x = px
    self.y = py
    self.z = pz
	
	
  def set_name(self, pname):
    """
    Function that modifies the name
    """
    self.name = pname
 	

  def set_coords(self, new_x, new_y, new_z):
    """
    Function that modifies the attributes x, y, z
    """
    self.x = new_x
    self.y = new_y
    self.z = new_z	

  def get_name(self):
    """
    Function that returns the name of the atom as a string
    """
    return(self.name)

    
  def get_coords(self):
    """
    Function that returns a list containing the coodinates (x,y,z)
    """
    return(self.x, self.y, self.z)
	
    
  def get_x(self):
    """
    Function that returns the x coordinate
    """
    return(self.x)
    
  
  def get_y(self):
    """
    Function that returns the y coordinate
    """
    return(self.y)
    
    
  def get_z(self):
    return(self.z)


  def copy(self, another_atom):
    """
    Function that copies the values of the current instance in a new atom passed as a parameter
    """
    self.set_name(another_atom.get_name())
    self.set_coords(another_atom.get_x(), another_atom.get_y(), another_atom.get_z())
  
  
  def __str__(self):
    s = "{} ({:.2f}, {:.2f}, {:.2f})".format(self.get_name(), self.get_x(), self.get_y(), self.get_z())
    return(s)
	
	
  def norm(self):
    """
    Function that computes the norm of the vector from O to the current instance
    """
    return(sqrt((self.get_x()**2)+(self.get_y()**2)+(self.get_z()**2)))

	
  def distance(self, another_atom):
    """
    Function that computes the distance between the current instance and another atom
    """
    return(sqrt(((self.get_x()-another_atom.get_x())**2)+((self.get_y()-another_atom.get_y())**2)+((self.get_z()-another_atom.get_z())**2)))


  def substract(self, another_atom):
    """
    Function that computes the substraction between the current atom and the other atom passed as a parameter, and returns it as a new Atom with an empty name.
    """
    x=self.get_x()-another_atom.get_x()
    y=self.get_y()-another_atom.get_y()
    z=self.get_z()-another_atom.get_z()
    atom=Atom("", x,y,z)
    return(atom)
	
  def dot_product(self, another_atom):
    """
    Function that computes the dot product between the current atom and the other atom passed as a parameter, and returns it as a float
    """
    return(((self.get_x()*another_atom.get_x())+(self.get_y()*another_atom.get_y())+(self.get_z()*another_atom.get_z())))


  def cross_product(self, another_atom):
    """
    Function that computes the cross product between the current atom and the other atom passed as a parameter, and returns it as a new Atom with an empty name.
    """
    cross1=(self.get_y()*another_atom.get_z())-(self.get_z()*another_atom.get_y())
    cross2=(self.get_z()*another_atom.get_x())-(self.get_x()*another_atom.get_z())
    cross3=(self.get_x()*another_atom.get_y())-(self.get_y()*another_atom.get_x())
    atom=Atom("",cross1,cross2,cross3)
    return(atom)

    
  def angle(self, another_atom):
    return(acos(self.dot_product(another_atom)/(self.norm()*another_atom.norm())))
	

  def dihedral(a1, a2, a3, a4):
    """
    Function that computes dihedral angle (torsion angle) between 4 atoms. 
    """
    v12 = a1.substract(a2)
    v23 = a2.substract(a3)
    v43 = a4.substract(a3)

    v1 = v23.cross_product(v12)
    v4 = v23.cross_product(v43)
    v = v1.cross_product(v4)

    angle = v1.angle(v4)

    if v.dot_product(v23) > 0:
      return angle
    else :
      return -angle


if __name__ == "__main__":	
  print("Testing Class Atom")
  atom1 = Atom("H",18.0,9.5,192.5)
  atom2 = Atom("C",18.0,9.5,0)
  atom3 = Atom("O",0,0,1)
  atom4=Atom("X",1,2,3)
  atomN=Atom("N",-1.115,8.537,7.075)
  atomCA=Atom("CA",-1.925,7.470,6.547)
  print(atom1.dihedral(atom2,atom3,atom4))
  """
  print(atomN.norm())
  print(atomCA.norm())
  print(atomN.distance(atomCA))
  print(atomCA.distance(atomN))
  print(atomN.substract(atomCA))
  print(atomCA.substract(atomN))
  print(atomN.dot_product(atomCA))
  print(atomN.cross_product(atomCA))
  print(atomN.angle(atomCA))
  #print(atom1.cross_product(atom2))
  #print(atom2.cross_product(atom1))
  #print(atom4.cross_product(atom1))
  #print(atom3.distance(atom4))
  #print(atom1.dot_product(atom2))
  #print(atom1)
  #print(atom2)
  #print(atom3)
  """