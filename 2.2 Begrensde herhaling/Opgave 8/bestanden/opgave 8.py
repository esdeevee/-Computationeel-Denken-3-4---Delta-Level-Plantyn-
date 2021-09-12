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

def graad(gemiddelde):
    if gemiddelde < 68:
        graad = 'V'
    if gemiddelde >= 68:
        graad = 'O'
    if gemiddelde >= 77:
        graad = 'GO'
    if gemiddelde >= 85:
        graad = 'GGO'
    if gemiddelde >= 90:
        graad = 'F'
    return(graad)

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()

for i in range(100):
  gemiddelde = randint(50,100)
  with open('0.in', 'a') as f:
    f.write(str(gemiddelde))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(graad(gemiddelde))
    g.write("\n")

