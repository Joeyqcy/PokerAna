from app.hand import Hand
from itertools import combinations
import numpy as np


def winner(player_cards, public_cards):
    hands = []
    for player_card in player_cards:
        hands.append(select_best_hand(player_card, public_cards))
    winner_id = check_winner(hands)
    return winner_id


def check_winner(hands):
    """hands = [[cards], [cards], [cards], ]"""
    hand_scores = [Hand.hand_score(hand) for hand in hands]
    max_score = np.max(hand_scores)
    max_id = []
    for id, score in enumerate(hand_scores):
        if score == max_score:
            max_id.append(id)
    return max_id


def select_best_hand(player_card, public_cards):
    """player_cards [card1, card2]
       public_cards [card1, card2, card3, card4, card5]
    """
    player_card = list(player_card)
    public_cards = list(public_cards)
    all_cards = player_card + public_cards
    hands = list(combinations(all_cards, 5))
    max_id = check_winner(hands)
    return list(hands[max_id[0]])



