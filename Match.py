from aifc import Error
from traceback import print_tb
from Card import Card
from Customer import Customer
from House import House
from Deck import Deck
##from OrderedEum import OrderedEnum


class Match:
    def __init__(self, score = -25):
        self.score = score
        self.round = 0
        
    def play(self):
        deck = Deck()
        deck.shuffle()
        deck.show()
        ##Customer
        player = Customer('Bod')
        player.print_player()
        card1 = deck.drawCard()
        player.draw(card1)
        player.showhand()
        ##House
        house = House()
        card2 = deck.drawCard()
        house.draw(card2)
        house.print_house()
        house.showhand()
        
        ''' compare = self.compareCard(card1, card2)
        if compare == True:
            player.score += 20
        else: player.score -= 20
        player.print_player()
        print(compare) '''
    
 
    def compareCard(self, card1, card2):
        cardShow1 = card1
        cardShow2 = card2
        
        try:
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
                    card2 = Card(int("1"), card2.suites, card2.color)
                case 'J':
                    card2 = Card(int("11"), card2.suites, card2.color)
                case 'Q': 
                    card2 = Card(int("12"), card2.suites, card2.color)
                case 'K':
                    card2 = Card(int("13"), card2.suites, card2.color)
                case 'Joker':
                    card2 = Card(int("14"), card2.suites, card2.color)
            
            match f"{card1.suites}":
                case 'Heart':
                    card1 = Card(card1.group, int("24"), card1.color)
                case 'Diamond':
                    card1 = Card(card1.group, int("23"), card1.color)
                case 'Club':
                    card1 = Card(card1.group, int("22"), card1.color)
                case 'Spade':
                    card1 = Card(card1.group, int("21"), card1.color)
                case '':
                    card1 = Card(card1.group, int("0"), card1.color)
            match f"{card2.suites}":
                case 'Heart':
                    card2 = Card(card2.group, int("24"), card2.color)
                case 'Diamond':
                    card2 = Card(card2.group, int("23"), card2.color)
                case 'Club':
                    card2 = Card(card2.group, int("22"), card2.color)
                case 'Spade':
                    card2 = Card(card2.group, int("21"), card2.color)
                case '':
                    card2 = Card(card2.group, int("0"), card2.color)
        except Error:
            print("Can't Convert")
        
        if int(card1.group) > int(card2.group):
            ''' print(f"{cardShow1.group} {cardShow1.suites} {cardShow1.color} > {cardShow2.group} {cardShow2.suites} {cardShow2.color}") '''
            return True
        elif (int(card1.group) == int(card2.group)) and (int(card1.suites) > int(card2.suites)):
            ''' print(f"{cardShow1.group} {cardShow1.suites} {cardShow1.color} > {cardShow2.group} {cardShow2.suites} {cardShow2.color}") '''
            return True
        elif  int(card1.group) < int(card2.group):
            ''' print (f"{cardShow1.group} {cardShow1.suites} {cardShow1.color} < {cardShow2.group} {cardShow2.suites} {cardShow2.color}") '''
            return False
        elif int(card1.suites) == 0 and f"{card1.color}" is 'Red' and int(card2.suites) == 0 and f"{card2.color}" is 'Black':
            ''' print(f"{cardShow1.group} {cardShow1.suites} {cardShow1.color} > {cardShow2.group} {cardShow2.suites} {cardShow2.color}") '''
            return True
        else: 
            ''' print(f"{cardShow1.group} {cardShow1.suites} {cardShow1.color} < {cardShow2.group} {cardShow2.suites} {cardShow2.color}") '''
            return False
        

        