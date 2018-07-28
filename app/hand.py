from app.model import HANDVALUE, Card, VALUEMAP
from collections import Counter
from operator import itemgetter

class Hand:
    # 对于五张牌，判断成牌类型
    @staticmethod
    def show_hand(cards):
        if Hand.royal_flush(cards):
            return 'RoyalFlush'
        elif Hand.straight_flush(cards):
            return 'StraightFlush'
        elif Hand.bomb(cards):
            return 'Bomb'
        elif Hand.full_house(cards):
            return 'FullHouse'
        elif Hand.flush(cards):
            return 'Flush'
        elif Hand.straight(cards):
            return 'Straight'
        elif Hand.trip(cards):
            return 'Trip'
        elif Hand.two_pairs(cards):
            return 'TwoPairs'
        elif Hand.pair(cards):
            return 'Pair'
        else:
            return 'HighCard'

    @staticmethod
    def show_hand_value(cards):
        hand = Hand.show_hand(cards)
        return HANDVALUE[hand]

    @staticmethod
    def royal_flush(cards):
        values = Hand.get_values(cards)
        colors = Hand.get_colors(cards)
        if len(set(colors)) == 1 and values[4] == 10:
            return True
        else:
            return False

    @staticmethod
    def straight_flush(cards):
        values = Hand.get_values(cards)
        colors = Hand.get_colors(cards)
        if len(set(colors)) == 1 and values[0] - values[4] == 4:
            return True
        else:
            return False

    @staticmethod
    def bomb(cards):
        values = Hand.get_values(cards)
        if len(set(values)) == 2:
            for value in set(values):
                if values.count(value) in [1, 4]:
                    return True
                else:
                    return False

    @staticmethod
    def full_house(cards):
        values = Hand.get_values(cards)
        if len(set(values)) == 2:
            for value in set(values):
                if values.count(value) in [2, 3]:
                    return True
                else:
                    return False

    @staticmethod
    def flush(cards):
        values = Hand.get_values(cards)
        colors = Hand.get_colors(cards)
        if len(set(colors)) == 1 and values[0] - values[4] != 4:
            return True
        else:
            return False

    @staticmethod
    def straight(cards):
        values = Hand.get_values(cards)
        colors = Hand.get_colors(cards)
        if len(set(values)) == 5 and values[0] - values[4] == 4 and len(set(colors)) != 1:
            return True
        else:
            return False

    @staticmethod
    def trip(cards):
        values = Hand.get_values(cards)
        if len(set(values)) == 3:
            for value in set(values):
                if values.count(value) == 3:
                    return True
                elif values.count(value) == 2:
                    return False
                else:
                    continue

    @staticmethod
    def two_pairs(cards):
        values = Hand.get_values(cards)
        if len(set(values)) == 3:
            for value in set(values):
                if values.count(value) == 2:
                    return True
                elif values.count(value) == 3:
                    return False
                else:
                    continue

    @staticmethod
    def pair(cards):
        values = Hand.get_values(cards)
        if len(set(values)) == 4:
            return True
        else:
            return False

    @staticmethod
    def get_colors(cards):
        colors = [card[0] for card in cards]
        return colors

    @staticmethod
    def get_values(cards):
        """按大小排序,特例A2345"""
        values = [VALUEMAP[card[1]] for card in cards]
        values.sort(reverse=True)
        if values == [14, 5, 4, 3, 2]:
            values = [5, 4, 3, 2, 1]
        return values

    @staticmethod
    def sort_by_type(cards):
        """按同牌大小排序"""
        values = [VALUEMAP[card[1]] for card in cards]
        counter = Counter(values)
        counter = sorted(counter.items(), key=itemgetter(1, 0), reverse=True)
        values = []
        for item in counter:
            for count in range(item[1]):
                values.append(item[0])
        return values

    @staticmethod
    def hand_score(cards):
        """生成手牌分数 格式为十一位， RoyalStraigth为十二位"""
        values = Hand.sort_by_type(cards)
        hand_score = str(Hand.show_hand_value(cards))
        for value in values:
            if value >= 10:
                hand_score += str(value)
            else:
                hand_score += ('0' + str(value))
        return int(hand_score)

