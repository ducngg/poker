import poker
from cards import *
class Game:
    """
    Implementing...
    """
    def __init__(self) -> None:
        self.players = []
        self.players.append("P1")
        self.players.append("P2")
        
    def simulate(self):
        i = 1
        
        TARGET_CODE = 9
        combinations = [
            "", # index 0 is not used
            "high card",
            "one pair",
            "two pair",
            "three of a kind",
            "straight",
            "flush",
            "fullhouse",
            "four of a kind",
            "straight flush",
            "royal flush"
        ]
        
        print(f'Finding {combinations[TARGET_CODE]}...')
        
        while(True):
            print(f'\r{i}', end='')
            deck = poker.Deck()
            cards1 = Card.sort(deck.draw(5))
            cards2 = Card.sort(deck.draw(5))
            
            result = poker.Poker.compare(cards1, cards2)
            
            if result[1][0][0] == TARGET_CODE or result[1][1][0] == TARGET_CODE:
                print(result)
                break
            i += 1
        