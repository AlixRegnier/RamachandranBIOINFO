# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:07:20 2020

@author: ebecker
"""
from math import sqrt

class Point:
  def __init__(self, x = 0.00, y = 0.00):
    self.abs = x 
    self.ord = y 


  def __str__(self):
    s = "Point of coordinates ({:.4f}, {:.4f})".format(self.get_abs(), self.get_ord())
    return(s)
	
  def get_abs(self):
    return self.abs
	
  def get_ord(self):
    return self.ord

  def set_abs(self,new_abs):
    self.abs=new_abs

  def set_ord(self,new_ord):
    self.ord=new_ord

  def add(self, another_point):
    """
    Functions that adds to the current Point to another point passed as an argument
    """
    self.set_abs(self.get_abs()+another_point.get_abs())
    self.set_ord(self.get_ord()+another_point.get_ord())

  def rescale(self, factor):
    """
    Functions that rescales the current Point by a scalar passed as an argument
    """
    self.set_abs(self.get_abs()*factor)    
    self.set_ord(self.get_ord()*factor)

  def distance_from_origin(self):	
    """
    Functions that computes the distance of the current Point to the origin of the plan O
    """
    return sqrt((self.get_abs())**2 + (self.get_ord())**2)

  def distance(self, another_point):
    """
    Functions that computes the distance of the current Point with another point passed as an argument
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
