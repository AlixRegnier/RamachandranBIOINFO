from ..ClusterPoint import *
from ..Point import Point
from ..ClusteringMeasures import *
from typing import List, Union

try :
    a = ClusteringMeasures("angles_1TEY_small_clust.txt")
    isinstance(a,ClusteringMeasures)
    print("test 1 : sucess - a is a ClusteringMeasures")
except :
    print("test 1 : failure - a isn't a ClusteringMeasures")

try :
    a = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(1,1,1,1)
    b = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(1,2,3,1)
    assert(a == 0)
    assert(b ==((1-3)**2+(2-1)**2)**0.5)
    print("test 2 : success - function distance() works")
except :
    print("test 2 : failure - function distances doesn't work")

try :
    cp=ClusterPoint(2,5,"1")
    C = ClusteringMeasures("angles_1TEY_small_clust.txt").a(cp)
    d1 = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(2,5,-1.296614,2.370531)
    d2 = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(2,5,-1.511338,-0.570213)
    m = (d1 + d2 )/ 2
    assert(C == m)
    print("test 3 : sucess - function a() works")
except :
    print("test 3 : failure - function a() doesn't work")