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
        





# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
file = open("1.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()
file = open("1.out", "w")
file.truncate()
file.close()

for i in range(1, 101): 
    with open('0.in', 'a') as file:
        file.write('>>> niveau(' + str(i) + ')')
        file.write('\n')
        file.write(str(niveau(i)))
        file.write('\n')
    with open('1.in', 'a') as file:
        file.write('>>> score(' + str(i) + ')')
        file.write('\n')
        file.write(str(score(i)))
        file.write('\n')

# wis alle gegevens in in.csv
file = open("2.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("2.out", "w")
file.truncate()
file.close()


for i in range(1, 5):
    for j in range(25):
        lijst = []
        aantal_leerlingen = randint(1, 5*i)
        for k in range(aantal_leerlingen):
            lijst.append(randint(1, 100))
        with open('2.in', 'a') as file:
            file.write('>>> klasresultaat(' + str(lijst) + ')')
            file.write('\n')
            file.write(str(klasresultaat(lijst)))
            file.write('\n')
        
