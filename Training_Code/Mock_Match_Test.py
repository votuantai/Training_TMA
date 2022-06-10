from struct import pack
import unittest
from unittest import TestCase, mock
from Customer import Customer
from Deck import Deck
from House import House
from Match import Match
from Card import Card

class Mock_Match_Test(TestCase):
    @mock.patch('builtins.input', return_value='l')
    def test_play_match(self, _input):
        deck = Deck()
        player = Customer('Bod')
        house = House()
        
        match = Match(player, house)
        with mock.patch.object(match, 'play', new_callable= mock.PropertyMock) as mock_play:
            mock_play.compareCard.return_value = "True"
            card1 = Card('4', 'Heart', 'Red')
            mock_play.player.draw(deck.drawCard()).return_value = card1
            
            card2 = Card('3', 'Heart', 'Red')
            mock_play.house.draw(deck.drawCard()).return_value = card2

            mock_play.match.Guess.return_value = 'l'
            
            self.assertEqual(mock_play.player.getScore().return_value, 55)
            
            
            
if __name__ == '__main__':
    unittest.main()
    