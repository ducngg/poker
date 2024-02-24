import game
from test import *
from cards import Card, Deck
from poker import Poker

# hand1 = straight.random_straight()
# hand2 = straight.random_straight()

# hand1 = [{'value': 1, 'type': 4}, {'value': 2, 'type': 3}, {'value': 3, 'type': 2}, {'value': 4, 'type': 1}, {'value': 5, 'type': 2}]
# hand2 = [{'value': 2, 'type': 4}, {'value': 3, 'type': 3}, {'value': 4, 'type': 2}, {'value': 5, 'type': 1}, {'value': 6, 'type': 2}]

# A 2 3 4 5 is currently > 2 3 4 5 6

# print(Poker.compare(hand1, hand2))

# experiment_game = game.Game()
# experiment_game.simulate()


# Players' cards: [['8♥️', '10♥️'], ['7♥️', '9♦️'], ['4♥️', 'K♦️'], ['4♣️', '4♦️']]


#         Community cards['Q♠️', 'Q♥️', '7♦️']
# Players' winning probs: [0.2804878048780488, 0.5365853658536586, 0.13902439024390245, 0.04390243902439024]


#         Community cards['Q♠️', 'Q♥️', '7♦️', 'J♣️']
# Players' winning probs: [0.225, 0.6, 0.15, 0.025]


#         Community cards['Q♠️', 'Q♥️', '7♦️', 'J♣️', 'A♣️']
# Players' winning probs: [0.0, 1.0, 0.0, 0.0]

deck = Deck()
deck.deck = Card.FULL

hands = [['8♥️', '10♥️'], ['7♥️', '9♦️'], ['4♥️', 'K♦️'], ['4♣️', '4♦️']]
hands = [Card.ss2cs(cards) for cards in hands]

for hand in hands:
    deck.deck = Card.remaining(deck.deck, hand)

shown = Card.ss2cs(['Q♠️', 'Q♥️', '7♦️'])
deck.deck = Card.remaining(deck.deck, shown)

print(len(deck.deck))
print(Poker.probabilities(hands, shown, deck.deck))

shown = Card.ss2cs(['Q♠️', 'Q♥️', '7♦️', 'J♣️'])
deck.deck = Card.remaining(deck.deck, shown)

print(len(deck.deck))
print(Poker.probabilities(hands, shown, deck.deck))

for card in deck.deck:
    
    shown_after_choose = shown + [card]
    deck_after_choose = Card.remaining(deck.deck, shown_after_choose)
    print(Card.c2s(card), Poker.probabilities(hands, shown_after_choose, deck_after_choose))
    print([Card.cs2ss(Poker.best_five(hand+shown_after_choose)) for hand in hands])



# shown = Card.ss2cs(['9♦️', '3♣️', 'J♣️', '9♠️', 'A♣️'])
# deck.deck = Card.remaining(deck.deck, shown)

print(len(deck.deck))
print(Poker.probabilities(hands, shown, deck.deck))

print([Card.cs2ss(Poker.best_five(hand+shown)) for hand in hands])
