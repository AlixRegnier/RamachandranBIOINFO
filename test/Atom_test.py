from ..Atom import *
import math

try:
    f=Atom("N",1,0,0)
    assert(isinstance(f,Atom))
    print("test 1 : success - f is an atom")
except AssertionError:
    print("test 1 : Failure - f isnt an atom")


try:
    f=Atom("N",1,0,0)
    assert(f.get_name()=="N")
    assert(f.get_name()!="45")
    print("test 2 : sucess - get_name() does access the attribut name")
except AssertionError:
    print("test 2 : Failure - get_name() does not access the attribut name")


try:
    f=Atom("N",1,0,0)
    f.set_name("O")
    assert(f.get_name()=="O")
    f.set_name("0")
    assert(f.get_name()=="0")
    print("test 3 : Success - set_name() does change the attribut name")
except AssertionError:
    print("test 3 : Failure - set_name() does not change the attribut name")


try:
    t=Atom("N",0,0,1)
    assert(t.get_coords()==(0,0,1))
    d=Atom("N",457897,4578,-45648798)
    assert(d.get_coords()==(457897,4578,-45648798))
    print("test 4 : Success - get_coords does return the correct coordinates as a tuple")
except AssertionError:
    print("test 4 : Failure - get_coords does not return the correct coordinates as a tuple")


try:
    f=Atom("N",0,0,0)
    assert(f.get_coords()==(0,0,0))
    f.set_coords(-457897,-4578,-45648798)
    assert(f.get_coords()==(-457897,-4578,-45648798))
    f.set_coords(-457897,-4578,-45648798)
    assert(f.get_coords()==(-457897,-4578,-45648798))
    f.set_coords(0,0,0)
    assert(f.get_coords()==(0,0,0))
    f.set_coords(0,1,0)
    assert(f.get_coords()==(0,1,0))
    f.set_coords(0,1,1)
    assert(f.get_coords()==(0,1,1))
    print("test 5 : Success - set_coords does change the coordinates correctly")
except AssertionError:
    print("test 5 : Failure - set_coords does not change the coordinates correctly")


try:
    f=Atom("N",1,2,0)
    assert(f.get_x()==1)
    assert(f.get_y()==2)
    assert(f.get_z()==0)
    print("test 6 : Success - get_x, get_y, get_z access the coordinates")
except AssertionError:
    print("test 6 : Failure - get_x, get_y, get_z does not access the coordinates")


try:
    d=Atom("C",25,-50,25)
    f.copy(d)
    assert(f.get_coords()==(25,-50,25))
    assert(f.get_name()==d.get_name())
    print("test 7 : Success - copy does copy correcly the name and the coordinates ")
except AssertionError:
    print("test 7 : Failure - copy does not copy correcly the name and the coordinates ")


try:
    a=str(Atom("C",1,5,6))
    assert(len(a.split(" "))==4)
    assert(float((a.split()[1]).strip("(,)")))
    assert(float((a.split()[2]).strip("(,)")))
    assert(float((a.split()[3]).strip("(,)")))
    print("test 8 : Success - the class is casted as a string correctly")
except AssertionError:
    print("test 8 : Failure - the class is not casted as a string correctly")


try :
    assert(Atom("C",0,1,0).norm()==1)
    assert(Atom("NA",2,3,5).norm()== math.sqrt(38))
    assert(Atom("NA",-2,3,5).norm()== math.sqrt(38))
    print("test 9 : Success - the norm is calculated correctly")
except AssertionError:
    print("test 9 : Success - the norm is not calculated correctly")

try:
    a=Atom("CA",0,0,0).distance(Atom("HA",35,78,54))
    b=(Atom("C",35,78,54).norm())
    assert(a==b)
    print("test 10 : Success - the substraction is done correctly")
except AssertionError:
    print("test 10 : Failure - the substraction is not done correctly")


try:
    assert(Atom("C",1,5,8).dot_product(Atom("N",10,56,8))==354)
    assert(Atom("C",0,0,0).dot_product(Atom("N",10,56,8))==0)
    assert(Atom("C",1,1,1).dot_product(Atom("N",10,56,-8))==58)
    assert(Atom("C",2,2,2).dot_product(Atom("N",2,2,2))==12)
    print("test 11 : Success - the dot product is calculate correctly")
except AssertionError:
    print("test 11 : Failure - the dot product is not calculate correctly")

try:
    assert((Atom("NA",1,2,3).cross_product(Atom("C",3,4,5))).get_coords()==(-2,4,-2))
    assert((Atom("NA",1,2,3).cross_product(Atom("C",3,4,5))).get_coords()==(-2,4,-2))
    print("test 12 : Success - the cross product is calculated correctly")
except:
    print("test 12 : Failure - the cross product is not calculated correctly")



try:
    assert(Atom("N",1,0,0).angle(Atom("N",0,1,0))==(math.pi/2))
    assert((Atom("N",-1.115,8.537,7.075).angle(Atom("N",-1.925,7.470,6.547))==0.09520358627719255))
    print("test 13 : Success - the angles are calculated correctly")
except AssertionError:
    print("test 13 : Failure - the angles are not calculated correctly")


try:
    assert(Atom.dihedral(Atom("C",0,0,0),Atom("G",4,-8,6),Atom("G",15,0,56),Atom("G",4,5,5))==0.3013034999610681)
    print("test 14 : Success - the dihedrals are computed proprely")
except AssertionError:
    print("test 14 : Failure - the dihedrals are not computed proprely")

