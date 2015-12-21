__author__ = 'zadoev@gmail.com'
"""
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, Ten, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives.
But if two ranks tie, for example, both players have a pair of queens, then
highest cards in each hand are compared; if the highest cards tie then the
next highest cards are compared, and so on.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename.
Each line in this file contains 2 hands (left and right). Cards and hands
are separated by space. E.g.

6D 7H AH 7S QC 6H 2D TD JD AS
JH 5D 7H TC JS JD JC TS 5S 7S
2H 8C AD TH 6H QD KD 9H 6S 6C
JS JH 4H 2C 9H QH KC 9D 4D 3S
TC 7H KH 4H JC 7D 9S 3H QS 7S
OUTPUT SAMPLE:

Print out the name of the winning hand or "none" in case the hands are equal.
E.g.

left
none
right
left
right
"""

import sys
from collections import Counter

cards_map = {
    str(label): value + 2 for value, label in enumerate(range(2, 10) + list('TJQKA'))
}

HIGHT_CARD = 1
ONE_PAIR = 2
TWO_PAIRS = 3
THREE_OF_KIND = 4
STRAIGH = 5
FLUSH = 6
FULL_HOUSE = 7
FOUR_OF_KIND = 8
STRAIGH_FLUSH = 9
ROYAL_FLUSH = 10

COMBINATION_LENGTH_HELPER = {3: TWO_PAIRS, 4: ONE_PAIR, 5: HIGHT_CARD}


def hand_builder(input):
    """
    Pretty dirty, need to refactoring

    >>> hand_builder('2D 3H 4D 5H 6D')  # straight
    [5, 6]

    >>> hand_builder('2D 3D 4D 5D 7D')  # flush
    [6, 7]

    >>> hand_builder('AD JD QD KD TD')  #  high straight flush eg royal flush
    [9, 14]

    >>> hand_builder('2D 3D 4D 5D 6D')  #  high straight flush eg royal flush
    [9, 6]

    >>> hand_builder('TD TH TS TC AD')  #  4 of kinds
    [8, 14]

    >>> hand_builder('TD TH TS 2C 2D')  #  flush
    [7, 10, 2]

    >>> hand_builder('TD TH TS 9C 2D')  #  three of kind
    [4, 10, 9, 2]

    >>> hand_builder('TD TH 3S 2C 2D')  #  2 pairs
    [3, 10, 2, 3]

    >>> hand_builder('TD TH KS KC 2D')  #  2 pairs
    [3, 13, 10, 2]

    >>> hand_builder('TD KH 3S 2C 2D')  #  1 pair
    [2, 2, 13, 10, 3]

    >>> hand_builder('TD KH 3S 2C 5D')  #  high card
    [1, 13, 10, 5, 3, 2]

    :param input: left string input
    :type input: basestring
    :return: hand as list
    :rtype: list
    """
    suites = set()
    cards = []

    for c in input.split():
        s, c = list(c)
        suites.add(c)
        cards.append(cards_map[s])
    cards = sorted(cards)
    is_flush = len(suites) == 1
    is_straight = map(lambda x: x - cards[0], cards) == [0, 1, 2, 3, 4]

    if is_straight:
        if is_flush:
            return [STRAIGH_FLUSH, cards[4]]
        return [STRAIGH, cards[4]]

    if is_flush:
        return [FLUSH, cards[4]]

    card_combinations = Counter(cards)

    num = len(card_combinations.keys())

    r = {v: k for k, v in card_combinations.items()}
    if num == 2:  # full house or 4 of kind
        if 4 in r:
            return [FOUR_OF_KIND, r[1]]

        return [FULL_HOUSE, r[3], r[2]]
    elif num == 3:
        if 3 in r:
            combo = [THREE_OF_KIND]
        else:
            combo = [TWO_PAIRS]
    else:
        combo = [COMBINATION_LENGTH_HELPER[num]]

    kickers = sorted(
        card_combinations.items(), key=lambda x: (x[1],x[0]), reverse=True
    )

    kickers = [i for i, v in kickers]

    return combo + kickers

if __name__ == '__main__':
    with open(sys.argv[1]) as test_cases:
        for line in test_cases:
            hand_a = hand_builder(line[:14])
            hand_b = hand_builder(line[15:29])
            if hand_a > hand_b:
                print 'left'
            elif hand_a < hand_b:
                print 'right'
            else:
                print 'none'

