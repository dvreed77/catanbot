class Command(object):
    """docstring"""

    # Abstract method
    def execute(self):
        pass

class PlaceSettlementCommand(Command):
    """docstring"""
    def __init__(self, player, position):
        pass

    def execute(self):
        pass

class PlaceRoadCommand(Command):
    """docstring"""
    def __init__(self):
        pass

    def execute(self):
        pass

class EndTurnCommand(Command):
    """docstring"""
    def __init__(self):
        pass

    def execute(self):
        pass