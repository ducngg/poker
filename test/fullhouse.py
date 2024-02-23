import unittest
from poker import Poker
from cards import *
import numpy as np

def random_fullhouse():
    values = np.random.choice(Card.ACCEPTED_VALUE, size=2, replace=False)
    types = np.random.choice(Card.ACCEPTED_TYPE, size=2)
    cards = [Card.Card(int(value), int(type)) for value, type in zip(values, types)]
    
    card_chosen_for_triple = cards[0]
    
    other_two_cards = [
        Card.Card(card_chosen_for_triple['value'], card_chosen_for_triple['type']),
        Card.Card(card_chosen_for_triple['value'], card_chosen_for_triple['type'])
    ]
    
    while other_two_cards[0]['type'] == card_chosen_for_triple['type']:
        other_two_cards[0]['type'] = np.random.choice(Card.ACCEPTED_TYPE)
        
    while other_two_cards[1]['type'] == card_chosen_for_triple['type']:
        other_two_cards[1]['type'] = np.random.choice(Card.ACCEPTED_TYPE)
        
    card_chosen_for_double = cards[1]
    
    other_one_card = {'value': card_chosen_for_double['value'], 'type': card_chosen_for_double['type']}
    
    while other_one_card['type'] == card_chosen_for_double['type']:
        other_one_card['type'] = np.random.choice(Card.ACCEPTED_TYPE)
    
    cards = cards + other_two_cards + [other_one_card]
    return cards

class TestFullhouse(unittest.TestCase):
    def gen_test(self, result, expected):
        def test_method(self):
            self.assertEqual(result, expected)
        return test_method
    
    def gen(self, N=100):        
        for i in range(N):
            cards = Card.sort(random_fullhouse())
            
            if Poker.triple(cards)[0] and Poker.twopairs(cards)[0]:
                in_out = cards, []
            else:
                in_out = [], cards
            
            # print(in_out)
                            
            test_method = TestFullhouse.gen_test(
                None, 
                Poker.fullhouse(cards), 
                in_out
            )
            setattr(TestFullhouse, f'test_case_{i}', test_method)
        

TestFullhouse.gen(None, 100)
