from app.hand import Hand
from app.model import ALLCARDS, get_conn, PreFlop,db
from app.game import select_best_hand, winner
from itertools import combinations
from copy import copy


def _prob_5cards():
    # 发五张牌， 各个牌型的概率
    result = {}
    combines = list(combinations(ALLCARDS, 5))
    for cards in combines:
        hand = Hand.show_hand(cards)
        result.setdefault(hand, 0)
        result[hand] += 1
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    for i, item in enumerate(result):
        item = list(item)
        item.append(round(item[1] / len(combines), 10))
        result[i] = tuple(item)
    return result


def _prob_7cards():
    # 发七张牌，各个牌型的概率
    result = {}
    combines = list(combinations(ALLCARDS, 7))
    for cards in combines:
        best_hand = select_best_hand(cards[:2], cards[2:])
        hand = Hand.show_hand(best_hand)
        result.setdefault(hand, 0)
        result[hand] += 1
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    for i, item in enumerate(result):
        item = list(item)
        item.append(round(item[1] / len(combines), 10))
        result[i] = tuple(item)
    return result


def _prob_preflop(c1, c2, c3, c4):
    # 两位玩家在翻前的各自胜率, *args在shell里好像不好给参数，先用命名参数
    result = {}
    winner_rate = []
    player_cards = [[c1, c2], [c3, c4]]
    conn = get_conn()
    sql = """select * from pre_flop where 
    P1C1 in ('%s', '%s') and P1C2 in ('%s', '%s') and 
    P2C1 in ('%s', '%s') and P2C1 in('%s', '%s') or 
    P1C1 in ('%s', '%s') and P1C2 in ('%s', '%s') and 
    P2C1 in ('%s', '%s') and P2C1 in('%s', '%s')""" % (c1, c2, c1, c2, c3, c4, c3, c4, c3, c4, c3, c4, c1, c2, c1, c2)
    old_preflop = conn.execute(sql).fetchone()
    conn.close()
    if old_preflop:
        if old_preflop['P1C1'] in [c1, c2]:
            winner_rate = [old_preflop['P1_winner_rate'], old_preflop['P2_winner_rate'], old_preflop['Split_rate']]
        elif old_preflop['P1C1'] in [c3, c4]:
            winner_rate = [old_preflop['P2_winner_rate'], old_preflop['P1_winner_rate'], old_preflop['Split_rate']]
    else:
        pile = copy(ALLCARDS)
        count = [0, 0, 0]
        for player in player_cards:
            for card in player:
                pile.remove(card)
        combines = list(combinations(pile, 5))
        for public_cards in combines:
            winner_id = winner(player_cards, public_cards)
            if len(winner_id) == 1:
                count[winner_id[0]] += 1
            else:
                count[2] += 1
        winner_rate = [round(cnt * 100 / len(combines), 1) for cnt in count]

        new_preflop = PreFlop(P1C1=c1, P1C2=c2, P2C1=c3, P2C2=c4,
                              P1_winner_rate=winner_rate[0], P2_winner_rate=winner_rate[1],
                              Split_rate=winner_rate[2])
        db.session.add(new_preflop)
        db.session.commit()
    result['winner_rate'] = winner_rate
    result['player_cards'] = player_cards
    return result
