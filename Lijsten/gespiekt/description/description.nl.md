### Inleiding

Tijdens de examenperiode zitten de leerlingen van een klas, gesorteerd volgens klasnummer, op één lange lijn. Spieken van de leerling links of rechts van je is dus niet heel erg moeilijk. Je mag uitgaan van de naïeve veronderstelling dat spieken bij leerlingen die niet je buren zijn, onmogelijk is.

Om mogelijke fraude gemakkelijk te detecteren, wil de school de resultaten automatische analyseren. Wanneer een mogelijk geval van fraude automatisch gedetecteerd wordt, kan de leerkracht manueel nakijken of er al dan niet gespiekt werd.

De resultaten van alle leerlingen in een klas worden in een lijst voorgesteld. Deze resultaten zijn percentages,natuurlijke getallen tussen 0 en 100. We noemen een situatie `verdacht` wanneer een leerling een resultaat haalt dat hoogstens 5 punten afwijkt van een leerling die naast hem/haar zat. We noemen een situatie `erg verdacht` wanneer twee naast zittende leerlingen exact hetzelfde resultaat behaald hebben.

### Opgave

Schrijf een functie `gespiekt(lijst)` die alle verdachte en erg verdachte situaties toont. Als leerlingen met klasnummer `n` en `n+1` een verdachte situatie vormen, geeft je programma als uitvoer `n en n+1 zijn verdacht`. Als leerlingen met klasnummer `n` en `n+1` een erg verdachte situatie vormen, geeft je programma als uitvoer `n en n+1 zijn erg verdacht`. Als er geen verdachte situaties waren, geeft je programma als uitvoer `Er waren geen verdachte situaties.`.

### Voorbeeld 1

**Invoer:**

    > gespiekt([60, 70, 35])

**Uitvoer:**

    Er waren geen verdachte situaties.


### Voorbeeld 2

**Invoer:**

    > gespiekt([60, 70, 73, 79, 79, 82, 30, 28, 75, 75])

**Uitvoer:**

    2 en 3 zijn verdacht
    4 en 5 zijn erg verdacht
    5 en 6 zijn verdacht
    7 en 8 zijn verdacht
    9 en 10 zijn erg verdacht
