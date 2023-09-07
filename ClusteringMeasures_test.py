import unittest
from ClusterPoint import *
from Point import Point
from ClusteringMeasures import *
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
    cp = ClusterPoint(2,5,"1")
    C = ClusteringMeasures("angles_1TEY_small_clust.txt").a(cp)
    d1 = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(2,5,-1.296614,2.370531)
    d2 = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(2,5,-1.511338,-0.570213)
    m = (d1 + d2 )/ 2
    assert(C == m)
    print("test 3 : sucess - function a() works")

except :
    print("test 3 : failure - function a() doesn't work")

try : 
    Cp = ClusterPoint(2,5,"1")
    Cm = ClusteringMeasures("angles_1TEY_small_clust.txt").b(cp)
    d1 = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(2,5,-0.841249,2.507612)
    d2 = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(2,5,-0.842724,-0.446035)
    m_c2 = (d1 + d2 )/ 2
    d1 = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(2,5,-1.535437,2.406232)
    d2 = ClusteringMeasures("angles_1TEY_small_clust.txt").distance(2,5,-1.530744,2.089859)
    m_c3 = (d1 + d2)/ 2
    assert(Cm==m_c3)
    print("test 4 : sucess - function b() works")
except :
    print("test 4 : failure - function b() doesn't work")

try :
    Cm = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").intra_max_distance("1")
    d = []
    d1 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").distance(-1.296614, 2.370531,-1.511338, -0.570213)
    d2 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").distance(-1.296614, 2.370531,-4.511338, -1.570213)
    d3 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").distance(-1.511338, -0.570213,-4.511338, -1.570213)
    d.append(d1)
    d.append(d2)
    d.append(d3)
    dmax = 0
    for i in d :
        if dmax < i :
            dmax = i
    assert(dmax == Cm)
    print("test 5 : sucess - function intra_max_distance() works")

except :
    print("test 5 : failure - function intra_max_distance() doesn't work")

try : 
    Cm1 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").cluster_centroid("1")
    Cm2 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").cluster_centroid("2")
    Cm3 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").cluster_centroid("3")
    px1 = (-1.296614 + -1.511338 + -4.511338) / 3
    py1 = (2.370531 + -0.570213 + -1.570213) /3
    px2 = (-0.841249 + -0.842724 + -0.942724) /3 
    py2 = (2.507612 + -0.446035 + -0.546035) /3
    px3 = (-1.535437 + -1.530744 + -1.520744) /3
    py3 = (2.406232 + 2.089859 + 2.099859) /3
    assert(Cm1 == Point(px1,py1), Cm2 == Point(px2, py2), Cm3 == Point(px3,py3))
    print("test 6 : sucess - function cluster_centroid() works")

except :
    print("test 6 : failure - function cluster_centroid() doesn't work")

