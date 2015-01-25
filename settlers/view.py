from abc import ABCMeta, abstractmethod


class View(object):
    """Docstring"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def display_road(self, edge_id):
        """Docstring"""
        pass

    @abstractmethod
    def display_settlement(self, node_id):
        """Docstring"""
        pass

    @abstractmethod
    def display_message(self, message):
        """Docstring"""
        pass

