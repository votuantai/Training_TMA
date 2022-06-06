
from abc import ABC, abstractmethod
class Player(ABC):
    @abstractmethod
    def draw(self, deck):
        pass
    
    @abstractmethod
    def showhand(self):
        pass