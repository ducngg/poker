from cards import *

md = Deck()

hand = md.deck[:40]

hand = Card.sort(hand)

print(list(map(Card.c2s, hand)))

