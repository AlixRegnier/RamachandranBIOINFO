from random import *
from math import *

tab=[(-1.296614, 2.370531), (-1.511338, -0.570213), (-2.371938, 2.313760), (-2.258944, 1.963503), (-1.259170, 2.105960), (-1.842084, -1.062512), (-1.771746, 2.187521), (-2.512711, 2.102471), (-2.403030, 2.659685), (-1.829785, 2.320666), (-2.017124, 3.129947), (1.269690, -0.450515), (-1.487427, 2.605062), (-1.570298, 2.488378), (-2.626018, 2.921923), (-0.841249, 2.507612), (-0.842724, -0.446035), (-1.411080, 0.286016), (-1.521470, 2.770053), (-1.478889, 2.602934), (-1.211359, 1.635598), (-1.725112, 1.906587), (-2.041602, 2.424909), (-1.876201, 1.742638), (-1.754265, 2.010250), (-1.914455, 1.853089), (-2.101968, 2.382771), (-1.818571, 1.999129), (-1.316841, 2.009511), (-1.329947, -0.519881), (-2.427104, 2.891669), (-1.294477, 2.264084), (-1.560267, 2.299633), (-1.785510, -0.471119), (-1.650293, 2.860153), (-1.535437, 2.406232), (-1.530744, 2.089859), (-1.688016, 1.763315), (-1.531831, 2.420221), (-2.421205, 2.547948), (-1.839761, 1.691518), (-1.686690, 1.844244), (-1.639756, 2.536854), (-1.240277, 2.025359), (-1.206102, -0.957996), (-2.414380, 2.353385), (-1.281364, -0.419033), (-1.187862, -0.738219), (-2.500448, 1.799694), (-1.196767, -0.196068), (-1.205962, -0.146895), (-1.462574, 0.138981), (-1.118819, 2.549342), (-2.465259, 2.318127), (-1.421465, 2.355275), (-1.742047, -1.102867), (-2.306870, 2.709722), (-2.448593, 2.126566), (-1.793591, 2.046430), (-2.005182, 2.286704), (-1.970683, 1.792342), (-1.846897, 1.974665), (-1.718165, 2.918932), (-1.735774, 1.942966), (-1.331726, 2.607481), (-1.094644, 2.147893), (2.696566, 2.848181), (-1.505243, 1.847566), (-1.776928, 2.401046)]
tab2=[(-1.296614, 2.370531), (-1.511338, -0.570213), (-2.371938, 2.313760), (-2.258944, 1.963503), (-1.259170, 2.105960), (-1.842084, -1.062512)]


#Piscine 1
class ClusteringMethods:
    def calcul_distance(tuple1,tuple2):
        return(sqrt((tuple1[0]-tuple2[0])**2+(tuple1[1]-tuple2[1])**2))

    def to_cluster(list_centroid,l_point):
        #print("list_centroid",list_centroid)

        list_cluster=[[] for _ in range(len(list_centroid))]

        for index_point in range(0,len(l_point)):
            lower_distance = -1
            for index_centroid in range(0,len(list_centroid)):
                distance = calcul_distance(list_centroid[index_centroid],l_point[index_point])            
                if distance == 0:
                    continue
                if lower_distance == -1 :
                    lower_distance = distance
                    cluster_to_save = index_centroid
                if distance < lower_distance:
                    lower_distance = distance
                    cluster_to_save = index_centroid
            list_cluster[cluster_to_save].append(l_point[index_point])
        return list_cluster

#Méthode de clustering
from random import *
class Kmeans(ClusteringMethods):
    """
    This class it's to

        Attributes:

        l_points: It's a list.
        Contains a list of points.
        k: It's a int.
        Contains the number of groups.
        clust_kmeans: It's a list of list.
        Contains the result of the clustering.
    """

    def init(self, l_points, k):
        clustkmeans=[[] for _ in range(k)]

    def random_centroid_initialization(l_point, k):
        list_copied=l_point.copy()
        list_centroid=[]
        for i in range(k):
            total_point = len(list_copied)
            index_picked = randint(0,total_point-1)
            list_centroid.append(list_copied[index_picked])
            del(list_copied[index_picked])

        return(list_centroid)
        
    #print(random_centroid_initialization(tab, 3))


    def new_mean_cluster(list_cluster):
        somme_phi_pointx = 0
        somme_psi_pointy = 0
        list_new_centroid=[[] for _ in range(len(list_centroid))]
        for cluster_index in range(len(list_cluster)):
            print("cluster_index ",cluster_index)
            print("cluster_nb ",len(list_cluster[cluster_index]))
            for point_index in range(len(list_cluster[cluster_index])):
                #print(list_cluster[cluster_index][point_index][0]) 
                somme_phi_pointx += list_cluster[cluster_index][point_index][0]
                somme_psi_pointy += list_cluster[cluster_index][point_index][1]
            div_phi=somme_phi_pointx/len(list_cluster[cluster_index])
            div_psi=somme_psi_pointy/len(list_cluster[cluster_index])
            tuple_div=(div_phi,div_psi)
            print(tuple_div)
            list_new_centroid.append(tuple_div)

        return(list_new_centroid)


list_centroid=random_centroid_initialization(tab, 3)
liste_cluster=(to_cluster(list_centroid,tab))
new_mean_cluster(liste_cluster)
# print()
# for i in liste_cluster:
#     print(i)

