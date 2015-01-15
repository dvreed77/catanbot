class Edge(object):
    """docstring for Edge"""
    id_ = 0
    def __init__(self):
        self.id = Edge.id_
        Edge.id_ += 1

        self.node_neighbors = []
        self.edge_neighbors = []
        self.face_neighbors = []
        self.owner = None

        #for ease
        self.nn = self.node_neighbors
        self.en = self.edge_neighbors
        self.fn = self.face_neighbors   

    def set_owner(self, player):
        self.owner = player     