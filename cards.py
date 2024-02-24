import numpy as np
import random
from itertools import combinations

class Card:
    """ 
    This class defines functions and constants relevant to a standard deck of playing cards.
    
    Note: A `card` is represented as a dictionary with keys `'value'` and `'type'`, where 
    `'value'` represents the card's rank and `'type'` represents its suit. This dictionary 
    format is used throughout the program to represent cards.
    
    Accepted values for `'value'` are integers ranging from 1 to 13, where:
        - 1 represents an Ace
        - 11 represents a Jack
        - 12 represents a Queen
        - 13 represents a King
    
    Accepted values for `'type'` are integers representing different suits:
        - 1: Spades
        - 2: Clubs
        - 3: Diamonds
        - 4: Hearts
    """
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
        """
        Value to value (number to string / string to number)
        """
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
        """Type to type (number to string / string to number)"""
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
        """Card to string"""
        if (card['value'] not in Card.ACCEPTED_VALUE) or (card['type'] not in Card.ACCEPTED_TYPE):
            raise ValueError("Invalid card value or type")
        return Card.v2v(card['value']) + Card.t2t(card['type'])
    
    @staticmethod 
    def s2c(s):
        """String to card (card emoji is the last 2 characters)"""
        return Card.Card(Card.v2v(s[:-2]), Card.t2t(s[-2:]))
    
    @staticmethod 
    def cs2ss(cards):
        """Cards to strings"""
        return list(map(Card.c2s, cards))

    @staticmethod 
    def ss2cs(ss):
        """Cards to strings"""
        return list(map(Card.s2c, ss))
    
    @staticmethod 
    def Card(value, type):
        """Create a card object: `dict[str, int]`"""
        if (value not in Card.ACCEPTED_VALUE or type not in Card.ACCEPTED_TYPE):
            raise ValueError("Invalid card value or type")
        return {'value': value, 'type': type}

    @staticmethod 
    def sort(cards):
        """Sort the cards in your hand(2, 3, 4, ..., 10, J, Q, K, A)."""
        sorted_cards = sorted(cards, key=lambda card: (card['value'], card['type']))
        aces = list(filter(lambda card: card['value'] == Card.A, sorted_cards))
        return Card.remaining(sorted_cards, aces) + aces
    
    @staticmethod
    def remaining(cards, takeout):
        """Returns `remaining = cards - takeout`"""
        remaining_cards = []
        for card in cards:
            if card not in takeout:
                remaining_cards.append(card)
        return remaining_cards
    
    @staticmethod 
    def highest(cards):
        """
        - A > K > Q > J > 10 > ... > 2
        - Hearts > Diamonds > Clubs > Spades
        """
        return Card.sort(cards)[-1]
    
    @staticmethod
    def compare(a, b):
        """
        - A > K > Q > J > 10 > ... > 2
        - Hearts > Diamonds > Clubs > Spades
        """
        if (a['value'] == Card.A and b['value'] != Card.A):
            return 1
        elif (a['value'] != Card.A and b['value'] == Card.A):
            return -1
        elif a['value'] > b['value']:
            return 1
        elif a['value'] < b['value']:
            return -1
        else:
            if a['type'] > b['type']:
                return 1
            elif a['type'] < b['type']:
                return -1
            else:
                return 0
            
    @staticmethod
    def compare_value(v1, v2):
        return Card.compare(Card.Card(v1, Card.SPADES), Card.Card(v2, Card.SPADES))
    
    @staticmethod
    def greater(card1, card2):
        """
        - A > K > Q > J > 10 > ... > 2
        - Hearts > Diamonds > Clubs > Spades
        """
        if Card.compare(card1, card2) == 1:
            return True
        else:
            return False
        
    @staticmethod
    def card_by_card_compare(cards1, cards2, sort=True):
        """
        Compare card by card starting from the highest card of two card lists.
        - A > K > Q > J > 10 > ... > 2
        - Hearts > Diamonds > Clubs > Spades
        """
        if sort:
            zipper = list(zip(Card.sort(cards1), Card.sort(cards2)))
        else:
            zipper = list(zip(cards1, cards2))
            
        for card1, card2 in zipper[::-1]:
            if Card.compare(card1, card2) == 1:
                return 1
            elif Card.compare(card1, card2) == -1:
                return -1
        return 0        
    
    @staticmethod
    def contains(cards, value, type=0):
        """
        Returns True if there is a card with value equal to the provided value in the cards list, optionally specifying the type. Otherwise, returns False.
        """
        if value and not type:
            return any([card['value'] == value for card in cards])
        else:
            return any([card['value'] == value and card['type'] == type for card in cards])


class Deck:
    """
    Create a deck object that serves as a deck, have the following methods: 
    - `shuffle()`: create a random list of 52 cards to `self.deck`.
    - `draw(n_cards)`: draw `n_cards` cards from the current `self.deck`.
    """
    def __init__(self) -> None:
        self.deck = []
        self.shuffle()
    def shuffle(self):
        self.deck = Card.shuffle()
    def draw(self, n_cards=1):
        cards = self.deck[:n_cards]
        self.deck = self.deck[n_cards:]
        return cards
         