# lees het aantal termen van de som in
n = int(input('Geef het aantal termen: '))

# initialiseer een numerieke variabele som
som = 0

# herhaal n keer:
for i in range(n):
    # de termen van de som zijn afwisselend positief en negatief
    # de eerste, derde, vijfde, ... termen zijn positief
    # voor Python zijn dit de nulde, tweede, vierde, ... termen
    # de teller van de breuken is dus 1 voor even waarden van i en -1 voor oneven waarden van i
    # je kunt de teller dus als volgt vinden:
    teller = (-1)**i
    # de noemer is gelijk aan het i-de oneven getal
    noemer = 2*i + 1
    # elke term is een breuk, gelijk aan teller gedeeld door noemer
    breuk = teller / noemer
    # verhoog de waarde van som met de waarde van de variabele breuk (die in de helft van de gevallen negatief is)
    som = som + breuk
    
# vermenigvuldig de bekomen waarde van som met 4 en print het resultaat
print(4*som)
