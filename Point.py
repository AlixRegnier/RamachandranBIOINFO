from math import sqrt

class Point:
  ''' Creates and manipulates objects of type Point. '''
  
  def __init__(self, x = 0.00, y = 0.00):
    ''' Initializates the class Point, which has two attributes: 
        1)coordinate on x axis
        2)coordinate on y axis
        Parameters
        ----------
        x and y = floats
        
        Returns:
        --------
        '''
    self.abs = x 
    self.ord = y 

  def __str__(self):
    '''An informative visualization of instances Point.
        Parameters:
        ----------

        Returns:
        --------
        String containing information about the current Point.
        '''
    s = "Point of coordinates ({:.4f}, {:.4f})".format(self.get_abs(), self.get_ord())
    return(s)
	
  def get_abs(self):
    ''' Returns the x axis coordinate. 
        Parameters:
        ----------
        
        Returns:
        ----------
        x '''
    return self.abs
	
  def get_ord(self):
    ''' Returns the y axis coordinate. 
        Parameters:
        ----------
        
        Returns:
        ----------
        y '''
    return self.ord

  def set_abs(self,new_abs):
    ''' Sets new value of x axis coordinate. 
        Parameters:
        ----------
        new_abs = float
        
        Returns:
        ----------
        '''
    self.abs=new_abs

  def set_ord(self,new_ord):
    ''' Sets new value of y axis coordinate. 
        Parameters:
        ----------
        new_ord = float
        
        Returns:
        ----------
        '''
    self.ord=new_ord

  def add(self, another_point):
    """ Adds to the current Point another point passed as an argument.
        Parameters:
        ----------
        another_point = object of type Point
            
        Returns:
        ----------
    """
    self.set_abs(self.get_abs()+another_point.get_abs())
    self.set_ord(self.get_ord()+another_point.get_ord())

  def rescale(self, factor):
    """ Rescales the current Point by a scalar passed as an argument.
        Parameters:
        ----------
        factor = float
            
        Returns:
        ----------
    """
    self.set_abs(self.get_abs()*factor)    
    self.set_ord(self.get_ord()*factor)

  def distance_from_origin(self):	
    """ Computes the distance from the current Point to the origin of the plan.
        Parameters:
        ----------
            
        Returns:
        ----------
        distance from origin = float
    """
    return sqrt((self.get_abs())**2 + (self.get_ord())**2)

  def distance(self, another_point):
    """ Computes the distance from the current Point to another Point passed as an argument.
        Parameters:
        ----------
            
        Returns:
        ----------
        distance from origin = float
    """
    return sqrt((self.get_abs() - another_point.get_abs() )**2 + \
                (self.get_ord() - another_point.get_ord() )**2 )


if __name__ == "__main__":	
  pA = Point(0,0)
  pB = Point(1,1)
  pC = Point(2,1)
  pD = Point(3,4)

  print(pA)
  print(pB)
  print(pC)
  print(pD)

  pA.add(pB)
  assert pA.get_abs() == 1, 'Error in Point.add'
  pA.rescale(5)
  assert pA.get_abs() == 5, 'Error in Point.rescale'
  assert pD.distance_from_origin() == 5, 'Error in Point.distance_from_origin'
  assert pB.distance(pC) == 1, 'Error in Point.distance'