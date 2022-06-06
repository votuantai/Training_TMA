from Card import Card
from Customer import Customer
from House import House
from Deck import Deck
from OrderedEum import OrderedEnum


class Match:
    def __init__(self, score = -25):
        self.score = score

    def play(self):
        deck = Deck()
        deck.shuffle()
        deck.show()
        ##Customer
        cardOfCustomer = Customer('Bod')
        cardOfCustomer.print_player()
        card1 = cardOfCustomer.draw(deck)
        cardOfCustomer.showhand()
        ##House
        cardOfHouse = House()
        cardOfHouse.print_house()
        card2 = cardOfHouse.draw(deck)
        cardOfHouse.showhand()
        Card.compare(card1, card2)