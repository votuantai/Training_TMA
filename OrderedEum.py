from collections import namedtuple
import enum

class OrderedEnum(enum.Enum):
    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.value < other.value
        return NotImplemented
    
    

Rank = OrderedEnum('Rank', ['one', 'two', 'three', 'four', 'five', 'six',
                        'seven', 'eight', 'nine', 'jack', 'queen','king', 'ace'])
Suit = OrderedEnum('Suit', ['clubs', 'diamonds', 'hearts', 'spades'])
CardValue = namedtuple('CardValue', ['rank', 'suit'])