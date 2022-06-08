from aifc import Error
from Card import Card
from Deck import Deck
##from OrderedEum import OrderedEnum


class Match:
    def __init__(self, player, house, score = -25):
        self.player = player
        self.house = house
        self.score = score
        self.round = 0
        
    def play(self):
        deck = Deck()
        deck.shuffle()
        
        ## Player
        card1 = deck.drawCard()
        self.player.draw(card1)
        
        ## House
        card2 = deck.drawCard()
        self.house.draw(card2)
        self.house.showhand()
        while True:
            self.round += 1
            if self.round > 0:
                self.player.setScore(self.score)
            self.player.print_player()
            Guess = input("Enter 'l' (Large) or 's' (Small): ")
            compare = self.compareCard(card1, card2)
            if (compare == True and Guess == 'l') or (compare == False and Guess == 's'):
                self.player.print_player()
                self.player.showhand()
                self.player.setShowHand()
                self.house.setShowHand()
                deck.setPutAgain(card1, card2)
                while input("Do you wanna continue? y(yes)/n(no):  ") == 'y':
                    self.round += 1
                    deck.shuffle()
                    
                    cardContinue2 = deck.drawCard()
                    self.house.draw(cardContinue2)
                    self.house.showhand()
                    self.house.setShowHand()
                    
                    cardContinue1 = deck.drawCard()
                    self.player.draw(cardContinue1)
                    
                    guess = input("Enter 'l' (Large) or 's' (Small): ")
                    compare = self.compareCard(cardContinue1, cardContinue2)
                    
                    if (compare == True and guess == 'l') or (compare == False and guess == 's'):
                        self.player.setScore(20*2)
                        self.player.print_player()
                        self.player.showhand()
                        self.player.setShowHand()
                        if self.player.getScore() > 1000:
                            print("YOU WIN")
                            break
                    else:
                        self.player.setScore(-20)
                        self.player.print_player()
                        self.player.showhand()
                        self.player.setShowHand()
                        if self.player.getScore() < 30: 
                            print("YOU LOSE")
                            break
                    deck.setPutAgain(cardContinue1, cardContinue2)
                self.round -= 1
            if self.round == 0:
                self.player.setScore(20)
                self.player.print_player()
                break
            else: 
                self.player.print_player()
                self.player.showhand()
                break
            
            
        
 
    def compareCard(self, card1, card2):
        
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
            return True
        elif (int(card1.group) == int(card2.group)) and (int(card1.suites) > int(card2.suites)):
            return True
        elif  int(card1.group) < int(card2.group):
            return False
        elif int(card1.suites) == 0 and f"{card1.color}" == 'Red' and int(card2.suites) == 0 and f"{card2.color}" == 'Black':
            return True
        else: 
            return False
        

        