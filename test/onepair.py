import unittest
from poker import Poker
from cards import *
import numpy as np

def random_onepair():
    values = np.random.choice(Card.ACCEPTED_VALUE, size=4, replace=False)
    types = np.random.choice(Card.ACCEPTED_TYPE, size=4)
    cards = [Card.Card(int(value), int(type)) for value, type in zip(values, types)]
    
    card_chosen = np.random.choice(cards)
    
    card_pair = {'value': card_chosen['value'], 'type': card_chosen['type']}
    while card_pair['type'] == card_chosen['type']:
        card_pair['type'] = np.random.choice(Card.ACCEPTED_TYPE)
    
    cards = cards + [card_pair]
    return cards

class TestOnePair(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_onepair())
            
            counter = {}
            double_values = set()
            for card in cards:
                counter[card['value']] = counter.get(card['value'], 0) + 1
            
            for value, occurrences in counter.items():
                if occurrences == 2:
                    double_values.add(value)
            
            double_values = list(double_values)
            if Card.A in double_values:
                highest_pair_value = Card.A
            else:
                highest_pair_value = max(double_values)
            
            cards_of_double = list(filter(lambda card: card['value'] == highest_pair_value, cards))
            in_out = cards_of_double, Card.remaining(cards, cards_of_double)
            # print(list(map(Card.c2s, cards)))
            # print(Card.c2s(highest))
            
            test_method = TestOnePair.gen_test(
                None, 
                Poker.onepair(cards), 
                in_out
            )
            setattr(TestOnePair, f'test_case_{i}', test_method)
        

TestOnePair.gen(None, 100)
