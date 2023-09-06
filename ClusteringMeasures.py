from ClusterPoint import ClusterPoint
from Point import Point
from typing import List, Union

class ClusteringMeasures:
	def __init__(self, classified_points : Union[List[ClusterPoint], str]):
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
		return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

	def a(self, p):
		sum = 0
		count = 0
		for v in self.clusters[p.id_cluster]:
			if v != p:
				sum += ClusteringMeasures.distance(p.x, p.y, v.x, v.y)
				count += 1
		
		return sum / count

	def b(self, p):

		#min_cluster = None
		min_dist = -1
		dist = 0

		for c in self.clusters.keys() - {p.id_cluster}:
			sum = 0
			for v in self.clusters[c]:
				sum += ClusteringMeasures.distance(p.x, p.y, v.x, v.y)
			
			dist = sum / len(self.clusters[c])

			if min_dist < 0 or dist < min_dist:
				min_dist = dist
				#min_cluster = c
		
		return min_dist

	def coefficient_silhouette_i(self, p):
		a = self.a(p)
		b = self.b(p)
		return (b - a) / max(a, b)

	def coefficient_silhouette(self):
		sum = 0
		for c in self.clusters:
			s = 0
			for p in self.clusters[c]:
				s += self.coefficient_silhouette_i(p)
			sum += s / len(self.clusters[c])
		return sum / len(self.clusters)

	def intra_max_distance(self, cluster):
		dmax = -1
		for i in range(len(self.clusters[cluster])):
			for j in range(i+1, len(self.clusters[cluster])):
				d = ClusteringMeasures.distance(self.clusters[cluster][i].x, self.clusters[cluster][i].y, self.clusters[cluster][j].x, self.clusters[cluster][j].y)
				if d > dmax:
					dmax = d
		return dmax 

	def cluster_centroid(self, cluster):
		sx, sy = 0, 0
		for p in self.clusters[cluster]:
			sx += p.x
			sy += p.y

		return Point(sx / len(self.clusters[cluster]), sy / len(self.clusters[cluster]))

	def intra_distance_moyenne(self, cluster):
		sum = 0
		for i in range(len(self.clusters[cluster])):
			for j in range(i+1, len(self.clusters[cluster])):
				sum += ClusteringMeasures.distance(self.clusters[cluster][i].x, self.clusters[cluster][i].y, self.clusters[cluster][j].x, self.clusters[cluster][j].y)
		return 2 / (len(self.clusters[cluster]) * (len(self.clusters[cluster]) - 1)) * sum

	def intra_distance_centroid(self, cluster):
		centroid = self.cluster_centroid(cluster)
		sum = 0
		for p in self.clusters[cluster]:
			sum += ClusteringMeasures.distance(p.x, p.y, centroid.x, centroid.y)
		return sum / len(self.clusters[cluster])

	def inter_min_distance(self, c1, c2):
		min = -1
		for p1 in self.clusters[c1]:
			for p2 in self.clusters[c2]:
				d = ClusteringMeasures.distance(p1.x, p1.y, p2.x, p2.y)
				if min == -1 or d < min:
					min = d
		return min

	def inter_centroid_distance(self, c1, c2):
		centroid1 = self.cluster_centroid(c1)
		centroid2 = self.cluster_centroid(c2)

		return ClusteringMeasures.distance(centroid1.x, centroid1.y, centroid2.x, centroid2.y)
	def indice_dunn(self, centroid = False):
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
	a = ClusteringMeasures("angles_1TEY_small_clust.txt")
	print("Coefficient Silhouette:", a.coefficient_silhouette())
	print("Dunn:", a.indice_dunn(False))
	print("Dunn (centroid):", a.indice_dunn(True))