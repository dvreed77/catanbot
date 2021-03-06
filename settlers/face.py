class Face(object):
    """docstring for Face"""
    id_ = 0
    def __init__(self):
        self.id = Face.id_
        Face.id_ += 1

        self.node_neighbors = []
        self.edge_neighbors = []
        self.face_neighbors = []
        self.resource = None
        self.probability = None
        self.robber_state = False

        #for ease
        self.nn = self.node_neighbors
        self.en = self.edge_neighbors
        self.fn = self.face_neighbors

    def add_face(self, face):
        if face != self and face not in self.face_neighbors:
            self.face_neighbors.append(face)

    def add_node(self, node):
        if node not in self.node_neighbors:
            self.node_neighbors.append(node)

    def set_robber(self, state):
        self.robber = state

    def get_node_neighbors(self):
        return self.node_neighbors

    def get_edge_neighbors(self):
        return self.edge_neighbors

    def get_face_neighbors(self):
        return self.face_neighbors

    def __repr__(self):
        return "<Face: %s>" % self.id    