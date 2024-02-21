import unittest
from game import Poker
from cards import *
import numpy as np

def random_twopairs():
    values = np.random.choice(Card.ACCEPTED_VALUE, size=3, replace=False)
    types = np.random.choice(Card.ACCEPTED_TYPE, size=3)
    cards = [{'value': int(value), 'type': int(type)} for value, type in zip(values, types)]
    
    cards_chosen = np.random.choice(cards, size=2, replace=False)
    
    first_card_pair = {'value': cards_chosen[0]['value'], 'type': cards_chosen[0]['type']}
    while first_card_pair['type'] == cards_chosen[0]['type']:
        first_card_pair['type'] = np.random.choice(Card.ACCEPTED_TYPE)
        
    second_card_pair = {'value': cards_chosen[1]['value'], 'type': cards_chosen[1]['type']}
    while second_card_pair['type'] == cards_chosen[1]['type']:
        second_card_pair['type'] = np.random.choice(Card.ACCEPTED_TYPE)
        
    cards = cards + [first_card_pair, second_card_pair]
    return cards

class TestTwoPairs(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_twopairs())
            # Select highest
            counter = {}
            double_values = set()
            for card in cards:
                counter[card['value']] = counter.get(card['value'], 0) + 1
            
            for value, occurrences in counter.items():
                if occurrences == 2:
                    double_values.add(value)
            
            double_values = list(double_values)
            
            cards_of_first_pair = list(filter(lambda card: card['value'] in double_values and card['value'] == double_values[0], cards))
            cards_of_second_pair = list(filter(lambda card: card['value'] in double_values and card['value'] == double_values[1], cards))

            highests = [Card.sort([Card.highest(cards_of_first_pair), Card.highest(cards_of_second_pair)])]
            # End select highest
            print(list(map(Card.c2s, cards)))
            print(list(map(Card.c2s, highests)))
            test_method = TestTwoPairs.gen_test(
                None, 
                Poker.onepair(cards), 
                (True, highests)
            )
            setattr(TestTwoPairs, f'test_case_{i}', test_method)
        

TestTwoPairs.gen(None, 100)
