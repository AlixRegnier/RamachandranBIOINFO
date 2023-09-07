from abc import ABC
from Point import Point
from ClusterPoint import ClusterPoint
from random import sample, choice
from math import sqrt

class ClusteringMethods(ABC):
    """
    Class that contains some algorithms for clustering 2D points
    """
    def __init__(self, l_points):
        """
        Initialize the class with points

        Parameters:
        -----------
        l_points : list<tuple<float>>
        A list of tuple with two dimensions
        """
        self.l_points = [Point(*p) for p in l_points]
        self.clusters = []

    @staticmethod
    def distance(p1, p2):
        """
        Calculate the euclidian distance between two points

        Parameters:
        -----------
        p1, p2 : Point

        Returns:
        --------
        return : float
        """
        return sqrt((p1.abs - p2.abs)**2 + (p1.ord - p2.ord) ** 2)

    def write_file(self, filename):
        with open(filename, "w") as f:
            f.write("x\ty\tcluster\n")
            for c in range(len(self.clusters)):
                for p in self.clusters[c]:
                    f.write(f"{p.abs}\t{p.ord}\t{c}\n")
    
    def getClusterPoints(self):
        list = []

        for i in range(len(self.clusters)):
            for j in range(len(self.clusters[i])):
                list.append(ClusterPoint(self.clusters[i][j].abs, self.clusters[i][j].ord, i))

        return list 

class Kmeans(ClusteringMethods):
    def __init__(self, l_points, k):
        if k <= 0:
            raise ValueError("k shall be greater than 0")
        super().__init__(l_points)
        self.clusters = [[] for _ in range(k)]
        self.k = k
        self.clusters = self.kmeans()

    @staticmethod
    def centroid_cluster(points):
        x = 0
        y = 0
        for p in points:
            x += p.abs
            y += p.ord

        return Point(x / len(points), y / len(points))

    def kmeans(self):
        centroids = sample(self.l_points, self.k)

        changed = True
        while changed:
            self.clusters = [[] for _ in range(self.k)]
            for p in self.l_points:
                min_dist = -1
                cluster = 0
                for i in range(self.k):
                    d = ClusteringMethods.distance(p, centroids[i])
                    if min_dist == -1 or d < min_dist:
                        min_dist = d
                        cluster = i
                
                self.clusters[cluster].append(p)

            changed = False
            for i in range(self.k):
                p = Kmeans.centroid_cluster(self.clusters[i])
                if p.abs != centroids[i].abs or p.ord != centroids[i].ord:
                    changed = True
                    centroids[i] = p

        return self.clusters

class DBscan(ClusteringMethods):
    def __init__(self, l_points, epsilon, min_points):
        super().__init__(l_points)
        self.epsilon = epsilon
        self.min_points = min_points
        self.clusters = self.dbscan()
    
    def get_cores(self):
        cores = []
        for i in range(len(self.l_points)):
            count = 0
            for j in range(i+1, len(self.l_points)):
                if ClusteringMethods.distance(self.l_points[i], self.l_points[j]) < self.epsilon:
                    count += 1

            if count >= self.min_points:
                cores.append(self.l_points[i])
        return cores

    def get_neighbors(self, p):
        n = set()
        for v in self.l_points:
            if p != v and ClusteringMethods.distance(p, v) < self.epsilon:
                n.add(v)
        return n

    def build_cluster(self, p, cluster, cores):
        if p not in cluster:
            cores.remove(p)
            cluster.add(p)
            for v in self.get_neighbors(p):
                if v in cores:
                    self.build_cluster(v, cluster, cores)
                else:
                    cluster.add(v)

    def dbscan(self):
        cores = set(self.get_cores())
        clusters = []
        while cores:
            x = choice(list(cores))
            cluster = set()
            self.build_cluster(x, cluster, cores)
            clusters.append(list(cluster))
        
        return clusters