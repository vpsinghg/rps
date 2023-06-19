import abc
from typing import List
import logging

class GameStrategy(abc.ABC):
    """
    A base class for all game strategies.
    """
    @abc.abstractmethod
    def compare(self, choice1, choice2) -> str:
        """
        Compare two options and return the result of the game.
        """
        pass
    
    @abc.abstractmethod
    def getOptions(self) -> List[str]:
        """
        Return a list of available options.
        """
        pass
    
    @abc.abstractmethod
    def getVictoryGraph(self):
        """
        Return a which Option can which of available options.
        """
        pass
