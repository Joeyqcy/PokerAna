from app.model import HANDVALUE


# 函数输入为牌类对象
class Hand:
    # 输入的牌均为牌对象，最后在外层代码进行转换
    @staticmethod
    def show_hand(cards):
        if Hand.royal_flush(cards):
            return 'RoyalFlush'
        if Hand.straight_flush(cards):
            return 'StraightFlush'
        if Hand.bomb(cards):
            return 'Bomb'
        if Hand.full_house(cards):
            return 'FullHouse'
        if Hand.flush(cards):
            return 'Flush'
        if Hand.straight(cards):
            return 'Straight'
        if Hand.trip(cards):
            return 'Trip'
        if Hand.two_pairs(cards):
            return 'TwoPairs'
        if Hand.pair(cards):
            return 'pair'
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
        if len(set(colors)) == 1 and (values[0] - values[4] == 4 or values == [14, 5, 4, 3, 2]):
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
        if len(set(colors)) == 1 and values[0] - values[4] != 4 and values != [14, 5, 4, 3, 2]:
            return True
        else:
            return False

    @staticmethod
    def straight(cards):
        values = Hand.get_values(cards)
        colors = Hand.get_colors(cards)
        if len(set(values)) == 5 and (values[0] - values[4] == 4 or values == [14, 5, 4, 3, 2]) and len(set(colors)) != 1:
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
        colors = [card.color for card in cards]
        return colors

    @staticmethod
    def get_values(cards):
        values = [card.value for card in cards]
        values.sort(reverse=True)
        return values

# scards = ['SA','S2','S3','S4','D5']
# cards = [Card(scard) for scard in scards]
# print(Hand.show_hand(cards))
# print(Hand.straight(cards))

