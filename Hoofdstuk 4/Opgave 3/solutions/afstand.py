from random import randint
from math import sqrt
import csv

def afstand(x1, y1, x2, y2):
  d = sqrt((x1-x2)**2 + (y1-y2)**2)
  return(d)

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()

for j in range(4):
  for i in range(25):
    x1 = randint(-10*10**j, 10*10**j)
    y1 = randint(-10*10**j, 10*10**j)
    x2 = randint(-10*10**j, 10*10**j)
    y2 = randint(-10*10**j, 10*10**j)
    uitvoer = str(afstand(x1, y1, x2, y2))
    with open("0.in", "a") as f:
      f.write(str(x1))
      f.write("\n")
      f.write(str(y1))
      f.write("\n")
      f.write(str(x2))
      f.write("\n")
      f.write(str(y2))
      f.write("\n")
    with open("0.out", "a") as f:
      f.write(uitvoer)
      f.write("\n")




  

  
