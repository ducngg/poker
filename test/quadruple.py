import unittest
from game import Poker
from cards import *
import numpy as np

def random_quadruple():
    values = np.random.choice(Card.ACCEPTED_VALUE, size=2, replace=False)
    types = np.random.choice(Card.ACCEPTED_TYPE, size=2)
    cards = [{'value': int(value), 'type': int(type)} for value, type in zip(values, types)]
    
    card_chosen = np.random.choice(cards)
    
    other_three_cards = [{'value': card_chosen['value'], 'type': type} for type in Card.ACCEPTED_TYPE if type != card_chosen['type']]
    
    cards = cards + other_three_cards
    return cards

class TestQuadruple(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_quadruple())
            
            counter = {}
            for card in cards:
                counter[card['value']] = counter.get(card['value'], 0) + 1
            
            for value, occurrences in counter.items():
                if occurrences == 4:
                    cards_of_triple = list(filter(lambda card: card['value'] == value, cards))
                    in_out = cards_of_triple, Card.remaining(cards, cards_of_triple)
            
            test_method = TestQuadruple.gen_test(
                None, 
                Poker.quadruple(cards), 
                in_out
            )
            setattr(TestQuadruple, f'test_case_{i}', test_method)
        
TestQuadruple.gen(None, 100)
