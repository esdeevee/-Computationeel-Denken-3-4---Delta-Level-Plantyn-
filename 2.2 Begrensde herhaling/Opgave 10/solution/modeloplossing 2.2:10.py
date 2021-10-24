# bij het begin van programma is het aantal drievouden gelijk aan nul
aantal_drievouden = 0

# herhaal 10 keer
for i in range(10):
    # lees een natuurlijk getal in
    getal = int(input('Geef een natuurlijk getal: '))
    if i == 0:
        # bij de eerste herhaling van de lus is het ingelezen getal zowel het grootste als het kleinste getal
        grootste = getal
        kleinste = getal
    else:
        # bij alle volgende iteraties moet je het ingelezen getal vergelijken met de bestaande waardes voor het grootste en het kleinste getal
        grootste = max(grootste, getal)
        kleinste = min(kleinste, getal)
    # controleer of het ingelezen getal deelbaar is door 3
    if getal % 3 == 0:
        # zo ja, verhoog de waarde van aantal_drievouden met 1
        aantal_drievouden = aantal_drievouden + 1
        
# toon de gewenste uitvoer
print('grootste:', grootste)
print('kleinste:', kleinste)
print('aantal drievouden:', aantal_drievouden)
