from app.hand import Hand
from app.model import ALLCARDS
from random import randint
from itertools import combinations

combines = combinations(ALLCARDS, 5)
for i, scards in enumerate(combines):
    pass
print(i)