import game
from cards import Card

N_PLAYERS = 4

d = game.Deck()
hands =[Card.sort(d.draw(2)) for _ in range(N_PLAYERS)]


print(f'Players\' cards: {[game.Card.cs2ss(hand) for hand in hands]}')
print('\n')

shown = d.draw(3)
print(f'\tCommunity cards{game.Card.cs2ss(shown)}')
ps = game.poker.Poker.probabilities(hands, shown, d.deck)
print(f'Players\' winning probs: {ps}')

print('\n')

shown += d.draw(1)
print(f'\tCommunity cards{game.Card.cs2ss(shown)}')
ps = game.poker.Poker.probabilities(hands, shown, d.deck)
print(f'Players\' winning probs: {ps}')

print('\n')

shown += d.draw(1)
print(f'\tCommunity cards{game.Card.cs2ss(shown)}')
ps = game.poker.Poker.probabilities(hands, shown, d.deck)
print(f'Players\' winning probs: {ps}')
