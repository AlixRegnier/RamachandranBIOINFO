from abc import ABC
from Point import Point
from ClusterPoint import ClusterPoint
from random import sample, choice
from math import sqrt

class ClusteringMethods(ABC):
    def __init__(self, l_points):
        self.l_points = [Point(*p) for p in l_points]
        self.clusters = []

    @staticmethod
    def distance(p1, p2):
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


tab=[(-1.296614, 2.370531), (-1.511338, -0.570213), (-2.371938, 2.313760), (-2.258944, 1.963503), (-1.259170, 2.105960), (-1.842084, -1.062512), (-1.771746, 2.187521), (-2.512711, 2.102471), (-2.403030, 2.659685), (-1.829785, 2.320666), (-2.017124, 3.129947), (1.269690, -0.450515), (-1.487427, 2.605062), (-1.570298, 2.488378), (-2.626018, 2.921923), (-0.841249, 2.507612), (-0.842724, -0.446035), (-1.411080, 0.286016), (-1.521470, 2.770053), (-1.478889, 2.602934), (-1.211359, 1.635598), (-1.725112, 1.906587), (-2.041602, 2.424909), (-1.876201, 1.742638), (-1.754265, 2.010250), (-1.914455, 1.853089), (-2.101968, 2.382771), (-1.818571, 1.999129), (-1.316841, 2.009511), (-1.329947, -0.519881), (-2.427104, 2.891669), (-1.294477, 2.264084), (-1.560267, 2.299633), (-1.785510, -0.471119), (-1.650293, 2.860153), (-1.535437, 2.406232), (-1.530744, 2.089859), (-1.688016, 1.763315), (-1.531831, 2.420221), (-2.421205, 2.547948), (-1.839761, 1.691518), (-1.686690, 1.844244), (-1.639756, 2.536854), (-1.240277, 2.025359), (-1.206102, -0.957996), (-2.414380, 2.353385), (-1.281364, -0.419033), (-1.187862, -0.738219), (-2.500448, 1.799694), (-1.196767, -0.196068), (-1.205962, -0.146895), (-1.462574, 0.138981), (-1.118819, 2.549342), (-2.465259, 2.318127), (-1.421465, 2.355275), (-1.742047, -1.102867), (-2.306870, 2.709722), (-2.448593, 2.126566), (-1.793591, 2.046430), (-2.005182, 2.286704), (-1.970683, 1.792342), (-1.846897, 1.974665), (-1.718165, 2.918932), (-1.735774, 1.942966), (-1.331726, 2.607481), (-1.094644, 2.147893), (2.696566, 2.848181), (-1.505243, 1.847566), (-1.776928, 2.401046)]
a = Kmeans(tab, 3)
a.write_file("test.txt")