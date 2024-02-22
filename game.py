from cards import *

class Poker:
    """
    This class consist of functions that check the 5 cards in your hand. 
    The functions return (
        - [cards in set], 
        - [remainings cards]
        
    )
    """
    @staticmethod
    def flush(cards):
        
        t = cards[0]['type']
        if all([card['type'] == t for card in cards]):
            return cards, []
        else:
            return [], cards
    
    @staticmethod
    def straight(cards):
        
        # 10 J Q K A
        if cards[0]['value'] == 10 and cards[4]['value'] == Card.A:
            for i in range(0, 3):
                if cards[i]['value'] + 1 != cards[i+1]['value']:
                    return [], cards
            return cards, []
        # 2 3 4 5 A
        if cards[0]['value'] == 2 and cards[4]['value'] == Card.A:
            for i in range(0, 3):
                if cards[i]['value'] + 1 != cards[i+1]['value']:
                    return [], cards
            return cards, []
        
        else:
            for i in range(4):
                if cards[i]['value'] + 1 != cards[i+1]['value']:
                    return [], cards
            return cards, []
    
    @staticmethod
    def onepair(cards):
        
        counter = {}
        double_values = set()
        for card in cards:
            counter[card['value']] = counter.get(card['value'], 0) + 1
        
        for value, occurrences in counter.items():
            if occurrences == 2:
                double_values.add(value)
        
        if len(double_values) == 0:
            return [], cards
        
        double_values = list(double_values)
        if Card.A in double_values:
            highest_pair_value = Card.A
        else:
            highest_pair_value = max(double_values)
        
        cards_of_double = list(filter(lambda card: card['value'] == highest_pair_value, cards))
        return cards_of_double, Card.remaining(cards, cards_of_double)

    @staticmethod
    def twopairs(cards):
        
        counter = {}
        double_values = set()
        for card in cards:
            counter[card['value']] = counter.get(card['value'], 0) + 1
        
        for value, occurrences in counter.items():
            if occurrences == 2:
                double_values.add(value)
        
        if len(double_values) < 2:
            return [], cards

        double_values = list(double_values)
        
        cards_of_first_pair = list(filter(lambda card: card['value'] in double_values and card['value'] == double_values[0], cards))
        cards_of_second_pair = list(filter(lambda card: card['value'] in double_values and card['value'] == double_values[1], cards))

        cards_of_two_pairs = Card.sort(cards_of_first_pair + cards_of_second_pair)
        
        return cards_of_two_pairs, Card.remaining(cards, cards_of_two_pairs)

    @staticmethod
    def triple(cards):
        
        counter = {}
        for card in cards:
            counter[card['value']] = counter.get(card['value'], 0) + 1
        
        for value, occurrences in counter.items():
            if occurrences == 3:
                cards_of_triple = list(filter(lambda card: card['value'] == value, cards))
                return cards_of_triple, Card.remaining(cards, cards_of_triple)
            
        return [], cards
    
    @staticmethod
    def quadruple(cards):
        
        counter = {}
        for card in cards:
            counter[card['value']] = counter.get(card['value'], 0) + 1
        
        for value, occurrences in counter.items():
            if occurrences == 4:
                cards_of_quadruple = list(filter(lambda card: card['value'] == value, cards))
                return cards_of_quadruple, Card.remaining(cards, cards_of_quadruple)
            
        return [], cards
    
    @staticmethod
    def fullhouse(cards):
        if Poker.triple(cards)[0] and Poker.twopairs(cards)[0]:
            return cards, []
        else:
            return [], cards
    
    @staticmethod
    def highest(cards):
        return [Card.highest(cards)], Card.remaining(cards, [Card.highest(cards)])

    @staticmethod
    def check(cards):
        """
        Using above functions to check the cards, returns (code, [highest cards]) with code is the id of the highest set.
        code:
        1: highest card
        2: one pair
        3: two pairs
        4: three of a kind
        5: straight
        6: flush
        7: fullhouse
        8: four of a kind
        """
        checkers = [
            Poker.highest, 
            Poker.onepair, 
            Poker.twopairs, 
            Poker.triple, 
            Poker.straight, 
            Poker.flush, 
            Poker.quadruple]
        
        
    
    @staticmethod
    def compare(hand1, hand2):
        pass
    
        
        
        
        
    

class Game:
    def __init__(self) -> None:
        pass
    
