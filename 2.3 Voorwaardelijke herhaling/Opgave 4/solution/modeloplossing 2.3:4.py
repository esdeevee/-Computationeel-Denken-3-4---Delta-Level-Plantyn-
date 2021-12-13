# lees een getal in
getal = int(input('Geef een natuurlijk getal: '))

# bij het begin van het programma gaan we ervan uit dat het ingelezen getal geen priemfactoren heeft
aantal_priemfactoren = 0

# onderzoek of 2 een priemfactor is
while getal % 2 == 0:
    print(2)
    getal = getal / 2
    aantal_priemfactoren = aantal_priemfactoren + 1

# de variabele getal is nu niet meer deelbaar door 2: het is dus zeker oneven
# er zijn dus zeker geen even priemfactoren meer
# onderzoek of er nog oneven priemfactoren zijn
# getal is van het type float
# om getal te kunnen gebruiken in een range(), moet je er eerst een integer van maken
for i in range(3, int(getal), 2):
    while getal % i == 0:
        # i is een priemfactor van getal
        print(i)
        getal = getal / i
        aantal_priemfactoren = aantal_priemfactoren + 1
    # als getal gelijk is aan 1, heb je alle priemfactoren gevonden
    # je hoeft niet meer te zoeken bij grotere waarden van i 
    if getal == 1:
        break

# als er geen enkele priemfactor gevonden is, moet je melden dat de variabele getal een priemgetal is
if aantal_priemfactoren == 0:
    print(getal, 'is een priemgetal.')
