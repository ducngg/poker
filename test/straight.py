import unittest
from game import Poker
from cards import *
import numpy as np

def random_straight():
    init_value = np.random.choice(Card.ACCEPTED_VALUE[:10]) # can't have a straight starts from J, Q, K
    if init_value == 10:
        values = [10, Card.J, Card.Q, Card.K, Card.A]
    else:
        values = [i for i in range(init_value, init_value+5)]
    return [{'value': value, 'type': np.random.choice(Card.ACCEPTED_TYPE)} for value in values]

class TestStraight(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_straight())
            
            # A 2 3 4 5
            if cards[0]['value'] == Card.A and cards[-1]['value'] == 5:
                highest = cards[-1]
            else: 
                highest = Card.highest(cards)
            test_method = TestStraight.gen_test(
                None, 
                Poker.straight(cards), 
                (True, [highest])
            )
            setattr(TestStraight, f'test_case_{i}', test_method)
        

TestStraight.gen(None, 3000)
