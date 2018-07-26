# 花色注释
# H 红桃(Heart)
# S 黑桃(Spade)
# D 方块(Diamond)
# C 梅花(Club)
COLOR = ['H', 'S', 'D', 'C']
VALUE = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
VALUEMAP = {'2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
            }
HANDVALUE = {'RoyalFlush': 10,
             'StraightFlush': 9,
             'Bomb': 8,
             'FullHouse': 7,
             'Flush': 6,
             'Straight': 5,
             'Trip': 4,
             'TwoPairs': 3,
             'Pair': 2,
             'HighCard': 1
             }
ALLCARDS = [color+value for color in COLOR for value in VALUE]

class Card:
    def __init__(self,card):
        self.card = card
        self.color = card[0]
        self.value = VALUEMAP[card[1]]

# print(len(ALLCARDS))
# print(ALLCARDS)
# card = Card(ALLCARDS[10])
# print(card.card, card.color, card.value)
