from random import randint
from math import sqrt
import csv

def Newton(x, vorige):
  volgende = (vorige + x/vorige)/2
  return volgende

def hoofdprogramma(getal, decimalen):
  benadering = getal / 2
  aantal_iteraties = 1
  while True:
    volgende = Newton(getal, benadering)
    verschil = abs(volgende - benadering)
    benadering = volgende
    aantal_iteraties = aantal_iteraties + 1
    #print(benadering, verschil)
    if verschil < 10**(-decimalen):
      break
  #print("De wortel van", getal, "is bij benadering gelijk aan", benadering)
  #print("Aantal iteraties:", aantal_iteraties)
  #print("De wortel van", getal, "is exact gelijk aan", sqrt(getal))

  with open('in.csv', 'a') as f:
    f.write(str(getal))
    f.write("\n")
    f.write(str(decimalen))
    f.write("\n")
  with open('out.csv', 'a') as f:
    f.write("De wortel van " + str(getal) + " is bij benadering gelijk aan " + str(benadering))
    f.write("\n")
    f.write("Aantal iteraties: " + str(aantal_iteraties))
    f.write("\n")
    f.write("Afwijking ten opzichte van de exacte waarde: " + str(abs(sqrt(getal) - benadering)))
    f.write("\n")

# wis alle gegevens in in.csv
f = open("in.csv", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("out.csv", "w")
f.truncate()
f.close()

for i in range(20):
  for j in range(5):
    #print(i)
    getal = randint(10**i, 10**(i+1))
    decimalen = randint(1, 8) 
    hoofdprogramma(getal, decimalen)
