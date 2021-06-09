### Opgave

In deze opgave is het de bedoeling een programma te schrijven dat het opgooien van twee eerlijke dobbelstenen simuleert. De gebruiker mag kiezen hoe vaak er "gegooid" wordt. Kijk bij Opgave 11 (p. 26) hoe je een (pseudo-)willekeurig getal kan genereren om het gooien van één enkele dobbelsteen te simuleren.

Schrijf een functie `dobbelstenen` die aan de gebruiker het aantal simulaties vraagt. Je code simuleert dan net zo vaak de som van twee dobbelstenen. De uitvoer bestaat uit een overzicht van de relatieve frequenties van de verschillende mogelijkheden.

In een naïeve implementatie van deze opdracht dreig je een monsterachtig grote lijst te genereren, waardoor het geheugen van de computer langzaam maar zeker vol loopt. Hoe zou je dit kunnen vermijden? Je zou deze efficiëntere oplossing in principe moeten kunnen implementeren, maar het hoeft niet.

### Voorbeeld

**Invoer:**

    Geef het aantal simulaties: 100000

**Uitvoer:**

    Relatieve frequentie van 2: 0.02788
    Relatieve frequentie van 3: 0.05633
    Relatieve frequentie van 4: 0.08379
    Relatieve frequentie van 5: 0.11048
    Relatieve frequentie van 6: 0.14095
    Relatieve frequentie van 7: 0.16683
    Relatieve frequentie van 8: 0.13818
    Relatieve frequentie van 9: 0.11038
    Relatieve frequentie van 10: 0.08262
    Relatieve frequentie van 11: 0.05519
    Relatieve frequentie van 12: 0.02737
