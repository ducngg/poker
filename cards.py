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
        return sorted(cards, key=lambda card: (card['value'], card['type']))
    
    @staticmethod 
    def highest(cards):
        sorted_cards = Card.sort(cards)
        aces = list(filter(lambda card: card['value'] == Card.A, sorted_cards))
        if len(aces) > 0:
            return aces[-1]
        else:
            return sorted_cards[-1]
class Deck:
    def __init__(self) -> None:
        self.deck = Card.shuffle()
    def pop(self):
        return self.deck.pop()

