"""
# dit programma vraagt een tijdstip en een aantal uur
# het berekent de hoek tussen de grote en de kleine wijzer van een klok nadat deze op tijdstip beginuur aantal_uur wordt doorgedraaid
beginuur = int(input('Geef het tijdstip waarop de klok wordt verder gedraaid: '))
aantal_uur = int(input('Geef het aantal uur waarop de klok wordt verder gedraaid: '))
einduur = (beginuur + aantal_uur) % 12
hoek = min(einduur * 30, 360 - einduur * 30)
print(hoek)
"""

from random import randint

def klok(begin,aantal):
    einduur = (beginuur + aantal_uur) % 12
    hoek = min(einduur * 30, 360 - einduur * 30)
    return(hoek)

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()

for i in range(20):
  beginuur = randint(0,11)
  aantal_uur = randint(0,10)
  with open('0.in', 'a') as f:
    f.write(str(beginuur))
    f.write("\n")
    f.write(str(aantal_uur))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(klok(beginuur,aantal_uur)))
    g.write("\n")

for i in range(20):
  beginuur = randint(0,11)
  aantal_uur = randint(10,100)
  with open('0.in', 'a') as f:
    f.write(str(beginuur))
    f.write("\n")
    f.write(str(aantal_uur))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(klok(beginuur,aantal_uur)))
    g.write("\n")

for i in range(20):
  beginuur = randint(0,11)
  aantal_uur = randint(100,1000)
  with open('0.in', 'a') as f:
    f.write(str(beginuur))
    f.write("\n")
    f.write(str(aantal_uur))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(klok(beginuur,aantal_uur)))
    g.write("\n")

for i in range(20):
  beginuur = randint(0,11)
  aantal_uur = randint(1000,10000)
  with open('0.in', 'a') as f:
    f.write(str(beginuur))
    f.write("\n")
    f.write(str(aantal_uur))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(klok(beginuur,aantal_uur)))
    g.write("\n")

for i in range(20):
  beginuur = randint(0,11)
  aantal_uur = randint(10000,100000)
  with open('0.in', 'a') as f:
    f.write(str(beginuur))
    f.write("\n")
    f.write(str(aantal_uur))
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(klok(beginuur,aantal_uur)))
    g.write("\n")
