from settlers.edge import Edge 
from settlers.face import Face 
from settlers.node import Node 


class Board(object):
	"""docstring for Board"""
	def __init__(self, arg):
		super(Board, self).__init__()

		# TODO: replace with real code
		self.nodes = [Node(), Node()]
		self.edges = [Edge(), Edge()]
		self.faces = [Face(), Face()]

		
