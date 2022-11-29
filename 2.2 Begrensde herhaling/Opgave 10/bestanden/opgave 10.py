"""
getal_1 = int(input('Geef een eerste geheel getal: '))
getal_2 = int(input('Geef een tweede geheel getal: '))
if getal_1 == getal_2:
    print('De getallen zijn gelijk aan elkaar.')
elif getal_1 > getal_2:
    print('Het eerste getal is groter dan het tweede getal.')
else:
    print('Het eerste getal is kleiner dan het tweede getal.')
"""

from random import randint

def treinticket(afstand):
    # bereken de prijzen voor beide tickets
    standaardprijs = 1.5 + 0.15 * afstand
    jongerenprijs = 7
    # controleer of de standaardprijs de laagste prijs is
    if standaardprijs == min(standaardprijs, jongerenprijs):
        uitvoer = ['standaard ticket', standaardprijs]
    else:
        uitvoer = ['jongerenticket', jongerenprijs]
    return(uitvoer)

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()

for i in range(100):
  afstand = randint(5,200)
  with open('0.in', 'a') as f:
    f.write(str(afstand))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(treinticket(afstand)[0]))
    g.write("\n")
    g.write(str(treinticket(afstand)[1]))
    g.write("\n")

