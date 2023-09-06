import unittest
from Point import *

try : 
    f = Point(0,0)
    isinstance(f,Point)
    print("test 1 : success - f is a point")
except:
    print("test 1 : Failure - f isnt a point")


try :
    assert(Point(0, 1).get_abs()==0)
    assert(Point(0, 1).get_ord()==1)
    print("test 2 : success - getters work")
except AssertionError :
    print("test 2 : failure - getters don't work")


try :
    p=Point(0,1)
    p.set_abs(5)
    print(p)
    assert(p.get_abs()==5)
    assert(p)
    print("test 3 : success - setter abs works")
except :
    print("test 3 : failure - setter doesn't work")

try:
    p=Point(1,2)
    p.set_ord(3)
    print(p)
    assert(p.get_ord()==3)
    print("test 4 : success - setter ord works")
except:
    print("test 4 : failure - setter ord doesn't work")

pA = Point(0,0)
pB = Point(1,1)
pC = Point(2,1)
pD = Point(3,4)

try:
    a=Point(2,1).add(Point(1,2))
    b=Point(1,1).add(Point(4,2))
    assert(a == 3,3)
    assert(b == 5,3)
    print("test 5 : sucess - function add works")
except:
    print("test 5 : failure - function add doesn't work")

try :
    p=pB
    p.rescale(2)
    assert(p.get_abs() == 2 and p.get_ord() == 2)
    print("test 6 : sucess - function rescale works")
except:
    print("test 6 : failure - function rescale doesn't work")


try :
    a=Point(2,1).distance_from_origin()
    b=Point(1,6).distance_from_origin()
    assert(a==sqrt((2)**2+(1)**2))
    assert(b==sqrt((1)**2+(6)**2))
    print("test 7 : sucess - function distance_from_origin works")
except:
    print("test 7 : failure - function distance_from_origin does't work")

try :
    a=Point(1,1).distance(Point(1,1))
    b=Point(2,6).distance(Point(2,3))
    c=Point(4,3).distance(Point(2,1))
    assert(c==sqrt((4-2)**2+(3-1)**2))
    assert(a==sqrt((1-1)**2+(1-1)**2))
    assert(b==sqrt((2-2)**2+(6-3)**2))
    print("test 8 : sucess - function distance works")
except:
    print("test 8 : failure - function distance doesn't work")