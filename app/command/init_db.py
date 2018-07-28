from app.model import ALLCARDS, Card, db

def init_db():
    cards = Card.query.all()
    if not cards:
        cards = [Card(scard) for scard in ALLCARDS]
        for card in cards:
            db.session.add(card)
        db.session.commit()
    else:
        print('Warning: table `card` is not empty, please check it.')