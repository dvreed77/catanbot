from edge import Edge 
from face import Face 
from node import Node 


class Board(object):
    """docstring for Board"""
    def __init__(self):
        # TODO: replace with real code
        Face.id_ = 0
        Node.id_ = 0

        self.nodes = []
        self.edges = []
        self.faces = []

        self._build_board()

    def build_board2(self):
        def get_nodes(u, v):
            # 0=LEFT, 1=RIGHT
            return [
            [u, v, 0], [u, v, 1],
            [u+1, v, 0], [u-1, v, 1],
            [u+1, v-1, 0], [u-1, v+1, 1],
            ]

        def get_edges(u, v):
            # 0=WEST, 1=NORTH, 2=EAST
            return [
            [u, v, 0], [u, v, 1], [u, v, 2],
            [u+1, v-1, 0], [u, v-1, 1], [u-1, v, 2],
            ]

        def get_faces(u, v):
            return [
            [u-1, v], [u+1, v],
            [u, v-1], [u, v+1],
            [u-1, v+1], [u+1, v-1]
            ]


        start = 4
        mid = 7

        total = 2*(mid - start) + 1
        offset = 0
        for c in range(total):
            n_nodes = start - offset
            for r in range(n_nodes):
                if (c > 0) and (c < total-1) and (r > 0) and (r < n_nodes-1):
                    # print c, r+offset
                    pass



            if c > (total/2 - 1):
                offset += 1
            else:
                offset -= 1

    def build_board(self):
    def get_node(self, node_id):
        return self.nodes[node_id]

    def get_edge(self, edge_id):
        return self.edges[edge_id]

    def get_face(self, face_id):
        return self.faces[face_id]

    def place_road(self, edge_id, player_id):
        self.edges[edge_id].set_owner(player_id)

    def place_settlement(self, node_id, player_id):
        self.nodes[node_id].set_owner(player_id)

    def _build_board(self):
        from itertools import product
        def add_node(r, c):
            node = Node()
            grid[r][c] = node
            self.nodes.append(node)

        def add_face(r, c):
            if r%2:
                face = Face()
                grid[r][c] = face
                grid[r+1][c] = face
                self.faces.append(face)

        def get_neighbors(r, c):
            out = []
            for dr, dc in product([-1, 0, 1], repeat=2):
                if dr==0 and dc==0:
                    continue

                r_ = r + dr
                c_ = c + dc        

                if r_ < 0 or c_ < 0 or r_ >= nrows or c_ >= ncols:
                    continue
                
                nbr = grid[r_][c_]
                out.append(nbr)

            return list(set(out))

        def process_objs():
            for r in range(nrows):
                for c in range(ncols):
                    obj = grid[r][c]

                    if not obj:
                        continue

                    nbrs = get_neighbors(r, c)
                    for nbr in nbrs:
                        if type(nbr) == Face:
                            obj.add_face(nbr)

                        if type(nbr) == Node:
                            obj.add_node(nbr)

        # Number of nodes in start row
        start = 3

        # Number of nodes in middle row
        middle = 6

        nrows = 4*(middle - start)
        ncols = 2*middle - 1

        grid = [[None]*ncols for _ in range(nrows)]
        
        # index to start drawing nodes
        start_index = middle - start

        # when to start bringing the board back in
        half = 2*(middle-start)
        index_switch = 2

        for r in range(nrows):            
            #always start with a node
            node = 1
            for c in range(ncols):
                if (c >= start_index) and (c < (ncols-start_index)):
                    if node:
                        # its a node
                        add_node(r, c)
                    else:
                        # its a face  
                        if r != 0 and r != (nrows-1): 
                            add_face(r, c)
                    node = not node
            
            # controls whether to move the offset in or out or stay the same
            if r > half-1:
                if (index_switch%2 == 0):            
                    start_index += 1
                index_switch += 1
            else:
                if (index_switch%2 == 0):            
                    start_index -= 1
                index_switch += 1

        # once board is filled, reiterate to process connections
        process_objs()