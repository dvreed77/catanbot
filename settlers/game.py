#import board
import player

class Game(object):

    def __init__(self, num_players, num_bots):

        self.num_players = num_players
        self.num_bots    = num_bots
        
        self.players     = []

        for n in xrange(self.num_players):
            self.players.append(player.Player('Player' + str(n + 1), 'blue'))
