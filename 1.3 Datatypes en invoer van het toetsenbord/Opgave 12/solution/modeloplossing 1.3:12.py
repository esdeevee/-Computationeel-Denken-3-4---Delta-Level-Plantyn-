# dit programma berekent de lengte l (in cm) van een persoon als de massa m (in kg) en de BMI (in kg/m2) gegeven zijn
from math import sqrt
m = float(input('Geef een massa (in kg): '))
BMI = float(input('Geef een BMI (in kg/m2): '))
l = 100 * sqrt(m / BMI)
print(round(l, 1))
