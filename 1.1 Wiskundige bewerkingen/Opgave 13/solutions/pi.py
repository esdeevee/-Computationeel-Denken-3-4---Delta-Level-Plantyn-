from random import randint

def pi(n):
  som = 0
  for i in range(n):
    teller = (-1)**(i)
    noemer = 2*i + 1
    breuk = teller /noemer
    som = som + breuk
  return(4*som)

for i in range(10):
  aantal = randint(1000, 1000000)
  print(aantal,pi(aantal))
