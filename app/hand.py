from app.model import Card, HANDVALUE


# 输入的牌面统一为字符串牌面，在函数内部转换为类对象
def show_hand(cards):
    cards = [Card(card) for card in cards]
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


def show_hand_value(cards):
    hand = show_hand(cards)
    return HANDVALUE[hand]


# 函数输入为牌类对象
class Hand:
    @staticmethod
    def royal_flush(cards):
        return True

    @staticmethod
    def straight_flush(cards):
        return True

    @staticmethod
    def bomb(cards):
        return True

    @staticmethod
    def full_house(cards):
        return True

    @staticmethod
    def flush(cards):
        return True

    @staticmethod
    def straight(cards):
        return True

    @staticmethod
    def trip(cards):
        return True

    @staticmethod
    def two_pairs(cards):
        return True

    @staticmethod
    def pair(cards):
        return True