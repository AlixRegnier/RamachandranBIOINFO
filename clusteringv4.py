from random import *
from math import *
from abc import ABC, abstractmethod

tab=[(-1.296614, 2.370531), (-1.511338, -0.570213), (-2.371938, 2.313760), (-2.258944, 1.963503), (-1.259170, 2.105960), (-1.842084, -1.062512), (-1.771746, 2.187521), (-2.512711, 2.102471), (-2.403030, 2.659685), (-1.829785, 2.320666), (-2.017124, 3.129947), (1.269690, -0.450515), (-1.487427, 2.605062), (-1.570298, 2.488378), (-2.626018, 2.921923), (-0.841249, 2.507612), (-0.842724, -0.446035), (-1.411080, 0.286016), (-1.521470, 2.770053), (-1.478889, 2.602934), (-1.211359, 1.635598), (-1.725112, 1.906587), (-2.041602, 2.424909), (-1.876201, 1.742638), (-1.754265, 2.010250), (-1.914455, 1.853089), (-2.101968, 2.382771), (-1.818571, 1.999129), (-1.316841, 2.009511), (-1.329947, -0.519881), (-2.427104, 2.891669), (-1.294477, 2.264084), (-1.560267, 2.299633), (-1.785510, -0.471119), (-1.650293, 2.860153), (-1.535437, 2.406232), (-1.530744, 2.089859), (-1.688016, 1.763315), (-1.531831, 2.420221), (-2.421205, 2.547948), (-1.839761, 1.691518), (-1.686690, 1.844244), (-1.639756, 2.536854), (-1.240277, 2.025359), (-1.206102, -0.957996), (-2.414380, 2.353385), (-1.281364, -0.419033), (-1.187862, -0.738219), (-2.500448, 1.799694), (-1.196767, -0.196068), (-1.205962, -0.146895), (-1.462574, 0.138981), (-1.118819, 2.549342), (-2.465259, 2.318127), (-1.421465, 2.355275), (-1.742047, -1.102867), (-2.306870, 2.709722), (-2.448593, 2.126566), (-1.793591, 2.046430), (-2.005182, 2.286704), (-1.970683, 1.792342), (-1.846897, 1.974665), (-1.718165, 2.918932), (-1.735774, 1.942966), (-1.331726, 2.607481), (-1.094644, 2.147893), (2.696566, 2.848181), (-1.505243, 1.847566), (-1.776928, 2.401046)]
tab2=[(-1.296614, 2.370531), (-1.511338, -0.570213), (-2.371938, 2.313760), (-2.258944, 1.963503), (-1.259170, 2.105960), (-1.842084, -1.062512)]

    
class ClusteringMethods(ABC):
    """
    This Class it's to define common clustering methods.     
    """
    def __init__(self, l_points, k):
        self.l_points = l_points
        self.k = k
        self.clusters = [[] for _ in range(k)]

    def calcul_distance(tuple1,tuple2):
        return(sqrt((tuple1[0]-tuple2[0])**2+(tuple1[1]-tuple2[1])**2))
    
    def get_clusters(self):
        """ 
        This function permit to return .
        Parameters:
        -----------
        Returns:
        --------
            List of list that contains clusters.
        """ 
        return [cluster[:] for cluster in self.clusters]

    def output_tabulate(list_res_cluster, filename_cluster):
        """ 
        This function permit to create a tabulated file with phi, psi, cluster_number.
        Parameters:
        -----------
        list_res_cluster : List.
            List of list that contains clusters.
        filename_cluster : String.
            Name of filename to create.
        Returns:
        --------
        """ 
        with open(f"C:\\Users\\rouge\\Documents\\OOP\\{filename_cluster}.txt","w") as fh:
            for id_cluster in range(0,len(list_res_cluster)):
                for id_point in range(0,len(list_res_cluster[id_cluster])):
                    fh.write(f"{list_res_cluster[id_cluster][id_point][0]}\t{list_res_cluster[id_cluster][id_point][1]}\t{list_res_cluster[id_cluster]}")
   
    @staticmethod
    def list_tuple_to_ClusterPoint(list_clusters_tuple):
        list_clustersP=[]
        for cluster in range(len(list_clusters_tuple)):
            for tuple in cluster:
                list_clustersP.append(ClusterPoint(tuple[0], tuple[1], cluster))
        return list_clustersP
    
