# in de while-lus verwijs je naar de variabele aantal
# bij de eerste herhaling van de lus moet deze dus gekend zijn door Python
# bij het begin van het programma is het aantal ingelezen getallen gelijk aan 0
aantal = 0

# gebruik de (while True: ... break)-constructie
while True:
    # lees de invoer
    invoer = input('Geef een natuurlijk getal of typ STOP: ')
    # als de invoer STOP is, wordt de while-lus afgebroken
    if invoer == 'STOP':
        break
    else:
    	# als de invoer een getal is, wordt het verwerkt
        getal = int(invoer)
        if aantal == 0:
            # bij de eerste herhaling van de lus is het ingelezen getal zowel het grootste als het kleinste
            grootste = getal
            kleinste = getal
        else:
            # bij elke volgende herhaling van de lus vergelijk je de ingelezen waarde met het vorige grootste en kleinste getal
            grootste = max(grootste, getal)
            kleinste = min(kleinste, getal)
        # bij elke herhaling van de lus moet het aantal ingelezen getallen verhogen met 1
        aantal = aantal + 1

# toon de gewenste uitvoer
print(grootste, kleinste, aantal)
