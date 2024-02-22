import poker
from cards import *
class Game:
    def __init__(self) -> None:
        self.players = []
        self.players.append("P1")
        self.players.append("P2")
        
    def simulte(self):
        i = 1
        while(True):
            # if i % 100000 == 0:
            print(f'\r{i}', end='')
            deck = poker.Deck()
            cards1 = Card.sort(deck.draw(5))
            cards2 = Card.sort(deck.draw(5))
            
            result = poker.Poker.compare(cards1, cards2)
            
            if result[1][0][0] == 8 or result[1][1][0] == 8:
                print(result)
                break
            i += 1
        
        """
        Haven't implement checking method for the in1 and in2 combination set yet!!!
        poker.py -> Poker -> compare()
        
        Code won't work if one of the two pairs is equal, but the other is difference!
        eg. 2 6 6 7 7 vs 4 5 5 7 7
        in_cards: [6 6 7 7] vs [5 5 7 7]
        -> result in equal -> check remaining -> hand2 has 4 wins, but in reality hand1 should have won (pair of 6 > pair of 4)
        
        Haven't implement for:
        - 2 pairs
        - fullhouse
        - straight
        
        """

"""
def simulte(self):
    i = 1
    while(True):
        # if i % 100000 == 0:
        print(f'\r{i}', end='')
        deck = poker.Deck()
        cards1 = Card.sort(deck.draw(5))
        cards2 = Card.sort(deck.draw(5))
        
        result = poker.Poker.compare(cards1, cards2)
        print(result[1][0][0])
        
        if result[1][0][0] == 10 or result[1][1][0] == 10:
            print(result)
            break
        i += 1
        
something strange happening here, 
if both 
    print(f'\r{i}', end='') 
    print(result[1][0][0])
are not commented, the script runs super fast, but if comment one or both, it will slows down???? 
That's super strange, it should runs very fast when I do not print anything!!

-> Turns out to be print(result[1][0][0]) prints an addition number, so I see the speed faster than 10 times
"""