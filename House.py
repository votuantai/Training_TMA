from Player import Player


class House(Player):
    def __init__(self, name = "F88"):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        return self.hand.append(deck.drawCard())
    
    def showhand(self):
        for card in self.hand:
            print(f"{card.group} {card.suites} {card.color}")
    
    def print_house(self):
        print("House Name:", self.name)
