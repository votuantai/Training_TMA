from Player import Player


class Customer(Player):
    def __init__(self, name, score = 60):
        self.name = name
        self.score = score
        self.hand = []

    def draw(self, deck):
        return self.hand.append(deck.drawCard())
    
    def showhand(self):
        for card in self.hand:
            print(f"{card.group} {card.suites} {card.color}")

    def print_player(self):
        print(f"Player Name: {self.name} // Score: {self.score}")