# dit programma vraagt de lengte van de rechthoekszijden van een rechthoekige driehoek en berekent de lengte van de schuine zijde c
from math import sqrt
a = float(input('Geef de lengte (in cm) van de eerste rechthoekszijde: '))
b = float(input('Geef de lengte (in cm) van de tweede rechthoekszijde: '))
c = sqrt(a**2 + b**2)
print(round(c, 1))
