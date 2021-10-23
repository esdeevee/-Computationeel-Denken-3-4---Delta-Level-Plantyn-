# dit programma vraagt de lengte van de grote en kleine diagonaal (in cm) in een ruit en berekent de oppervlakte (in cm2) en de omtrek (in cm)
# stel de grote en de kleine diagonaal voor door de variabelen GD en KD
# A is de oppervlakte en P is de omtrek
from math import sqrt
GD = float(input('Geef de lengte van de grote diagonaal (in cm): '))
KD = float(input('Geef de lengte van de kleine diagonaal (in cm): '))
A = GD * KD/2
P = 4 * sqrt((GD/2)**2 + (KD/2)**2)
print(round(A,2))
print(round(P, 1))
