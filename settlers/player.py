
class Player(object):

    _id = 0

    def __init__(self, name, color):
        self.name  = name
        self.color = color
        self.id    = Player._id
        Player._id += 1