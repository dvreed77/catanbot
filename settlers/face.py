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

    def set_robber(self, state):
        self.robber = state

    def __repr__(self):
        return "<Face: %s>" % self.id    