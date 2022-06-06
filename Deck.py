from Card import Card
import random as rd
from msilib.schema import Error 
class Deck():
    def __init__(self):
        self.cards = []
        Suites = ('Heart', 'Diamond', 'Club', 'Spade')
        Group = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'Joker')
        for group in Group:
            if (group == 'Joker'):
                card = Card(group, '', 'Red')
                self.cards.append(card)
                card = Card(group, '', 'Black')
                self.cards.append(card)
            for suites in Suites:
                if (group == 'Joker'): continue
                elif (suites == "Club" or suites == "Spade"):
                    card = Card(group, suites, 'Black')
                    self.cards.append(card)
                else:
                    card = Card(group, suites, 'Red')
                    self.cards.append(card)
                    
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = rd.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def drawCard(self):
        try:
            draw = self.cards.pop()
            return draw
        except Error:
            print("Error at drawCard")
            
    def show(self):
        for card in self.cards:
            card.print_card()
        print(len(self.cards))