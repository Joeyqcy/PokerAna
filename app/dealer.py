from app.model import ALLCARDS
from random import shuffle
from copy import copy


class Dealer:
    def __init__(self, players=1):
        players = int(players)
        """1<=players<=9"""
        if players > 9:
            raise ValueError('players should  be less than 10.')
        self.players = players
        self.pile = copy(ALLCARDS)
        self.player_cards = []
        self.public_cards = []
        self.flop = []
        self.turn = ''
        self.river = ''
        shuffle(self.pile)
        for i in range(self.players):
            self.player_cards.append([])

    def deal_hand(self):
        for player in self.player_cards:
            player.append(self.pile.pop(0))
        for player in self.player_cards:
            player.append(self.pile.pop(0))
        return self.player_cards

    def deal_public(self):
        self.pile.append(self.pile.pop(0))
        for i in range(3):
            self.public_cards.append(self.pile.pop(0))
        self.pile.append(self.pile.pop(0))
        self.public_cards.append(self.pile.pop(0))
        self.pile.append(self.pile.pop(0))
        self.public_cards.append(self.pile.pop(0))
        self.flop = self.public_cards[0:3]
        self.turn = self.public_cards[3]
        self.river = self.public_cards[4]
        return self.public_cards

    @staticmethod
    def deal_5cards(players=1):
        pile = copy(ALLCARDS)
        hands = []
        for i in range(players):
            hands.append([])
        shuffle(pile)
        for i in range(5):
            for player in hands:
                player.append(pile.pop(0))
        return hands






