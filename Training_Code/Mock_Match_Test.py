
from importlib.resources import path
import math
import unittest
from unittest import TestCase, mock
import sys
import os
from Customer import Customer
from Deck import Deck
from House import House
from Card import Card
from Match import Match


class Mock_Match_Test(TestCase):
    
    def test_play_match(self):
        
        player = Customer('Bob')
        house = House()
        
        match = Match(player, house)
        with mock.patch.object(match, 'compareCard') as mockCompareCard:
            mockCompareCard.return_value = 'True'
            
            
             
if __name__ == '__main__':
    unittest.main()
    