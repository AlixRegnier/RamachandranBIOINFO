from ClusterPoint import ClusterPoint
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

if __name__ == "__main__":
	a = ClusteringMeasures("angles_1TEY_small_clust.txt")
	print("Coefficient Silhouette:", a.coefficient_silhouette())