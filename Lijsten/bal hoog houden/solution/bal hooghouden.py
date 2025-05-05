from random import randint
from math import floor

def niveau(aantal_toetsen):
    return 1 + (aantal_toetsen - 1) // 10

def score(aantal_toetsen):
    resultaat = 0
    for toets in range(aantal_toetsen + 1):
        punt = niveau(toets)
        resultaat += punt
    return resultaat

def klasresultaat(lijst):
    scorelijst = []
    for kandidaat in lijst:
        scorelijst.append(score(kandidaat))
    # print(scorelijst)
    som = 0
    for resultaat in scorelijst:
        som += resultaat
    gemiddelde = floor(som / len(lijst))
    return gemiddelde
