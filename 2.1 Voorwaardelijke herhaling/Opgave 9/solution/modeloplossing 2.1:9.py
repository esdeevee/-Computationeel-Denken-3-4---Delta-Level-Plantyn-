# lees twee natuurlijke getallen in
getal_1 = int(input('Geef een eerste natuurlijk getal: '))
getal_2 = int(input('Geef een tweede natuurlijk getal: '))

# je weet niet welke van beide het grootste is
# gebruik min() en max() om dit uit te zoeken
kleinste = min(getal_1, getal_2)
grootste = max(getal_1, getal_2)

# controleer of het kleinste getal een deler is van het grootste getal
if grootste % kleinste == 0:
    print(grootste, 'is een veelvoud van', kleinste)
else:
    print(grootste, 'is geen veelvoud van', kleinste)
