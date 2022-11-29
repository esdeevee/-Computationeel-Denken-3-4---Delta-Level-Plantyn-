"""
# dit programma berekent de datum (einddatum) en het tijdstip (einduur) waarop een timer met duur timer afloopt die start op 31 december om beginuur
begindatum = int(input('Geef de datum (in december) waarop de timer wordt gestart: '))
beginuur = int(input('Geef het tijdstip waarop de timer wordt gestart: '))
timer = int(input('Geef de duur (in uur) van de timer: '))
einddatum = (begindatum + (beginuur + timer) // 24)
einduur = (beginuur + timer) % 24
print(einddatum, einduur)
"""

from random import randint

def timer(begindatum, beginuur, tijd):
    einddatum = (begindatum + (beginuur + tijd) // 24)
    einduur = (beginuur + tijd) % 24
    uitvoer = [einddatum, einduur]
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
  begindatum = randint(1,30)
  beginuur = randint(0,23)
  tijd = randint(1,24*(31-begindatum))
  with open('0.in', 'a') as f:
    f.write(str(begindatum))
    f.write("\n")
    f.write(str(beginuur))
    f.write("\n")
    f.write(str(tijd))
    f.write("\n")
  with open('0.out', 'a') as g:
    uitvoer = str(timer(begindatum, beginuur, tijd)[0]) + " " + str(timer(begindatum, beginuur, tijd)[1])
    g.write(uitvoer)
    g.write("\n")
