import numpy as np
import random

class Card:
    A = 1
    J = 11
    Q = 12
    K = 13
    S = 1
    C = 2
    D = 3
    H = 4
    SPADES = 1
    CLUBS = 2
    DIAMONDS = 3
    HEARTS = 4
    
    ACCEPTED_VALUE = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
    ACCEPTED_TYPE = [SPADES, CLUBS, DIAMONDS, HEARTS]
    
    FULL = []
    for T in ACCEPTED_TYPE:
        for V in ACCEPTED_VALUE:
            FULL.append({'value': V, 'type': T})
        
    @staticmethod    
    def shuffle():
        res = Card.FULL.copy()
        random.shuffle(res)
        return res
    
    @staticmethod 
    def v2v(v):
        if v == 'A':
            return 1
        if v == 'J':
            return 11
        if v == 'Q':
            return 12
        if v == 'K':
            return 13
        if v == Card.A:
            return 'A'
        if v == Card.J:
            return 'J'
        if v == Card.Q:
            return 'Q'
        if v == Card.K:
            return 'K'
        if isinstance(v, str):
            return int(v)
        if isinstance(v, int):
            return str(v)
        raise ValueError("Invalid card value")
    
    @staticmethod 
    def t2t(t):
        if t == '♠️':
            return Card.S
        if t == '♣️':
            return Card.C
        if t == '♦️':
            return Card.D
        if t == '♥️':
            return Card.H
        if t == Card.S:
            return '♠️'
        if t == Card.C:
            return '♣️'
        if t == Card.D:
            return '♦️'
        if t == Card.H:
            return '♥️'
        raise ValueError("Invalid card type")
    
    @staticmethod 
    def c2s(card):
        if (card['value'] not in Card.ACCEPTED_VALUE) or (card['type'] not in Card.ACCEPTED_TYPE):
            raise ValueError("Invalid card value or type")
        return Card.v2v(card['value']) + Card.t2t(card['type'])
    
    @staticmethod 
    def Card(value, type):
        if (value not in Card.ACCEPTED_VALUE or type not in Card.ACCEPTED_TYPE):
            raise ValueError("Invalid card value or type")
        return {'value': value, 'type': type}

    @staticmethod 
    def sort(cards):
        sorted_cards = sorted(cards, key=lambda card: (card['value'], card['type']))
        aces = list(filter(lambda card: card['value'] == Card.A, sorted_cards))
        return Card.remaining(sorted_cards, aces) + aces
    
    @staticmethod
    def remaining(cards, takeout):
        remaining_cards = []
        for card in cards:
            if card not in takeout:
                remaining_cards.append(card)
        return remaining_cards
    
    @staticmethod 
    def highest(cards):
        return Card.sort(cards)[-1]
    
    @staticmethod
    def compare(a, b):
        if a['value'] > b['value'] or a['value'] == Card.A and b['value'] != Card.A:
            return 1
        elif a['value'] < b['value'] or a['value'] != Card.A and b['value'] == Card.A:
            return -1
        else:
            if a['type'] > b['type']:
                return 1
            elif a['type'] < b['type']:
                return -1
            else:
                return 0
    
    @staticmethod
    def greater(a, b):
        if Card.compare(a, b) == 1:
            return True
        else:
            return False
        
class Deck:
    def __init__(self) -> None:
        self.deck = Card.shuffle()
    def pop(self):
        return self.deck.pop()

