import game
from test import *
from cards import Card, Deck
from poker import Poker

def print_possibilities(players, hands, shown, deck):
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
    
    possibilities = Poker.possibilities(hands, shown, deck)
    n_possibilities = len(possibilities)
    cases = [possibility[0] for possibility in possibilities]
    best_five_of_players_based_on_cases = [possibility[1] for possibility in possibilities]

    # [([best_hand], index)]
    winners = [Poker.best_hand(best_five_of_players) for best_five_of_players in best_five_of_players_based_on_cases]
    win_indexes = [w[1] for w in winners]

    for i in range(n_possibilities):
        print(f"Case {Card.cs2ss(cases[i])}: Player {players[win_indexes[i]]} won! ({Card.cs2ss(winners[i][0])}) - {combinations[Poker.check(winners[i][0])[2]]}")

    counts = [win_indexes.count(i) for i, _ in enumerate(hands)]

    for i in range(len(hands)):
        print(f"{players[i]} winning chance: {counts[i]}/{n_possibilities}")


N = 4

deck = Deck()

players = [f"P{i}" for i in range(N)]
hands = [deck.draw(2) for _ in players]

print(players)
print(hands)
print([Card.cs2ss(hand) for hand in hands])

print('\n--------------------------------------------------------\n')

shown = deck.draw(3)
print(Card.cs2ss(shown))
print_possibilities(players, hands, shown, deck.deck)
print(Poker.probabilities(hands, shown, deck.deck))

print('\n--------------------------------------------------------\n')

shown += deck.draw(1)
print(Card.cs2ss(shown))
print_possibilities(players, hands, shown, deck.deck)
print(Poker.probabilities(hands, shown, deck.deck))

print('\n--------------------------------------------------------\n')

shown += deck.draw(1)
print(Card.cs2ss(shown))
print_possibilities(players, hands, shown, deck.deck)
print(Poker.probabilities(hands, shown, deck.deck))
