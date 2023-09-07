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
    cp=ClusterPoint(-1,9,"1")
    cp1=ClusterPoint(-1.296614,2.370531, "1")
    cp2=ClusterPoint(-1.511338,-0.570213, "1")
    cp3=ClusterPoint(-4.511338,-1.570213, "1")
    cp4=ClusterPoint(-0.841249,2.507612, "2")
    cp5=ClusterPoint(-0.842724,-0.446035, "2")
    cp6=ClusterPoint(-0.942724,-0.546035, "2")
    cp7=ClusterPoint(-1.535437,2.406232, "3")
    cp8=ClusterPoint(-1.530744,2.089859, "3")
    cp9=ClusterPoint(-1.520744,2.099859, "3")
    Clust=ClusteringMeasures("angles_1TEY_small_clust.txt").coefficient_silhouette_i(cp)
    Clust1=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp1)
    Clust2=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp2)    
    Clust3=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp3)
    Clust4=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp4)
    Clust5=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp5)
    Clust6=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp6)
    Clust7=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp7)
    Clust8=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp8)
    Clust9=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").coefficient_silhouette_i(cp9)
    a=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp)
    b=ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp)
    c=(b-a)/max(a,b)
    a1 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp1)
    a2 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp2)
    b1 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp1)
    b2 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp2)
    a3 = ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp3)
    b3= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp3)
    a4= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp4)
    b4= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp4)
    a5= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp5)
    b5= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp5)
    a6= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp6)
    b6= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp6)
    a7= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp7)
    b7= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp7)
    a8= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp8)
    b8= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp8)
    a9= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").a(cp9)
    b9= ClusteringMeasures("angles_1TEY_small_clust_modifV2.txt").b(cp9)

    s1 = (b1 - a1)/ max(a1, b1)
    s2 = (b2 - a2) / max(a2, b2)
    s3 = (b3 - a3) / max(a3, b3)
    s4 = (b4 - a4) / max(a4, b4)
    s5 = (b5 - a5) / max(a5, b5)
    s6 = (b6 - a6) / max(a6, b6)
    s7 = (b7 - a7) / max(a7, b7)
    s8 = (b8 - a8) / max(a8, b8)
    s9 = (b9 - a9) / max(a9, b9)
    print(s1)
    assert(Clust1==s1 and Clust2==s2 and Clust3==s3 and Clust4==s4 and Clust5==s5 and Clust6==s6 and Clust7==s7 and Clust8==s8 and Clust9==s9)
    print("test 5 : sucess - the function coefficient_silhouette_i works")
except:
    print("test 5 : failure - the function coefficient_silhouette_i doesn't work")


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
    print("test 6 : sucess - function intra_max_distance() works")

except :
    print("test 6 : failure - function intra_max_distance() doesn't work")

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
    print("test 7 : sucess - function cluster_centroid() works")

except :
    print("test 7 : failure - function cluster_centroid() doesn't work")

