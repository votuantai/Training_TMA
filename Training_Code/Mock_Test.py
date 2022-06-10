import unittest
from unittest import TestCase, mock
from Customer import Customer
from House import House
from Match import Match
from Card import Card
        
class Mock_Test(TestCase):
    def test_mock_check_compare_greaterthan(self):  
        ## Player name: Bob
        player = Customer('Bob')
        
        ## House
        house = House()
        
        ## Match
        match = Match(player, house)
        
        
        ## Cards mock
        playerJokerCard1 = Card('Joker', '', 'Red')
        houseKCard1 = Card('K', 'Heart', 'Red')
       
        mockCompareCards1 = mock.Mock(return_value= match.compareCard(playerJokerCard1, houseKCard1))
       
        playerJokerCard2 = Card('Joker', '', 'Red')
        houseKCard2 = Card('Joker', '', 'Black')
        
        mockCompareCards2 = mock.Mock(return_value= match.compareCard(playerJokerCard2, houseKCard2))
        
        
        self.assertEqual(mockCompareCards1.return_value, mockCompareCards2.return_value)
        
        
if __name__ == '__main__':
    unittest.main()
    