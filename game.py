from cards import *

class Poker:
    """
    This class consist of functions that check the 5 cards in your hand. 
    """
    @staticmethod
    def flush(cards):
        
        t = cards[0]['type']
        return all([card['type'] == t for card in cards]), [Card.highest(cards)]
    
    @staticmethod
    def straight(cards):
        
        # A 10 J Q K
        if cards[0]['value'] == Card.A and cards[1]['value'] == 10:
            for i in range(1, 4):
                if cards[i]['value'] + 1 != cards[i+1]['value']:
                    return False, None
            return True, [cards[0]]
        
        for i in range(4):
            if cards[i]['value'] + 1 != cards[i+1]['value']:
                return False, None
        return True, [cards[-1]]
    
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
            return False, None
        
        cards_of_double = list(filter(lambda card: card['value'] in double_values, cards))
        return True, [Card.highest(cards_of_double)]

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
            return False, None
        
        cards_of_first_pair = list(filter(lambda card: card['value'] in double_values and card['value'] == double_values[0], cards))
        cards_of_second_pair = list(filter(lambda card: card['value'] in double_values and card['value'] == double_values[1], cards))

        return True, [Card.sort([Card.highest(cards_of_first_pair), Card.highest(cards_of_second_pair)])]


    @staticmethod
    def check(cards):
        pass
    
    
        
        
        
        
    

class Game:
    def __init__(self) -> None:
        pass
    
