from ClusterPoint import ClusterPoint
from Point import Point
from typing import List, Union

class ClusteringMeasures:
	"""
	Class that provides many methods to calculate various kind of distances between points and clusters
	"""
	def __init__(self, classified_points : Union[List[ClusterPoint], str]):
		"""
		Constructor of the class


		Parameters:
		-----------
		classified_points : list<ClusterPoint> | str
		If str, parse a tabulated file to create instances of ClusterPoint
		"""
		self.clusters = {}
		if isinstance(classified_points, str):
			with open(classified_points, "r") as f:
				f.readline() #skip first line
				for line in f:
					t = line.rstrip().split('\t')
					t[0] = float(t[0])
					t[1] = float(t[1])

					if t[2] in self.clusters:
						self.clusters[t[2]].append(ClusterPoint(*t))
					else:
						self.clusters[t[2]] = [ClusterPoint(*t)]

		elif isinstance(classified_points, list):
			for p in classified_points:
				if p.id_cluster in self.clusters:
					self.clusters[p.id_cluster].append(p)
				else:
					self.clusters[p.id_cluster] = [p]
					
	@staticmethod
	def distance(x1, y1, x2, y2):
		"""
		Calculates the euclidian distance between two points

		Parameters:
		-----------
		x1, y1, x2, y2 : float

		"""
		return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

	def a(self, p):
		"""
		Method that calculates the average distance between a point and other points of its cluster

		Parameters:
		-----------
		p : ClusterPoint

		Returns:
		--------
		return : float
		"""
		sum = 0
		count = 0
		for v in self.clusters[p.id_cluster]:
			if v != p:
				sum += ClusteringMeasures.distance(p.abs, p.ord, v.abs, v.ord)
				count += 1
		
		return sum / count

	def b(self, p):
		"""
		Method that calculates the mean distance between a point and points of another cluster (it uses the cluster which result is the lowest)

		Parameters:
		-----------
		p : ClusterPoint

		Returns:
		--------
		return : float
		"""

		min_dist = -1
		dist = 0

		for c in self.clusters.keys() - {p.id_cluster}:
			sum = 0
			for v in self.clusters[c]:
				sum += ClusteringMeasures.distance(p.abs, p.ord, v.abs, v.ord)
			
			dist = sum / len(self.clusters[c])

			if min_dist < 0 or dist < min_dist:
				min_dist = dist
		
		return min_dist

	def coefficient_silhouette_i(self, p):
		"""
		Method that calculates the silhouette coefficient of a point

		Parameters:
		-----------
		p : ClusterPoint

		Returns:
		--------
		return : float
		"""

		a = self.a(p)
		b = self.b(p)
		return (b - a) / max(a, b)

	def coefficient_silhouette(self):
		"""
		Method that calculates the silhouette coefficient of the clustering

		Returns:
		--------
		return : float
		"""

		sum = 0
		for c in self.clusters:
			s = 0
			for p in self.clusters[c]:
				s += self.coefficient_silhouette_i(p)
			sum += s / len(self.clusters[c])
		return sum / len(self.clusters)

	def intra_max_distance(self, cluster):
		"""
		Method that calculates the maximum distance of two points from the same cluster

		Parameters:
		-----------
		cluster : Any
		The identifier of the cluster

		Returns:
		--------
		return : float
		"""
		dmax = -1
		for i in range(len(self.clusters[cluster])):
			for j in range(i+1, len(self.clusters[cluster])):
				d = ClusteringMeasures.distance(self.clusters[cluster][i].abs, self.clusters[cluster][i].ord, self.clusters[cluster][j].abs, self.clusters[cluster][j].ord)
				if d > dmax:
					dmax = d
		return dmax 

	def cluster_centroid(self, cluster):
		"""
		Method that returns the cluster centroid

		Parameters:
		-----------
		cluster : Any
		The identifier of the cluster

		Returns:
		--------
		return : Point
		"""
		sx, sy = 0, 0
		for p in self.clusters[cluster]:
			sx += p.abs
			sy += p.ord

		return Point(sx / len(self.clusters[cluster]), sy / len(self.clusters[cluster]))

	def intra_distance_moyenne(self, cluster):
		"""
		Method that calculates the mean distance between each points of the cluster

		Parameters:
		-----------
		cluster : Any
		The identifier of the cluster

		Returns:
		--------
		return : float
		"""
		sum = 0
		for i in range(len(self.clusters[cluster])):
			for j in range(i+1, len(self.clusters[cluster])):
				sum += ClusteringMeasures.distance(self.clusters[cluster][i].abs, self.clusters[cluster][i].ord, self.clusters[cluster][j].abs, self.clusters[cluster][j].ord)
		return 2 / (len(self.clusters[cluster]) * (len(self.clusters[cluster]) - 1)) * sum

	def intra_distance_centroid(self, cluster):
		"""
		Method that calculates the mean distance between each points of the cluster and the centroid

		Parameters:
		-----------
		cluster : Any
		The identifier of the cluster

		Returns:
		--------
		return : float
		"""
		centroid = self.cluster_centroid(cluster)
		sum = 0
		for p in self.clusters[cluster]:
			sum += ClusteringMeasures.distance(p.abs, p.ord, centroid.abs, centroid.ord)
		return sum / len(self.clusters[cluster])

	def inter_min_distance(self, c1, c2):
		"""
		Method that calculates the minimum distance between two points from clusters c1 and c2

		Parameters:
		-----------
		c1, c2 : Any
		The identifiers of the two clusters

		Returns:
		--------
		return : float
		"""
		min = -1
		for p1 in self.clusters[c1]:
			for p2 in self.clusters[c2]:
				d = ClusteringMeasures.distance(p1.abs, p1.ord, p2.abs, p2.ord)
				if min == -1 or d < min:
					min = d
		return min

	def inter_centroid_distance(self, c1, c2):
		"""
		Method that calculates the distance between the centroids of two clusters

		Parameters:
		-----------
		c1, c2 : Any
		The identifiers of the two clusters

		Returns:
		--------
		return : float
		"""

		centroid1 = self.cluster_centroid(c1)
		centroid2 = self.cluster_centroid(c2)

		return ClusteringMeasures.distance(centroid1.abs, centroid1.ord, centroid2.abs, centroid2.ord)

	def indice_dunn(self, centroid = False):
		"""
		Method that calculates the Dunn score of the clustering

		Parameters:
		-----------
		centroid : bool
		Whether method should use centroids for calculation or not

		Returns:
		--------
		return : float
		"""
		if centroid:
			interFunc = self.inter_centroid_distance
			intraFunc = self.intra_distance_centroid
		else:
			interFunc = self.inter_min_distance
			intraFunc = self.intra_max_distance

		cm = list(self.clusters.keys())
		inter_min_dist = -1
		for i in range(len(cm)):
			for j in range(i+1, len(cm)):
				d = interFunc(cm[i], cm[j])
				if inter_min_dist == -1 or d < inter_min_dist:
					inter_min_dist = d
		
		intra_max_dist = -1
		for c in self.clusters:
			d = intraFunc(c)

			if intra_max_dist == -1 or d > intra_max_dist:
				intra_max_dist = d
		
		return inter_min_dist / intra_max_dist


if __name__ == "__main__":
	a = ClusteringMeasures("test.txt")
	print("Coefficient Silhouette:", a.b(a.clusters['5'][0]))
	#print("Dunn:", a.indice_dunn(False))
	#print("Dunn (centroid):", a.indice_dunn(True))