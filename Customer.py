from Player import Player

class Customer(Player):
    def __init__(self, name):
        self.score = 60
        self.name = name
        self.hand = []

    def draw(self, card):
        return self.hand.append(card)
    
    def showhand(self):
        for card in self.hand:
            print(f"{card.group} {card.suites} {card.color}")
            
    def setShowHand(self):
        return self.hand.clear()
    
    def setScore(self, score):
        self.score += score
        
    def getScore(self):
        return self.score

    def print_player(self):
        print(f"Player Name: {self.name} // Score: {self.getScore()} ")