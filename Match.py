from Card import Card
from Card import Card
from Customer import Customer
from House import House
from Deck import Deck
##from OrderedEum import OrderedEnum


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
        card1 = deck.drawCard()
        cardOfCustomer.draw(card1)
        cardOfCustomer.showhand()
        ##House
        cardOfHouse = House()
        card2 = deck.drawCard()
        cardOfHouse.draw(card2)
        cardOfHouse.print_house()
        cardOfHouse.showhand()
        self.compare(card1, card2)
        
    def compare(self, card1, card2):
        cardShow1 = card1
        cardShow2 = card2
        
        match f"{card1.group}":
            case 'A':
                card1 = Card(int("1"), card1.suites, card1.color)
            case 'J':
                card1 = Card(int("11"), card1.suites, card1.color)
            case 'Q': 
                card1 = Card(int("12"), card1.suites, card1.color)
            case 'K':
                card1 = Card(int("13"), card1.suites, card1.color)
            case 'Joker':
                card1 = Card(int("14"), card1.suites, card1.color)
        match f"{card2.group}":
            case 'A':
                card2 = Card(int("1"), card1.suites, card1.color)
            case 'J':
                card2 = Card(int("11"), card1.suites, card1.color)
            case 'Q': 
                card2 = Card(int("12"), card1.suites, card1.color)
            case 'K':
                card2 = Card(int("13"), card1.suites, card1.color)
            case 'Joker':
                card2 = Card(int("14"), card1.suites, card1.color)
        
        match f"{card1.suites}":
            case 'Heart':
                card1 = Card(card1.group, int("24"), card1.color)
            case 'Diamond':
                card1 = Card(card1.group, int("23"), card1.color)
            case 'Club':
                card1 = Card(card1.group, int("22"), card1.color)
            case 'Spade':
                card1 = Card(card1.group, int("21"), card1.color)
        match f"{card2.suites}":
            case 'Heart':
                card2 = Card(card2.group, int("24"), card1.color)
            case 'Diamond':
                card2 = Card(card2.group, int("23"), card1.color)
            case 'Club':
                card2 = Card(card2.group, int("22"), card1.color)
            case 'Spade':
                card2 = Card(card2.group, int("21"), card1.color)
                
        ##print(f"{int(card1.group)} {int(card2.group)}")
        if int(card1.group) > int(card2.group):
            print(f"{cardShow1.group} > {cardShow2.group}")
        elif (int(card1.group) == int(card2.group)) and (int(card1.suites) > int(card2.suites)):
            print(f"{cardShow1.suites} > {cardShow2.suites}")
        else: return False
        
        

        