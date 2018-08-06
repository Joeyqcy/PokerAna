from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy import create_engine


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


db_engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)


def get_conn(db='PokerAna'):
    conn = db_engine.connect()
    conn.execute('USE ' + db)
    return conn


db = SQLAlchemy()

class Card(db.Model):
    """52张牌"""

    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    card = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(10), nullable=False)
    value = db.Column(db.Integer, nullable=False)

    def __init__(self, scard):
        self.card = scard
        self.color = scard[0]
        self.value = VALUEMAP[scard[1]]


class PreFlop(db.Model):
    """翻前胜率"""

    __tablename__ = 'pre_flop'
    id = db.Column(db.Integer, primary_key=True)
    P1C1 = db.Column(db.String(10), nullable=False)
    P1C2 = db.Column(db.String(10), nullable=False)
    P2C1 = db.Column(db.String(10), nullable=False)
    P2C2 = db.Column(db.String(10), nullable=False)
    P1_winner_rate = db.Column(db.Float, nullable=False)
    P2_winner_rate = db.Column(db.Float, nullable=False)
    Split_rate = db.Column(db.Float, nullable=False)
