import math

n = eval(input("Geef het aantal termen: "))

volgende = 0
vorige = 0
for i in range(n):
    teller = (-1)**(i)
    noemer = 2*i + 1
    breuk = teller /noemer
    vorige = volgende
    volgende = volgende + breuk

print("Heel naïeve benadering van pi:", 4*volgende)
print("Afwijking t.o.v. pi:", abs(math.pi - 4*volgende))
print("Iets minder maar nog steeds erg naïeve benadering van pi:", 2*(volgende + vorige))
print("Afwijking t.o.v. pi:", abs(math.pi - 2*(volgende + vorige)))


from random import randint
import math

def pi(n): 
  volgende = 0
  vorige = 0
  for i in range(n):
    teller = (-1)**(i)
    noemer = 2*i + 1
    breuk = teller /noemer
    vorige = volgende
    volgende = volgende + breuk
  return([4*volgende, 2*(volgende + vorige)])
"""
print("Heel naïeve benadering van pi:", pi(100000)[0])
print("Afwijking t.o.v. pi:", abs(math.pi - pi(100000)[0]))
print("Iets minder maar nog steeds erg naïeve benadering van pi:", pi(100000)[1])
print("Afwijking t.o.v. pi:", abs(math.pi - pi(100000)[1]))
"""

for i in range(10):
  aantal = randint(1000, 1000000)
  print(aantal)
  print("Heel naïeve benadering van pi:", pi(aantal)[0])
  print("Afwijking t.o.v. pi:", abs(math.pi - pi(aantal)[0]))
  print("Iets minder maar nog steeds erg naïeve benadering van pi:", pi(aantal)[1])
  print("Afwijking t.o.v. pi:", abs(math.pi - pi(aantal)[1]))
