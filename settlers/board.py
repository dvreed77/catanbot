from settlers.edge import Edge
from settlers.face import Face
from settlers.node import Node

print 'dave'
class HexBoard(object):
    def __init__(self):
        self.cols = {
            -3: [0, 3],
            -2: [-1, 3],
            -1: [-2, 3],
            0: [-3, 3],
            1: [-3, 2],
            2: [-3, 1],
            3: [-3, 0]
        }
        self.u_min = -3
        self.u_max = 3

    def get_face(self, u, v):
        if (u < self.u_min) or (u > self.u_max):
            return None

        if (v < self.cols[u][0]) or (v > self.cols[u][1]):
            return None

        return 'Face'

class Board(object):
    """docstring for Board"""
    def __init__(self):
        # TODO: replace with real code
        Face.id_ = 0
        Node.id_ = 0

        self.nodes = []
        self.edges = []
        self.faces = []

        self.build_board2()

    def build_board2(self):
        def get_nodes_from_face(u, v):
            return [
                out[u][v]['L'], out[u][v]['R'],
                out[u+1][v]['L'], out[u-1][v]['R'],
                out[u+1][v-1]['L'], out[u-1][v+1]['R']
            ]

        def get_edges_from_face(u, v):
            return [
                out[u][v]['W'], out[u][v]['N'], out[u][v]['E'],
                out[u+1][v-1]['W'], out[u][v-1]['N'], out[u-1][v]['E'],
            ]

        def get_faces_from_face(u, v):
            return [
                out[u-1][v]['F'], out[u+1][v]['F'],
                out[u][v-1]['F'], out[u][v+1]['F'],
                out[u-1][v+1]['F'], out[u+1][v-1]['F']
            ]
        def get_nodes_from_node(u, v, lr):
            if lr == 'R':
                return [
                    out[u+1][v]['L'],
                    out[u+1][v-1]['L'],
                    out[u+2][v-1]['R'],
                ]
            else:
                return [
                    out[u-1][v]['R'],
                    out[u-1][v+1]['R'],
                    out[u-2][v+1]['L'],
                ]

        def get_edges_from_node(u, v, lr):
            if lr == 'R':
                return [
                    out[u][v]['E'],
                    out[u+1][v-1]['W'],
                    out[u+1][v-1]['N'],
                ]
            else:
                return [
                    out[u-1][v]['E'],
                    out[u-1][v]['N'],
                    out[u][v]['W'],
                ]

        def get_faces_from_node(u, v, lr):
            if lr == 'R':
                return [
                    out[u][v]['F'],
                    out[u+1][v]['F'],
                    out[u+1][v-1]['F'],
                ]
            else:
                return [
                    out[u][v]['F'],
                    out[u-1][v]['F'],
                    out[u-1][v+1]['F'],
                ]
        def get_nodes_from_edge(u, v, wne):
            if wne == 'W':
                return [
                    out[u][v]['L'],
                    out[u-1][u+1]['R'],
                ]
            elif wne == 'N':
                return [
                    out[u+1][v]['L'],
                    out[u-1][v+1]['R'],
                ]
            else:
                return [
                    out[u+1][v]['L'],
                    out[u][v]['R'],
                ]

        def get_edges_from_edge(u, v, wne):
            if wne == 'W':
                return [
                    out[u-1][v]['N'],
                    out[u-1][v]['E'],
                    out[u][v]['N'],
                    out[u-1][v+1]['E'],
                ]
            elif wne == 'N':
                return [
                    out[u][v]['W'],
                    out[u][v]['E'],
                    out[u-1][v+1]['E'],
                    out[u+1][v]['W'],
                ]
            else:
                return [
                    out[u][v]['N'],
                    out[u+1][v]['W'],
                    out[u+1][v-1]['N'],
                    out[u+1][v-1]['W'],
                ]

        def get_faces_from_edge(u, v, wne):
            if wne == 'W':
                return [
                    out[u][v]['F'],
                    out[u-1][v+1]['F'],
                ]
            elif wne == 'N':
                return [
                    out[u][v]['F'],
                    out[u][v+1]['F'],
                ]
            else:
                return [
                    out[u][v]['F'],
                    out[u+1][v]['F'],
                ]


        start = -3
        n_rows = 4
        offset = 0
        columns = range(start, -start+1)
        n_cols = len(columns)

        out = {}
        for c in columns:
            out[c] = {}
            # print c <= columns[n_cols/2]
            if c <= columns[n_cols/2]:
                n_rows += 1
            else:
                offset += 1
                n_rows -= 1

            rows = range(start+offset, start+n_rows+offset-1)
            # print rows
            for r in rows:
                # print c,
                out[c][-r] = {
                    'F': Face(),
                    'L': Node(),
                    'R': Node(),
                    'W': Edge(),
                    'N': Edge(),
                    'E': Edge()
                }

        print get_nodes_from_edge(0, 0, 'N')
        print get_edges_from_edge(0, 0, 'N')
        print get_faces_from_edge(0, 0, 'N')
        print '----'
        print get_nodes_from_face(0, 0)
        print get_edges_from_face(0, 0)
        print get_faces_from_face(0, 0)
        print '----'
        print get_nodes_from_node(0, 0, 'L')
        print get_edges_from_node(0, 0, 'L')
        print get_faces_from_node(0, 0, 'L')
        # print get_edges(0,0)
        # print get_faces(0,0)
        # print out
        # mid = 7
        #
        # total = 2*(mid - start) + 1
        # offset = 0
        # for c in range(total):
        #     n_nodes = start - offset
        #     for r in range(n_nodes):
        #         if (c > 0) and (c < total-1) and (r > 0) and (r < n_nodes-1):
        #             # print c, r+offset
        #             pass
        #
        #
        #
        #     if c > (total/2 - 1):
        #         offset += 1
        #     else:
        #         offset -= 1

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

if __name__ == "__main__":
    # bd = Board()
    hb = HexBoard()
    print hb.get_face(0,0)
    print hb.get_face(-3,3)
    print hb.get_face(-3,-3)