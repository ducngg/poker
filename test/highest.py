import unittest
from poker import Poker
from cards import *
import numpy as np

def random_highest():
    values = np.random.choice(Card.ACCEPTED_VALUE, size=5, replace=False)
    types = np.random.choice(Card.ACCEPTED_TYPE, size=5)
    return [{'value': value, 'type': type} for value, type in zip(values, types)]

class TestHighest(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_highest())
            in_out = [Card.highest(cards)], Card.remaining(cards, [Card.highest(cards)])
            
            # print(in_out)
            
            test_method = TestHighest.gen_test(
                None, 
                Poker.highest(cards), 
                in_out
            )
            setattr(TestHighest, f'test_case_{i}', test_method)
        

TestHighest.gen(None, 100)
