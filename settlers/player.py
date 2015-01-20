from inventory import Inventory

class Player(object):
    """Docstring HELP HOW DOES IT WORK"""

    def __init__(self, name, color, _id):

        self.id         = _id
        self.color      = color
        self.inventory  = Inventory()

        if name == None:
            self.name  = 'Player ' + str(self.id)