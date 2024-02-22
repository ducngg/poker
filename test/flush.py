import unittest
from game import Poker
from cards import *
import numpy as np

def random_flush():
    values = np.random.choice(Card.ACCEPTED_VALUE, size=5, replace=False)
    type = np.random.choice(Card.ACCEPTED_TYPE)
    return [{'value': value, 'type': type} for value in values]

class TestFlush(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_flush())
            in_out = cards, []
            
            # print(in_out)
            
            test_method = TestFlush.gen_test(
                None, 
                Poker.flush(cards), 
                in_out
            )
            setattr(TestFlush, f'test_case_{i}', test_method)
        

TestFlush.gen(None, 1000)
