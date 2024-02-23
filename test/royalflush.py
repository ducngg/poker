import unittest
from poker import Poker
from cards import *
import numpy as np

def random_royalfush():
    values = [10, Card.J, Card.Q, Card.K, Card.A]
    chosen_type = int(np.random.choice(Card.ACCEPTED_TYPE))
    return [Card.Card(int(value), chosen_type) for value in values]

class TestRoyalFlush(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_royalfush())
            in_out = cards, []
            
            # print(in_out)
            
            test_method = TestRoyalFlush.gen_test(
                None, 
                Poker.royalflush(cards), 
                in_out
            )
            setattr(TestRoyalFlush, f'test_case_{i}', test_method)
        

TestRoyalFlush.gen(None, 100)
