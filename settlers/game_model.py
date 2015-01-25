import random

from board import Board
from player import Player


class GameModel(object):
    """Docstring"""

    class GameMode:
        """Enumeration for keeping track of the game mode"""
        SETUP = 0
        MAIN = 1

    DEFAULT_OPTIONS = {
        "num_players": 4
    }

    # TODO: Place this in a global constants structure
    PLAYER_COLORS = ['red', 'green', 'blue', 'yellow']

    def __init__(self):
        """Initializes the game object"""
        self.active_player = None
        self.board = Board()
        self.players = []
        self.num_players = 0
        self.mode = None

    def create_new_game(self, options=None):
        """Wipes current gamestate and begins a brand new game"""
        if not options:
            options = self.DEFAULT_OPTIONS

        self.players = []
        self.num_players = options['num_players']

        random.shuffle(self.PLAYER_COLORS)

        for n in xrange(self.num_players):
            color = self.PLAYER_COLORS[n]
            self.players.append(Player(None, color, n + 1))

        self.mode = self.GameMode.SETUP
        self.active_player = random.randint(1, self.num_players)

    def get_active_player(self):
        return self.active_player

    def set_active_player(self, player_id):
        """Sets the active player to player_id. Returns true if successful"""
        result = False
        if 1 <= player_id <= self.num_players:
            self.active_player = player_id
            result = True

        return result

    def start_next_turn(self):
        """
        Ends the active players turn and starts the next players turn.
        Returns the new active player.
        """
        self.active_player += 1
        if self.active_player > self.num_players:
            self.active_player = 1
        return self.active_player

    def build_road(self, player_id, edge_id):
        """
        Builds a road for the specified player at the specified position. 
        Returns true if successful, false if not

        Arguments:
        player_id   -- the player number to build the road for
        position    -- the position of the road (an edge)
        """
        result = False
        if player_id != self.active_player:
            result = False
        else:
            edge = self.board.get_edge(edge_id)
            if not edge.get_owner():
                node_neighbors = edge.get_node_neighbors()
                edge_neighbors = edge.get_edge_neighbors()
                for node in node_neighbors.extend(edge_neighbors):
                    owner_id = node.get_owner()
                    if owner_id == player_id:
                        self.board.place_road(edge_id, player_id)
                        result = True
                        break

        return result

    def build_settlement(self, player_id, node_id):
        """
        Builds a settlement for the specified player at the specified position. 
        Returns true if successful, false if not

        Arguments:
        player_id      -- the player number to build the road for
        node_id    -- the position of the settlement (a vertex)
        """

        result = False
        
        if player_id == self.active_player:
            node = self.board.get_node(node_id)
            can_place = False
            if not node.get_owner():
                has_a_neighbor = False
                for node in node.get_node_neighbors():
                    if node.get_owner():
                        has_a_neighbor = True
                        break
                if not has_a_neighbor:
                    can_place = True

            if can_place:
                self.board.place_settlement(node_id, player_id)
                result = True

        return result