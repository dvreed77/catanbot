class Node(object):
	"""docstring for Node"""
	id_ = 0
	def __init__(self, arg):
		super(Node, self).__init__()
		self.id = Node.id_
		Node.id_ += 1

		self.node_neighbors = []
		self.edge_neighbors = []
		self.face_neighbors = []
		self.building_type = None
		self.owner = None

	def set_building(self, building_type):
		self.building_type = building_type

	def set_owner(self, player):
		self.owner = player		