# dit programma vraagt de massa m (in kg) en de lengte l (in m) van een persoon en berekent de BMI
m = float(input('Geef de massa (in kg): '))
l = float(input('Geef de lengte (in m): '))
BMI = m/l**2
print(round(BMI, 1))
