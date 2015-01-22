class Node(object):
    """docstring for Node"""
    id_ = 0
    def __init__(self):
        self.id = Node.id_
        Node.id_ += 1

        self.node_neighbors = []
        self.edge_neighbors = []
        self.face_neighbors = []
        self.building_type = None
        self.owner = None

        #for ease
        self.nn = self.node_neighbors
        self.en = self.edge_neighbors
        self.fn = self.face_neighbors

    def add_face(self, face):
        if face not in self.face_neighbors:
            self.face_neighbors.append(face)

    def add_node(self, node):
        if node != self and node not in self.node_neighbors:
            self.node_neighbors.append(node)

    def set_building(self, building_type):
        self.building_type = building_type

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
        return "<Node: %s>" % self.id    