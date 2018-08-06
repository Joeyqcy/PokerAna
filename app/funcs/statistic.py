from app.hand import Hand
from app.model import ALLCARDS
from app.game import select_best_hand, winner
from app.dealer import Dealer
from random import sample, shuffle
from copy import copy


def _statistic_5cards(hand_count):
    # 随机发五张牌，统计n手牌的牌型分布
    result = {}
    for i in range(hand_count):
        cards = Dealer.deal_5cards(1)[0]
        # pile = copy(ALLCARDS)
        # shuffle(pile)
        # cards = sample(pile, 5)
        hand = Hand.show_hand(cards)
        result.setdefault(hand, 0)
        result[hand] += 1
    result = sorted(list(result.items()), key=lambda x: x[1], reverse=True)
    for i, item in enumerate(result):
        item = list(item)
        item.append(round(item[1] / hand_count, 10))
        result[i] = tuple(item)
    return result


def _statistic_7cards(hand_count):
    # 随机发7张牌，统计n手牌的牌型分布
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
    for i, item in enumerate(result):
        item = list(item)
        item.append(round(item[1] / hand_count, 10))
        result[i] = tuple(item)
    return result


def _statistic_games(players=2, games=10000):
    # 统计若干玩家若干对局之后，获胜者的牌型分布
    result = {}
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
    for i, item in enumerate(result):
        item = list(item)
        item.append(round(item[1] / games, 10))
        result[i] = tuple(item)
    return result


def _statistic_preflop(c1, c2, c3, c4, games):
    # 以统计方式计算翻前胜率
    result = {}
    player_cards = [[c1, c2], [c3, c4]]
    count = [0, 0, 0]
    pile = copy(ALLCARDS)
    for player in player_cards:
        for card in player:
            pile.remove(card)
    shuffle(pile)
    for i in range(games):
        public = sample(pile, 5)
        winner_id = winner(player_cards, public)
        if len(winner_id) == 1:
            count[winner_id[0]] += 1
        else:
            count[2] += 1
    winner_rate = [round(cnt * 100 / games, 1) for cnt in count]
    result['winner_rate'] = winner_rate
    result['player_cards'] = player_cards
    return result
