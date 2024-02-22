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
    def highest(cards):
        return [Card.highest(cards)], Card.remaining(cards, [Card.highest(cards)])
    
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
    def flush(cards):
        
        t = cards[0]['type']
        if all([card['type'] == t for card in cards]):
            return cards, []
        else:
            return [], cards
        
    @staticmethod
    def fullhouse(cards):
        if Poker.triple(cards)[0] and Poker.twopairs(cards)[0]:
            return cards, []
        else:
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
    def straightflush(cards):
        if Poker.straight(cards)[0] and Poker.flush(cards)[0]:
            return cards, []
        else:
            return [], cards
    
    @staticmethod
    def royalflush(cards):
        if Poker.straight(cards)[0] and Poker.flush(cards)[0] and cards[0]['value'] == 10:
            return cards, []
        else:
            return [], cards

    @staticmethod
    def check(cards):
        """
        Using above functions to check the cards, returns (code, [highest cards]) with code is the id of the highest combination.
        code:
        1: highest card
        2: one pair
        3: two pairs
        4: three of a kind
        5: straight
        6: flush
        7: fullhouse
        8: four of a kind
        9: straight flush
        10: royal flush
        """
        checkers = [
            Poker.highest, 
            Poker.onepair, 
            Poker.twopairs, 
            Poker.triple, 
            Poker.straight, 
            Poker.flush, 
            Poker.fullhouse, 
            Poker.quadruple,
            Poker.straightflush,
            Poker.royalflush
        ]
        
        cards = Card.sort(cards)
                
        for checker, code in zip(checkers, range(1, len(checkers)+1)):
            in_cards, out_cards = checker(cards)
            if in_cards:
                final_code = code
                final_in_cards = in_cards
                final_out_cards = out_cards
                
        return final_in_cards, final_out_cards, final_code
    
    @staticmethod
    def compare(hand1, hand2):
        """
        Compare two hands of poker.

        This function compares two hands, each consisting of 5 cards.

        In the context of poker, a "combination" refers to a specific hand combination. 
        There are various types of combinations (see `Poker.check()` for details).

        Returns:
        - Result = 3 if the combination type of `hand1` is better than `hand2`.
        - Result = 2 if both hands have the same combination type, but the cards in `hand1` are better.
        - Result = 1 if both hands have the same combination type and cards, but the remaining cards in `hand1` are better.
        - Result = 0 if both hands are identical.

        Returns a tuple containing the result and additional information about the hands:
        (`result`, ([code1, in1, out1], [code2, in2, out2]))
        - `result`: The result of the comparison (as described above).
        - `code1`, `in1`, `out1`: Combination type code, cards inside the combination, and remaining cards for `hand1`.
        - `code2`, `in2`, `out2`: Combination type code, cards inside the combination, and remaining cards for `hand2`.
        
        The combination type codes and their meanings can be found in the `Poker.check()` function.
        """

        in1, out1, code1 = Poker.check(hand1)
        in2, out2, code2 = Poker.check(hand2)
        
        # Level 3 winning: combination type is better
        if code1 > code2:
            return 3, ([code1, in1, out1], [code2, in2, out2])
        elif code1 < code2:
            return -3, ([code1, in1, out1], [code2, in2, out2])
        else:
            # Level 2 winning: combination type is the same, cards in combination type are better
            '''
            Currently compare card by card.
            Working on implementing comparing method for each combination.
            '''
            if Card.card_by_card_compare(in1, in2) == 1:
                return 1, ([code1, in1, out1], [code2, in2, out2])
            elif Card.card_by_card_compare(in1, in2) == -1:
                return -1, ([code1, in1, out1], [code2, in2, out2])
            else:
                # Level 1 winning: combination type is the same, highest card in combination type is the same, remaining cards is better
                if Card.card_by_card_compare(out1, out2) == 1:
                    return 1, ([code1, in1, out1], [code2, in2, out2])
                elif Card.card_by_card_compare(out1, out2) == -1:
                    return -1, ([code1, in1, out1], [code2, in2, out2])
                else:
                    return 0, ([code1, in1, out1], [code2, in2, out2])
    
    
