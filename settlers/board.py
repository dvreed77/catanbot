from settlers.edge import Edge 
from settlers.face import Face 
from settlers.node import Node 


class Board(object):
    """docstring for Board"""
    def __init__(self):
        # TODO: replace with real code
        Face.id_ = 0
        Node.id_ = 0

        self.nodes = []
        self.edges = []
        self.faces = []

        self.build_board()

    def build_board(self):
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