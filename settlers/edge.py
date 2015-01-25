class Edge(object):
    """docstring for Edge"""
    id_ = 0
    def __init__(self, c, r, wne):
        self.id = Edge.id_
        Edge.id_ += 1

        self.c = c
        self.r = r
        self.wne = wne
        self.node_neighbors = []
        self.edge_neighbors = []
        self.face_neighbors = []
        self.owner = None

        #for ease
        self.nn = self.node_neighbors
        self.en = self.edge_neighbors
        self.fn = self.face_neighbors   

    def add_face(self, face):
        if face not in self.face_neighbors:
            self.face_neighbors.append(face)

    def add_node(self, node):
        if node not in self.node_neighbors:
            self.node_neighbors.append(node)

    def add_edge(self, edge):
        if edge != self and edge not in self.edge_neighbors:
            self.edge_neighbors.append(edge)

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

    def __repr__(self):
        return "<E%0i: %s,%s,%s>" % (self.id, self.c, self.r, self.wne)