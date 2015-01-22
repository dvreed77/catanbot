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

    def get_owner(self):
        return self.owner

    def get_node_neighbors(self):
        return self.node_neighbors

    def get_edge_neighbors(self):
        return self.edge_neighbors

    def get_face_neighbors(self):
        return self.face_neighbors