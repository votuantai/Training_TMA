
##from Match import Match
import unittest
from Customer import Customer
from Deck import Deck
from House import House
from Match import Match

class Test_Player(unittest.TestCase):
    def test_player_draw(self):
        deck = Deck()
        deck.shuffle()
        
        player = Customer('Bob')
        card1 = deck.drawCard()
        self.assertIsNotNone(player)
        self.assertIsNotNone(card1)
        
        house = House()
        card2 = deck.drawCard()
        self.assertIsNotNone(house)
        self.assertIsNotNone(card2)
        
        
    def test_player_setShowHand(self):
        deck = Deck()
        deck.shuffle()
        
        player = Customer('Bob')
        card1 = deck.drawCard()
        player.draw(card1)
        self.assertIsNone(player.setShowHand())
        self.assertIsNotNone(player.getScore())
        
        house = House()
        card2 = deck.drawCard()
        house.draw(card2)
        self.assertIsNone(house.setShowHand())
        
    def test_Match(self):
        deck = Deck()
        deck.shuffle()
        
        player = Customer('Bob')
        player.print_player()
        house = House()
        house.print_house()
        
        match = Match(player, house)
        match.play()
       
       
        
if __name__ == "__main__":
    unittest.main()
    
    