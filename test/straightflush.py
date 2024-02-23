import unittest
from poker import Poker
from cards import *
import numpy as np

def random_straightfush():
    init_value = np.random.choice(Card.ACCEPTED_VALUE[:10]) # can't have a straight starts from J, Q, K
    if init_value == 10:
        values = [10, Card.J, Card.Q, Card.K, Card.A]
    else:
        values = [i for i in range(init_value, init_value+5)]
    chosen_type = int(np.random.choice(Card.ACCEPTED_TYPE))
    return [Card.Card(int(value), chosen_type) for value in values]

class TestStraightFlush(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_straightfush())
            in_out = cards, []
            
            # print(in_out)
            
            test_method = TestStraightFlush.gen_test(
                None, 
                Poker.straightflush(cards), 
                in_out
            )
            setattr(TestStraightFlush, f'test_case_{i}', test_method)
        

TestStraightFlush.gen(None, 100)
