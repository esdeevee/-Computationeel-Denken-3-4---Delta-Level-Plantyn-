from random import randint
from math import ceil

def bakken(aantal_bakken):
    #aantal_bakken = int(input('Geef het aantal bestelde bakken water: '))
    aantal_palletten = ceil(aantal_bakken / 48)
    aantal_vrachtwagens = aantal_palletten // 20
    aantal_palletten_niet_in_vrachtwagen = aantal_palletten % 20
    aantal_bestelwagens = ceil(aantal_palletten_niet_in_vrachtwagen / 8)
    aantal_palletten_bestelwagen = aantal_palletten_niet_in_vrachtwagen % 8
    aantal_bakken_op_halfvolle_pallet = aantal_bakken % 48

    return([aantal_palletten, aantal_vrachtwagens, aantal_palletten_niet_in_vrachtwagen, aantal_bestelwagens, aantal_palletten_bestelwagen, aantal_bakken_op_halfvolle_pallet])

#getal = int(input('Geef een ISBN-nummer van 12 cijfers: '))
#print(ISBN(getal))

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()



for i in range(25):
  aantal = randint(1,100)
  with open('0.in', 'a') as f:
    f.write(str(aantal))
    f.write("\n")
  with open('0.out', 'a') as g:
    uitvoer = str(bakken(aantal)[0])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[1])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[2])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[3])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[4])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[5])
    g.write(uitvoer)
    g.write("\n")
    #break

for i in range(25):
  aantal = randint(100,1000)
  with open('0.in', 'a') as f:
    f.write(str(aantal))
    f.write("\n")
  with open('0.out', 'a') as g:
    uitvoer = str(bakken(aantal)[0])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[1])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[2])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[3])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[4])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[5])
    g.write(uitvoer)
    g.write("\n")
    #break

for i in range(25):
  aantal = randint(1000,10000)
  with open('0.in', 'a') as f:
    f.write(str(aantal))
    f.write("\n")
  with open('0.out', 'a') as g:
    uitvoer = str(bakken(aantal)[0])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[1])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[2])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[3])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[4])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[5])
    g.write(uitvoer)
    g.write("\n")
    #break

for i in range(25):
  aantal = randint(10000,100000)
  with open('0.in', 'a') as f:
    f.write(str(aantal))
    f.write("\n")
  with open('0.out', 'a') as g:
    uitvoer = str(bakken(aantal)[0])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[1])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[2])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[3])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[4])
    g.write(uitvoer)
    g.write("\n")
    uitvoer = str(bakken(aantal)[5])
    g.write(uitvoer)
    g.write("\n")
    #break

