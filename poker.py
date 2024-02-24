from cards import *

class Poker:
    """
    This class consists of checker functions that evaluate the 5 cards in a hand.

    The checker functions return a tuple containing two lists:
    - The first list contains cards in the combination.
    - The second list contains remaining cards.

    Essential functions:
    - check(cards): Evaluate the combination of cards.
    - compare(hand1, hand2): Compare two hands.
    - best_hand(hands): Determine the best hand among multiple hands.
    - probabilities(hands, shown, deck): Calculate winning probabilities of the hands based on the hands and shown cards.
    """
    
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    HOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10
        
    @staticmethod
    def highest(cards: list):
        return [Card.highest(cards)], Card.remaining(cards, [Card.highest(cards)])
    
    @staticmethod
    def onepair(cards: list):
        
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
    def twopairs(cards: list):
        
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
    def triple(cards: list):
        
        counter = {}
        for card in cards:
            counter[card['value']] = counter.get(card['value'], 0) + 1
        
        for value, occurrences in counter.items():
            if occurrences == 3:
                cards_of_triple = list(filter(lambda card: card['value'] == value, cards))
                return cards_of_triple, Card.remaining(cards, cards_of_triple)
            
        return [], cards
    
    @staticmethod
    def straight(cards: list):
        
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
    def flush(cards: list):
        
        t = cards[0]['type']
        if all([card['type'] == t for card in cards]):
            return cards, []
        else:
            return [], cards
        
    @staticmethod
    def fullhouse(cards: list):
        if Poker.triple(cards)[0] and Poker.onepair(cards)[0]:
            return cards, []
        else:
            return [], cards
    
    @staticmethod
    def quadruple(cards: list):
        
        counter = {}
        for card in cards:
            counter[card['value']] = counter.get(card['value'], 0) + 1
        
        for value, occurrences in counter.items():
            if occurrences == 4:
                cards_of_quadruple = list(filter(lambda card: card['value'] == value, cards))
                return cards_of_quadruple, Card.remaining(cards, cards_of_quadruple)
            
        return [], cards

    @staticmethod
    def straightflush(cards: list):
        if Poker.straight(cards)[0] and Poker.flush(cards)[0]:
            return cards, []
        else:
            return [], cards
    
    @staticmethod
    def royalflush(cards: list):
        if Poker.straight(cards)[0] and Poker.flush(cards)[0] and cards[0]['value'] == 10:
            return cards, []
        else:
            return [], cards

    @staticmethod
    def check(cards: list):
        """
        Evaluate the combination of cards and return the result.

        `return in_list, out_list, code` with:
            - in_list (list): Cards in the combination.
            - out_list (list): Remaining cards.
            - code (int): ID representing the highest combination found.
        
        Combination Codes:
            1: Highest card
            2: One pair
            3: Two pairs
            4: Three of a kind
            5: Straight
            6: Flush
            7: Full house
            8: Four of a kind
            9: Straight flush
            10: Royal flush
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
    
    def compare_straight(in1: list, in2: list):
        # If the inputs are not straight -> return 0
        if not Poker.straight(in1)[0] or not Poker.straight(in2)[0]:
            return 0
        
        # If 2 3 4 5 A -> A 2 3 4 5
        if Card.contains(in1, Card.A) and Card.contains(in1, 2):
            in1 = [in1[-1]] + in1[:-1]
        if Card.contains(in2, Card.A) and Card.contains(in2, 2):
            in2 = [in2[-1]] + in2[:-1]
        
        return Card.card_by_card_compare(in1, in2, sort=False)
    
    def compare_two_pairs(in1: list, in2: list):
        # If the inputs are not two pairs -> return 0
        if not Poker.twopairs(in1)[0] or not Poker.twopairs(in2)[0]:
            return 0
        
        value_low_pair_in1 = in1[0]['value']
        value_high_pair_in1 = in1[2]['value']
        value_low_pair_in2 = in2[0]['value']
        value_high_pair_in2 = in2[2]['value']
        
        if Card.compare_value(value_high_pair_in1, value_high_pair_in2) == 1:
            return 1
        elif Card.compare_value(value_high_pair_in1, value_high_pair_in2) == -1:
            return -1
        
        if Card.compare_value(value_low_pair_in1, value_low_pair_in2) == 1:
            return 1
        elif Card.compare_value(value_low_pair_in1, value_low_pair_in2) == -1:
            return -1
        
        return Card.card_by_card_compare(in1, in2, sort=False)
    
    def compare_fullhouse(in1: list, in2: list):
        # If the inputs are not fullhouse -> return 0
        if not Poker.fullhouse(in1)[0] or not Poker.fullhouse(in2)[0]:
            return 0
        
        triple_in1 = Poker.triple(in1)[0]
        pair_in1 = Poker.onepair(in1)[0]
        triple_in2 = Poker.triple(in2)[0]
        pair_in2 = Poker.onepair(in2)[0]
        
        value_triple_in1 = triple_in1[0]['value']
        value_pair_in1 = pair_in1[0]['value']
        value_triple_in2 = triple_in2[0]['value']
        value_pair_in2 = pair_in2[0]['value']
                
        if Card.compare_value(value_triple_in1, value_triple_in2) == 1:
            return 1
        elif Card.compare_value(value_triple_in1, value_triple_in2) == -1:
            return -1
        
        if Card.compare_value(value_pair_in1, value_pair_in2) == 1:
            return 1
        elif Card.compare_value(value_pair_in1, value_pair_in2) == -1:
            return -1
        
        return Card.card_by_card_compare(pair_in1+triple_in1, pair_in2+triple_in2, sort=False)
        
    @staticmethod
    def compare(hand1: list, hand2: list):
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

        # Level 2 winning: combination type is the same, cards in combination type are better
        ## Check for specific code first
        if code1 in [Poker.STRAIGHT, Poker.STRAIGHT_FLUSH, Poker.ROYAL_FLUSH]:
            if Poker.compare_straight(in1, in2) == 1:
                return 2, ([code1, in1, out1], [code2, in2, out2])
            elif Poker.compare_straight(in1, in2) == -1:
                return -2, ([code1, in1, out1], [code2, in2, out2])
        elif code1 in [Poker.TWO_PAIRS]:
            if Poker.compare_two_pairs(in1, in2) == 1:
                return 2, ([code1, in1, out1], [code2, in2, out2])
            elif Poker.compare_two_pairs(in1, in2) == -1:
                return -2, ([code1, in1, out1], [code2, in2, out2])
        elif code1 in [Poker.FULL_HOUSE]:
            if Poker.compare_fullhouse(in1, in2) == 1:
                return 2, ([code1, in1, out1], [code2, in2, out2])
            elif Poker.compare_fullhouse(in1, in2) == -1:
                return -2, ([code1, in1, out1], [code2, in2, out2])
        ## Other codes: use card by card comparison
        else:
            if Card.card_by_card_compare(in1, in2) == 1:
                return 2, ([code1, in1, out1], [code2, in2, out2])
            elif Card.card_by_card_compare(in1, in2) == -1:
                return -2, ([code1, in1, out1], [code2, in2, out2])
            
        # Level 1 winning: combination type is the same, highest card in combination type is the same, remaining cards is better
        if Card.card_by_card_compare(out1, out2) == 1:
            return 1, ([code1, in1, out1], [code2, in2, out2])
        elif Card.card_by_card_compare(out1, out2) == -1:
            return -1, ([code1, in1, out1], [code2, in2, out2])
        else:
            return 0, ([code1, in1, out1], [code2, in2, out2])
    
    @staticmethod
    def best_hand(hands: list):
        """
        Return the best hand and the index of it in `hands`.
        """
        # Filtering out to just the potential hands to reduce calculation  

        check_codes = [Poker.check(hand)[2] for hand in hands]
        max_code = max(check_codes)
        
        highest_hands = []
        for comb, code in zip(hands, check_codes):
            if code == max_code:
                highest_hands.append(comb)
                
        best = highest_hands[0]
        for hand in highest_hands:
            if Poker.compare(hand, best)[0] > 0:
                best = hand
                
        return best, hands.index(best)
        
    @staticmethod
    def next_possible_cards_combination(deck, number_of_cards=1):
        return list(combinations(deck, number_of_cards))
        
    @staticmethod
    def probabilities(hands, shown, deck):
        """
        Calculate probability of winning for each hand in `hands`. 
        """
        if len(shown) == 3:
            next_combinations = Poker.next_possible_cards_combination(deck, 2)
        elif len(shown) == 4:
            next_combinations = Poker.next_possible_cards_combination(deck, 1)
        elif len(shown) == 5:
            next_combinations = [[]]
        else:
            return []
        
        # [[seven1, seven2, ...], [seven1, seven2, ...], ...]
        sevens_of_hands = [
            [hand + shown + list(next_combination) for next_combination in next_combinations] 
            for hand in hands
        ]
                
        # [[five1, five2, ...], [five1, five2, ...], ...]
        bests_of_hands = [
            [Poker.best_five(seven) for seven in sevens] 
            for sevens in sevens_of_hands
        ]
        
        # [[five1, five1, ...], [five2, five2, ...], ...]
        hands_possibilities = [[best[case] for best in bests_of_hands] for case in range(len(next_combinations))]
        
        # [[best_hand_of_fives1, index],[best_hand_of_fives2, index], ...]
        results = [Poker.best_hand(hands_possibility) for hands_possibility in hands_possibilities]
        win_indexes = [result[1] for result in results]

        counts = [win_indexes.count(i) for i, _ in enumerate(hands)]
        
        probs = [count/len(next_combinations) for count in counts]
        
        return probs
            
    @staticmethod
    def best_five(seven):
        combs = list(combinations(seven, 5))
        combs = [Card.sort(comb) for comb in combs]        
    
        return Poker.best_hand(combs)[0]
        
        
        