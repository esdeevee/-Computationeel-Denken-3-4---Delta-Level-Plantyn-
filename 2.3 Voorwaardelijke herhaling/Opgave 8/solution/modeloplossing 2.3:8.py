# importeer de vierkantswortelfunctie
from math import sqrt

# lees de x- en y-coordinaten van het eerste punt in
x0 = int(input('Geef de x-coordinaat: '))
y0 = int(input('Geef de y-coordinaat: '))

# op het einde heb je x0 en y0 nog nodig om de veelhoek te sluiten
# in de while-lus gebruik je de variabelen x1, y1, x2, y2
# voor het eerste punt is x1 = x0 en y1 = y0
x1 = x0
y1 = y0
# definieer de variabele omtrek
omtrek = 0

# herhaal
while True:
    # lees de x-coordinaat in, of STOP
    x2 = input('Geef de x-coordinaat of typ STOP: ')
    if x2 == 'STOP':
        # als er STOP werd getypt, wordt de while-lus afgebroken
        break
    else:
        # er werd een x-coordinaat ingevoerd. Zet deze om naar een integer en lees de y-coordinaat in
        x2 = int(x2)
        y2 = int(input('Geef de y-coordinaat: '))
        # verhoog de waarde van omtrek met de lengte van het lijnstuk tussen (x1,y1) en (x2,y2)
        omtrek = omtrek + sqrt((x2-x1)**2+(y2-y1)**2)
    # het laatst ingevoerde punt (x2,y2) heb je in een volgende stap nodig als (x1,y1) 
    x1 = x2
    y1 = y2

# de gebruiker heeft STOP getypt
# je moet de veelhoek nog sluiten
# verhoog de omtrek een laatste keer met de afstand tussen het laatst ingevoerde punt (x1,y1) en het startpunt (x0,y0)
omtrek = omtrek + sqrt((x1-x0)**2+(y1-y0)**2)
# print de berekende omtrek
print(omtrek)
