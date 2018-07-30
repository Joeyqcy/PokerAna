from app.hand import Hand
from app.model import ALLCARDS
from app.game import select_best_hand, winner
from app.dealer import Dealer
from random import sample, shuffle
from copy import copy


def statistic_5cards(hand_count):
    # 随机发五张牌，统计n手牌的牌型分布
    hand_count = int(hand_count)
    result = {}
    for i in range(hand_count):
        cards = Dealer.deal_5cards(1)[0]
        # pile = copy(ALLCARDS)
        # shuffle(pile)
        # cards = sample(pile, 5)
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


def statistic_7cards(hand_count):
    # 随机发7张牌，统计n手牌的牌型分布
    hand_count = int(hand_count)
    result = {}
    for i in range(hand_count):
        pile = copy(ALLCARDS)
        shuffle(pile)
        cards = sample(pile, 7)
        best_hand = select_best_hand(cards[:2], cards[2:])
        hand = Hand.show_hand(best_hand)
        result.setdefault(hand, 0)
        result[hand] += 1
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print('\n')
    print(' ' * 20 + '%d hands statistic:' % hand_count)
    print('=' * 80)
    print('hand type' + ' ' * 15 + 'counts' + ' ' * 20 + 'rate')
    print('=' * 80)
    for hand, count in result:
        print(hand + ' ' * (24 - len(hand)) + str(count) + ' ' * (25 - len(str(count))) + '{:.10f}'.format(count / hand_count))
    print('=' * 80)


def statistic_games(players=2, games=10000):
    # 统计若干玩家若干对局之后，获胜者的牌型分布
    result = {}
    players = int(players)
    games = int(games)
    for i in range(games):
        dealer = Dealer(players)
        player_cards = dealer.deal_hand()
        public_cards = dealer.deal_public()
        winner_id = winner(player_cards, public_cards)
        winner_hand = select_best_hand(player_cards[winner_id[0]], public_cards)
        hand = Hand.show_hand(winner_hand)
        result.setdefault(hand, 0)
        result[hand] += 1
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print('\n')
    print(' ' * 10 + '%d players %d games statistic:' % (players, games))
    print('=' * 80)
    print('winner hand' + ' ' * 15 + 'counts' + ' ' * 20 + 'rate')
    print('=' * 80)
    for hand, count in result:
        print(hand + ' ' * (24 - len(hand)) + str(count) + ' ' * (25 - len(str(count))) + '{:.10f}'.format(
            count / games))
    print('=' * 80)
