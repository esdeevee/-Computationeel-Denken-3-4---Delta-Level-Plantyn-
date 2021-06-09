getal = input("Geef een natuurlijk getal: ")

while len(getal) > 1:
  som = 0
  for i in range(len(getal)):
    som = som + int(getal[i])
  getal = str(som)
  #print(getal)
print(som)




from random import randint
import csv

def reduceer(getal):
  while len(getal) > 1:
    som = 0
    for i in range(len(getal)):
      som = som + int(getal[i])
    getal = str(som)
    #print(getal)
  return(som)

# wis alle gegevens in in.csv
f = open("in.csv", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("out.csv", "w")
f.truncate()
f.close()

for i in range(100):
  n = str(randint(10000, 10000000))
  #print(n, reduceer(n))
  with open('in.csv', 'a') as f:
    f.write(n)
    f.write("\n")
  with open('out.csv', 'a') as f:
    f.write(str(reduceer(n)))
    f.write("\n")
