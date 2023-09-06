from Point import Point

class ClusterPoint(Point):
	def __init__(self, x, y, id_cluster = None):
		super().__init__(x, y)
		self.id_cluster = id_cluster

	def __str__(self):
		return f"x: {self.x} | y: {self.y} | id_cluster: {self.id_cluster}"