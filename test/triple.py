import unittest
from poker import Poker
from cards import *
import numpy as np

def random_triple():
    values = np.random.choice(Card.ACCEPTED_VALUE, size=3, replace=False)
    types = np.random.choice(Card.ACCEPTED_TYPE, size=3)
    cards = [{'value': int(value), 'type': int(type)} for value, type in zip(values, types)]
    
    card_chosen = np.random.choice(cards)
    
    other_two_cards = [
        {'value': card_chosen['value'], 'type': card_chosen['type']},
        {'value': card_chosen['value'], 'type': card_chosen['type']}
    ]
    
    while other_two_cards[0]['type'] == card_chosen['type']:
        other_two_cards[0]['type'] = np.random.choice(Card.ACCEPTED_TYPE)
        
    while other_two_cards[1]['type'] == card_chosen['type']:
        other_two_cards[1]['type'] = np.random.choice(Card.ACCEPTED_TYPE)
    
    cards = cards + other_two_cards
    return cards

class TestTriple(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_triple())
            
            counter = {}
            for card in cards:
                counter[card['value']] = counter.get(card['value'], 0) + 1
            
            for value, occurrences in counter.items():
                if occurrences == 3:
                    cards_of_triple = list(filter(lambda card: card['value'] == value, cards))
                    in_out = cards_of_triple, Card.remaining(cards, cards_of_triple)
                            
            test_method = TestTriple.gen_test(
                None, 
                Poker.triple(cards), 
                in_out
            )
            setattr(TestTriple, f'test_case_{i}', test_method)
        

TestTriple.gen(None, 100)
