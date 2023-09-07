from Point import Point

class ClusterPoint(Point):
	"""
	Class that represents a point with 2 coordinates and with a cluster id
	"""
	def __init__(self, x, y, id_cluster = None):
		"""
		Constructor of the class

		Parameters:
		-----------
		x, y : float
		Coordinates of the point

		id_cluster : Any
		The identifier of the point's cluster
		"""
		super().__init__(x, y)
		self.id_cluster = id_cluster

	def __str__(self):
		"""
		Quick overview of point's datas

		Returns:
		--------
		return : str
		Information about the ClusterPoint instance
		"""
		
		return f"x: {self.abs} | y: {self.ord} | id_cluster: {self.id_cluster}"