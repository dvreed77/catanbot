from board import Board
from player import Player

import random

class GameModel(object):
    """Docstring"""
    class GameMode:
        """Enumeration for keeping track of the game mode"""
        SETUP = 0
        MAIN  = 1

    DEFAULT_OPTIONS = {
        "num_players" : 4
    }

    PLAYER_COLORS = ['red', 'green', 'blue', 'yellow']

    def __init__(self):
        """Initializes the game object"""
        self.active_player = None
        self.board         = Board()
        self.players       = []
        self.num_players   = 0
        self.mode          = None


    def create_new_game(self, options=None):
        """Wipes current gamestate and begins a brand new game"""
        if not options:
            options = self.DEFAULT_OPTIONS

        self.players        = []
        self.num_players    = options['num_players']

        random.shuffle(self.PLAYER_COLORS)

        for n in xrange(self.num_players):
            color   = self.PLAYER_COLORS[n]
            self.players.append(Player(None, color, n + 1))

        self.mode           = self.GameMode.SETUP
        self.active_player  = random.randint(1, self.num_players)

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

    def build_road(self, player_id, position):
        """
        Builds a road for the specified player at the specified position. 
        Returns true if successful, false if not

        Arguments:
        player_id   -- the player number to build the road for
        position    -- the position of the road (an edge)
        """
        # Psuedocode

        # result = False
        # if its the players turn, and the position is free,
        # and (it connects to one of the players settlements or roads):
        #   put a road on the board at position
        #   result = True
        # return result

        pass

    def build_settlement(self, player_id, position):
        """
        Builds a settlement for the specified player at the specified position. 
        Returns true if successful, false if not

        Arguments:
        player_id      -- the player number to build the road for
        position    -- the position of the settlement (a vertex)
        """

        # Psuedocode

        # result = False
        # if its the players turn, and the position is free,
        # and there are no settlements at any neighboring vertices:
        #   put a settlement on the board at position
        #   result = True
        # return result

        pass