from math import sqrt, acos

class Atom:
  """
      Class that represent the Atoms, the name and the coordonates.

      Attributes:
      -----------
      name : str
          the name of the atom
      px : float
          the coordonate x of the point (atom). The default value is 0.00
      py : float
          the coordonate y of the point (atom). The default value is 0.00
      pz : float
          the coordonate z of the point (atom). The default value is 0.00

  """

  def __init__(self, name, px = 0.00, py = 0.00, pz = 0.00):
    """ Initialize the Class Atom

    Parameters:
    -----------
      name : str
          the name of the atom
      px : float
          the coordonate x of the point (atom). The default value is 0.00
      py : float
          the coordonate y of the point (atom). The default value is 0.00
      pz : float
          the coordonate z of the point (atom). The default value is 0.00
    """
    self.name = name
    self.x = px
    self.y = py
    self.z = pz
	
	
  def set_name(self, pname):
    """
    Function that modifies the name of the atom

    Parameter:
    ----------
    pname : str
        the new name of the atom
    """
    self.name = pname
 	
  def set_coords(self, new_x, new_y, new_z):
    """
    Function that modifies the coordinates of the atom

    Parameters:
    -----------
    new_x : float
        the new coordinate x of the atom
    new_y : float
        the new coordinate y of the atom
    new_z : float
        the new coordinate z of the atom
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
    Function that returns a tuple containing the coordinates (x,y,z) of the current instance
    """
    return(self.x, self.y, self.z)
	
    
  def get_x(self):
    """
    Function that returns the coordinate x of the current instance
    """
    return(self.x)
    
  
  def get_y(self):
    """
    Function that returns the coordinate y of the current instance
    """
    return(self.y)
    
    
  def get_z(self):
    """
    Function that returns the coordinate z of the current instance
    """
    return(self.z)


  def copy(self, another_atom):
    """
    Function that copies the values of the new atom passed as a parameter in the current instance.
    """
    self.set_name(another_atom.get_name())
    self.set_coords(another_atom.get_x(), another_atom.get_y(), another_atom.get_z())
  
  
  def __str__(self):
    """
    Function that returns a string containing the name and the coordinates of the current instance.
    """
    s = "{} ({:.2f}, {:.2f}, {:.2f})".format(self.get_name(), self.get_x(), self.get_y(), self.get_z())
    return(s)
	
	
  def norm(self):
    """
    Function that computes the norm of the vector from O to the current instance

    Returns:
    --------
    float
      value of the norm
    """
    return(sqrt((self.get_x()**2)+(self.get_y()**2)+(self.get_z()**2)))

	
  def distance(self, another_atom):
    """
    Function that computes the distance between the current instance and another atom

    Returns:
    --------
    float
      Value of the distance between two atoms

    """
    return(sqrt(((self.get_x()-another_atom.get_x())**2)+((self.get_y()-another_atom.get_y())**2)+((self.get_z()-another_atom.get_z())**2)))


  def substract(self, another_atom):
    """
    Function that computes the substraction between the current atom and the other atom passed as a parameter, and returns it as a new Atom with an empty name.

    Returns:
    --------
    atom : object
      Object containing an empty name, and the coordinates (x, y, z) of the new atom.
    """
    x=self.get_x()-another_atom.get_x()
    y=self.get_y()-another_atom.get_y()
    z=self.get_z()-another_atom.get_z()
    atom=Atom("", x,y,z)
    return(atom)
	
  def dot_product(self, another_atom):
    """
    Function that computes the dot product between the current atom and the other atom passed as a parameter, and returns it as a float

    Returns:
    --------
    float
      Value of the dot product
    """
    return(((self.get_x()*another_atom.get_x())+(self.get_y()*another_atom.get_y())+(self.get_z()*another_atom.get_z())))


  def cross_product(self, another_atom):
    """
    Function that computes the cross product between the current atom and the other atom passed as a parameter, and returns it as a new Atom with an empty name.

    Returns:
    --------
    atom : object
      Object containing an empty name, and the coordinates (x, y, z) of the new atom.
    """
    cross1=(self.get_y()*another_atom.get_z())-(self.get_z()*another_atom.get_y())
    cross2=(self.get_z()*another_atom.get_x())-(self.get_x()*another_atom.get_z())
    cross3=(self.get_x()*another_atom.get_y())-(self.get_y()*another_atom.get_x())
    atom=Atom("",cross1,cross2,cross3)
    return(atom)

    
  def angle(self, another_atom):
    """
    Function that compute de value of the angle between the current atom and the other atom passed as a parameter.

    Returns:
    --------
    float
      Value of the angle
    """
    return(acos(self.dot_product(another_atom)/(self.norm()*another_atom.norm())))
	

  def dihedral(a1, a2, a3, a4):
    """
    Function that computes dihedral angle (torsion angle) between 4 atoms.

    Returns:
    --------
    float
      Value of the dihedral angle 
    """
    v12 = a1.substract(a2)
    v23 = a2.substract(a3)
    v43 = a4.substract(a3)

    v1 = v23.cross_product(v12)
    v4 = v23.cross_product(v43)
    v = v1.cross_product(v4)

    angle = v1.angle(v4)

    if v.dot_product(v23) > 0:
      return -angle
    else :
      return angle
