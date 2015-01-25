from game_model import GameModel


class GameController(object):
    """Docstring"""
    def __init__(self, game_model, view):
        """
        @type game_model: GameModel
        @type view: View
        """
        self.game_model = game_model
        self.view = view

    def select_edge(self, edge_id):
        """Docstring"""
        active_player = self.game_model.get_active_player()
        if self.game_model.build_road(active_player, edge_id):
            self.view.display_road(edge_id)
        else:
            # TODO: Place this message in a global constants structure
            self.view.display_message("You can't build a road there ya dunce")

    def select_node(self, node_id):
        """Docstring"""
        active_player = self.game_model.get_active_player()
        if self.game_model.build_settlement(active_player, node_id):
            self.view.display_settlement(node_id)
        else:
            # TODO: Place this message in a global constants structure
            self.view.display_message("You can't build a settlement there ya dummy")

