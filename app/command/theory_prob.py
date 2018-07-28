from app.hand import Hand
from app.model import ALLCARDS
from itertools import combinations
import numpy as np
np.set_printoptions(suppress=True)

def theory_prob_5cards():
    # 发五张牌， 各个牌型的概率
    result = {}
    combines = list(combinations(ALLCARDS, 5))
    for cards in combines:
        hand = Hand.show_hand(cards)
        result.setdefault(hand, 0)
        result[hand] += 1
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print('\n')
    print('Theoretical probability of hand type with 5 cards')
    print('=' * 50)
    print('Hand type' + ' ' * 20 + 'Probability')
    print('=' * 50)
    for hand, count in result:
        print(hand + ' ' * (25 - len(hand)) + '{:.10f}'.format(count / len(combines)))
    print('=' * 50)