class Point:
  def __init__(self, x = 0.00, y = 0.00):
    self.abs = x 
    self.ord = y 

class ClusterPoint(Point):
  def __init__(self, x, y, num_cluster):
    self.num_cluster = num_cluster



class Kmeans(ClusteringMethods):
    """
    This class permit to create clusters with kmeans algorithm.
    """
    def init(self, l_points, k):
        super().__init__(l_points, k)
        self.to_cluster()


    def random_centroid_initialization(self):
        """ 
        This function permit to pick a random centroid for the initialization.
        Parameters:
        -----------
        Returns:
        --------
        Point
            Point considered as centroid.
        """
        return sample(self.l_points, self.k)

    
    def to_cluster(self, list_centroid):
        """ 
        This function permit to pick a random centroid for the initialization.
        Parameters:
        -----------
        list_centroid : List.
            Centroid in list.
        Returns:
        --------
        list_cluster : List.
            Clusters in a list.
        """ 
        for centroid in range(len(list_centroid)):
            if type(centroid) != tuple() :
                raise TypeError
            if centroid[0] != float or centroid[1] != float:
                raise TypeError
            if centroid[0] > 180 or centroid[1] > 180:
                raise TypeError
        list_cluster=[[] for _ in range(len(list_centroid))]
        for index_point in range(0,len(self.l_point)):
            lower_distance = -1
            for index_centroid in range(0,len(list_centroid)):
                distance = ClusteringMethods.calcul_distance(list_centroid[index_centroid],self.l_point[index_point])            
                if distance == 0:
                    continue
                if lower_distance == -1 :
                    lower_distance = distance
                    cluster_to_save = index_centroid
                if distance < lower_distance:
                    lower_distance = distance
                    cluster_to_save = index_centroid
            list_cluster[cluster_to_save].append(self.l_point[index_point])
        return list_cluster
    
    def new_mean_cluster(self, list_cluster):
        """ 
        This function permit to calculate the mean of a cluster.
        Parameters:
        -----------
        list_cluster : List.
            Clusters in a list.
        Returns:
        --------
        list_new_centroid : List.
            New centroids in a list.
        """ 
        for cluster in list_cluster:
            if cluster != list():
                raise ValueError
        list_new_centroid=[]
        for cluster_index in range(len(list_cluster)):
            somme_phi_pointx = 0
            somme_psi_pointy = 0
            for point_index in range(len(list_cluster[cluster_index])):
                somme_phi_pointx += list_cluster[cluster_index][point_index][0]
                somme_psi_pointy += list_cluster[cluster_index][point_index][1]
            div_phi=somme_phi_pointx/len(list_cluster[cluster_index])
            div_psi=somme_psi_pointy/len(list_cluster[cluster_index])
            tuple_div=(div_phi,div_psi)
            list_new_centroid.append(tuple_div)
        return(list_new_centroid)

    def kmeans(self):
        """ 
        This function is the main method to execute kmeans algorithm.
        Parameters:
        -----------
        Returns:
        --------
        """ 
        list_centroid=self.random_centroid_initialization(tab, 3)
        liste_cluster=(self.to_cluster(list_centroid,tab))
        while self.new_mean_cluster(liste_cluster) != list_centroid:
            list_centroid=(self.new_mean_cluster(liste_cluster))
            liste_cluster=(self.to_cluster(list_centroid,tab))
        self.output_tabulate(liste_cluster)
        ClusteringMethods.list_tuple_to_ClusterPoint(liste_cluster)

