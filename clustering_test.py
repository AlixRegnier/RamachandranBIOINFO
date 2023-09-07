from AminoAcid import AminoAcid
from Atom import Atom
from Point import Point
from PDBStructure import StructurePDB
from ClusterPoint import ClusterPoint
from Clustering import *
from math import sqrt
import os


test_points = [(-1.296614, 2.370531), (-1.511338, -0.570213), (-2.371938, 2.313760), (-2.258944, 1.963503), 
     (-1.259170, 2.105960), (-1.842084, -1.062512), (-1.771746, 2.187521), (-2.512711, 2.102471), 
     (-2.403030, 2.659685), (-1.829785, 2.320666), (-2.017124, 3.129947), (1.269690, -0.450515),
     (-1.487427, 2.605062), (-1.570298, 2.488378), (-2.626018, 2.921923), (-0.841249, 2.507612), 
     (-0.842724, -0.446035), (-1.411080, 0.286016), (-1.521470, 2.770053), (-1.478889, 2.602934), 
     (-1.211359, 1.635598), (-1.725112, 1.906587), (-2.041602, 2.424909), (-1.876201, 1.742638), 
     (-1.754265, 2.010250), (-1.914455, 1.853089), (-2.101968, 2.382771), (-1.818571, 1.999129), 
     (-1.316841, 2.009511), (-1.329947, -0.519881), (-2.427104, 2.891669), (-1.294477, 2.264084),
     (-1.560267, 2.299633), (-1.785510, -0.471119), (-1.650293, 2.860153), (-1.535437, 2.406232),
     (-1.530744, 2.089859), (-1.688016, 1.763315), (-1.531831, 2.420221), (-2.421205, 2.547948),
     (-1.839761, 1.691518), (-1.686690, 1.844244), (-1.639756, 2.536854), (-1.240277, 2.025359),
     (-1.206102, -0.957996), (-2.414380, 2.353385), (-1.281364, -0.419033), (-1.187862, -0.738219),
     (-2.500448, 1.799694), (-1.196767, -0.196068), (-1.205962, -0.146895), (-1.462574, 0.138981),
     (-1.118819, 2.549342), (-2.465259, 2.318127), (-1.421465, 2.355275), (-1.742047, -1.102867),
     (-2.306870, 2.709722), (-2.448593, 2.126566), (-1.793591, 2.046430), (-2.005182, 2.286704), 
     (-1.970683, 1.792342), (-1.846897, 1.974665), (-1.718165, 2.918932), (-1.735774, 1.942966), 
     (-1.331726, 2.607481), (-1.094644, 2.147893), (2.696566, 2.848181), (-1.505243, 1.847566),
     (-1.776928, 2.401046)]
Ks= [2,3,4]; epsilon=2; min_p = 4
Km = Kmeans(test_points,Ks[0])
Ds = DBscan(test_points, epsilon, min_p)

# check calcul_distance(p1, p2)
try:
    assert ClusteringMethods.distance(Point(test_points[0][0],test_points[0][1]),Point(test_points[1][0],test_points[1][1])) == sqrt((2.370531 -(-0.570213))** 2 + ((-1.296614) - (-1.511338))**2)
    print("The test of function calcul_distance(p1,p2) has passed.")
except:
    AssertionError
    print("The test of function calcul_distance(p1,p2) has failed.")
    
# check centroid_cluster(points)
test_points2 = [Point(3,3), Point(3,4), Point(2,4), Point(4,3), Point(2,3)]
try:
    assert str(Kmeans.centroid_cluster(test_points2)) == "Point of coordinates (2.8000, 3.4000)"
    print("The test for centroid_cluster(points) has passed.")
except:
    AssertionError
    print("The test for centroid_cluster(points) has failed.")

# check kmeans(self)
try: 
    check_list=[]
    for ka in Ks:
        check_list.append(len(Kmeans(test_points,ka).kmeans()))
    assert check_list == Ks
    print("The test of function kmeans has passed in terms of number of cluster formation.")
except:
    AssertionError
    print(("The test of function kmeans has failed in terms of number of cluster formation."))
    
# check get_cores
test_no_core = [(3,3), (3,4), (2,4), (4,3), (10,2)]
test_core = [(3,3), (3,4), (2,4), (4,3), (2,3)]
Ds_no = DBscan(test_no_core, epsilon, min_p)
Ds_yes = DBscan(test_core, epsilon, min_p)

try:
    assert Ds_no.get_cores() == []
    print("The test of function get_core has passed.")
except:
    AssertionError
    print("The test of function get_core has failed.")
    
try:
    assert Ds_yes.get_cores() != []
    print("The test of function get_core has passed.")
except:
    AssertionError
    print("The test of function get_core has failed.")
    
# check get_neighbours(self, p)
list_check_core = {"Point of coordinates (3.0000, 4.0000)", "Point of coordinates (2.0000, 3.0000)","Point of coordinates (2.0000, 4.0000)", "Point of coordinates (4.0000, 3.0000)"}
try:
    list_str_neighbour =[]
    for neighbour in Ds_yes.get_neighbors(Point(3,3)):
        list_str_neighbour.append(str(neighbour))
    assert set(list_str_neighbour) == list_check_core
    print("The test for function get_neighbours has passed.")
except:
    AssertionError
    print("The test for function get_neighbours has failed.")
    
# check write_file(self, filename)
try :
    Km.write_file("Km_test_file")
    assert(os.path.exists("Km_test_file"))
    print("The test of function write_file(self, filename) has passed, file exists")
except :
    print("The test of function write_file(self, filename) has failed, dile does not exists")
