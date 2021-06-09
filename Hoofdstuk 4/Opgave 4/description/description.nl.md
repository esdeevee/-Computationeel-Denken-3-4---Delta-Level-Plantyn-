### Opgave

Newton bedacht de volgende, zeer efficiënte methode om de vierkantswortel
van een willekeurig positief reëel getal te berekenen:
* Neem als eerste benadering voor de vierkantswortel van x de helft van x.
* Vervang deze benadering een nieuwe benadering, die gelijk is aan het gemiddelde
van de vorige benadering en het getal bekomen door x te delen door de vorige
benadering.
* Herhaal de vorige stap tot de absolute waarde van het verschil tussen twee opeenvolgende benaderingen kleiner is dan een bepaalde waarde.

Schrijf een programma dat aan de gebruiker eerst een natuurlijk getal vraagt. Vervolgens vraagt je programma het gewenste aantal decimalen van het verschil tussen twee opeenvolgende benaderingen. (Het verschil moet dus kleiner zijn dan 10**(-aantal_decimalen).)

Voer het algoritme van Newton uit. Als uitvoer geeft je programma de benaderde waarde, het aantal iteraties (het aantal benaderingen dat gemaakt werd), en de afwijking ten opzichte van de exacte vierkantswortel (berekend met sqrt). Maak hierbij minstens één keer gebruik van een functie.

### Voorbeeld

**Invoer:**

    Geef een natuurlijk getal: 9
    Geef een aantal decimalen: 4

**Uitvoer:**

    De wortel van 9 is bij benadering gelijk aan 3.0000000000393214
    Aantal iteraties: 5
    Afwijking ten opzichte van de exacte waarde: 3.9321434996963944e-11

**Invoer:**

    Geef een natuurlijk getal: 560
    Geef een aantal decimalen: 7

**Uitvoer:**

    De wortel van 560 is bij benadering gelijk aan 23.664319132398465
    Aantal iteraties: 9
    Afwijking ten opzichte van de exacte waarde: 0.0
