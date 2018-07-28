from app.hand import Hand
from app.model import ALLCARDS
from random import randint, shuffle
from itertools import combinations


def statistic_5cards(hand_count=100000):
    # 随机发五张牌，统计n手牌的牌型分布
    hand_count = int(hand_count)
    result = {}
    combines = list(combinations(ALLCARDS, 5))
    shuffle(combines)
    for i in range(hand_count):
        cards = combines[randint(0, len(combines)-1)]
        hand = Hand.show_hand(cards)
        result.setdefault(hand, 0)
        result[hand] += 1
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print('\n')
    print(' ' * 20 +'%d hands statistic:' % hand_count)
    print('=' * 80)
    print('hand type' + ' ' * 15 + 'counts' + ' ' * 20 + 'rate')
    print('=' * 80)
    for hand, count in result:
        print(hand + ' ' * (24 - len(hand)) + str(count) + ' ' * (25 - len(str(count))) + '{:.10f}'.format(count / hand_count))
    print('=' * 80)