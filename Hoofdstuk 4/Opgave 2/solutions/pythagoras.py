from math import sqrt

def pythagoras(a, b):
  c = sqrt(a**2 + b**2)
  return(c)

a = eval(input("Geef de lengte van de eerste rechthoekszijde: "))
b = eval(input("Geef de lengte van de tweede rechthoekszijde: "))
print("De schuine zijde heeft een lengte van", pythagoras(a,b))







from math import sqrt
from random import randint
import csv

def pythagoras(a, b):
  c = sqrt(a**2 + b**2)
  return(c)


for i in range(100):
  #print(i)
  a = randint(1, 100)
  b = randint(1, 200)
  uitvoer = "De schuine zijde heeft een lengte van " + str(pythagoras(a,b))
  with open('in.csv', 'a') as f:
    f.write(str(a))
    f.write("\n")
    f.write(str(b))
    f.write("\n")
  with open('out.csv', 'a') as f:
    f.write(uitvoer)
    f.write("\n")