class DBscan(ClusteringMethods):
    """
    This class it's to clustering points with the DBscan method.

        Methods:

        get_core():
        Returns the list of all core points.

        get_neighbor_point():
        Returns the list of neighbor point for a starting point.

        get_neighbor_list():
        Returns the list of all neighbor of a point list.

        db_scan():
        Returns a list of list of cluster.
    """
    def __init__(self, l_points, min_points, epsilon):
        super().__init__(l_points)
        self.min_points = min_points
        self.epsilon = epsilon


    def get_core(self, min_points, epsilon):
        """
        This function return the tuple list of all core points.

        Parameters:

        min_points: Integer.
            Contains the minimal number of points to create a cluster.

        epsilon: Float.
            Contains the minimal distance to consider two point like neighbor.

        Returns:

        List
            Tuple list of all cores.
        """
        core_list = []
        for index_point in range (len(self.l_points)) :
            proximal_counter = 0
            for index_neigh in range (index_point+1, len(self.l_points)) :
                distance = self.calcul_distance(self.l_points[index_point],self.l_points[index_neigh])
                if distance < epsilon :
                    proximal_counter += 1
            if proximal_counter >= min_points :
                core_list.append(self.l_points[index_point])
        return core_list


    def get_neighbor_point(self, min_points, epsilon, starting_point):
        """
        This function return the tuple list of all neighbor for a point.

        Parameters:

        min_points: Integer.
            Contains the minimal number of points to create a cluster.

        epsilon: Float.
            Contains the minimal distance to consider two point like neighbor.

        starting_point: Tuple.
            Coordinate of the starting point.

        Returns:

        List
            Tuple list of all neighbor for a starting point.
        """
        neighbor_list = []
        possible_neighbor_list = []
        proximal_counter = -1 #because the point is neighbor with himself
        for index_point in range(len(self.l_points)) :
            dist = self.calcul_distance(self, starting_point, self.l_points[index_point])
            if dist < epsilon :
                proximal_counter += 1
                possible_neighbor_list.append(self.l_points[index_point])
            if proximal_counter >= min_points :
                neighbor_list = possible_neighbor_list
        return neighbor_list


    def get_neighbor_list(self, min_points, epsilon, liste_to_parse):
        """
        This function return the tuple list for all neighbor for a list of points.

        Parameters:

        min_points: Integer.
            Contains the minimal number of points to create a cluster.

        epsilon: Float.
            Contains the minimal distance to consider two point like neighbor.

        liste_to_parse: List.
            Contains the list of tuple for all neighbor for a point.
            
        Returns:

        List
            Tuple list of all neighbor for a list of points. It's a cluster.
        """
        all_neighbor_list = []
        for point in liste_to_parse:
            temp_list = self.get_neighbor_point(min_points, epsilon, self.l_points, point)
            all_neighbor_list.extend(temp_list)
        return list(set(all_neighbor_list)) #all_neighbor it's pass in a set for remove the double neighbor




    def db_scan(self, min_points, epsilon):
        """
        This function return a list of tuple list. Each list represente a cluster.

        Parameters:

        min_points: Integer.
            Contains the minimal number of points to create a cluster.

        epsilon: Float.
            Contains the minimal distance to consider two point like neighbor.
            
        Returns:

        List
            List of tuple liste. Contains all clusters.
        """
        cluster_list = []
        core_points = set(self.get_core(min_points, epsilon, self.l_points))
        while len(core_points) > 0:
            random_point = choice(self.l_points)
            cluster = self.get_neighbor_list(min_points, epsilon, self.l_points, self.get_neighbor_point(min_points, epsilon, self.l_points, random_point))
            temp = self.get_neighbor_list(min_points, epsilon, self.l_points, cluster)
            while temp != cluster:
                cluster = temp
                temp = self.get_neighbor_list(min_points, epsilon, self.l_points, cluster)
            if len(temp) > 0:
                cluster_list.append(temp)
                core_points -= set(temp)

        self.output_tabulate(cluster_list)
        return ClusteringMethods.list_tuple_to_ClusterPoint(cluster_list)