"""
# lees het bedrag in dat je wilt afhalen
bedrag = int(input('Geef een bedrag in euro: '))
# bereken de kosten
kosten_A = 2 + 0.02 * bedrag
kosten_B = 0.05 * bedrag
kosten_C = 5
# controleer welke van de kosten de laagste is
if kosten_A == min(kosten_A, kosten_B, kosten_C):
    print('A')
    print(bedrag + kosten_A)
elif kosten_B == min(kosten_A, kosten_B, kosten_C):
    print('B')
    print(bedrag + kosten_B)
else:
    print('C')
    print(bedrag + kosten_C)
"""

from random import randint

def bankkaart(bedrag):
    # bereken de kosten
    kosten_A = 2 + 0.02 * bedrag
    kosten_B = 0.05 * bedrag
    kosten_C = 5
    # controleer welke van de kosten de laagste is
    if kosten_A == min(kosten_A, kosten_B, kosten_C):
        uitvoer = ['A', bedrag + kosten_A]
    elif kosten_B == min(kosten_A, kosten_B, kosten_C):
        uitvoer = ['B', bedrag + kosten_B]
    else:
        uitvoer = ['C', bedrag + kosten_C]
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
  bedrag = 5 * randint(1,50)
  with open('0.in', 'a') as f:
    f.write(str(bedrag))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(bankkaart(bedrag)[0]))
    g.write("\n")
    g.write(str(bankkaart(bedrag)[1]))
    g.write("\n")

