from app.model import ALLCARDS, Card, db
from random import sample, shuffle
from app.command.theory_prob import preflop
from copy import copy
from time import sleep


def init_db():
    cards = Card.query.all()
    if not cards:
        cards = [Card(scard) for scard in ALLCARDS]
        for card in cards:
            db.session.add(card)
        db.session.commit()
    else:
        print('Warning: table `card` is not empty, please check it.')


def upgrade_preflop(count):
    count = int(count)
    pile = copy(ALLCARDS)
    shuffle(pile)
    for i in range(count):
        cards = sample(pile, 4)
        try:
            preflop(cards[0], cards[1], cards[2], cards[3])
        except Exception as e:
            print(e)
        sleep(60)