class Inventory(object):

    MAX_ROADS       = 10
    MAX_SETTLEMENTS = 10

    def __init__(self):
        self._settlements = self.MAX_SETTLEMENTS
        self._roads       = self.MAX_ROADS

    def get_roads():
        return self._roads

    def set_roads(r):
        self._roads = r
        self.__validate()

    def add_roads(r):
        self._roads += r
        self.__validate()

    def __validate():
        if self._roads > self.MAX_ROADS:
            self._roads = self.MAX_ROADS
        elif self._roads < 0:
            self._roads = 0
