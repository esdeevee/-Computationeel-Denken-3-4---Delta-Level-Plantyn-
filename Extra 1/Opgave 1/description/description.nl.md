### Opgave

Schrijf een programma dat een natuurlijk getal vraagt tussen 0 en 100. Dit getal stelt de resterende lading voor van een batterij (uitgedrukt in procent).

Je programma geeft dit percentage op een grafische manier weer. De uitvoer bestaat uit een recht haakje ([), gevolgd door 20 karakters. Een karakter is ofwel een verticale streep (|), ofwel een spatie. De uitvoer wordt beëindigd door een recht haakje (]), een spatie, en de resterende lading.

Je begrijpt dat een verticale streep dus overeenkomt met 5% lading. Meer specifiek:
* als de lading 0 is, toont je programma geen enkele verticale streep.
* als de lading in het interval [1, 5] ligt, toont je programma 1 verticale streep.
* als de lading in het interval [6, 10] ligt, toont je programma 2 verticale strepen.
* ...
* als de lading in het interval [96, 100] ligt, toont je programma 20 verticale strepen.


### Voorbeeld

**Invoer:**

    Geef het percentage van de batterij: 14

**Uitvoer:**

    [|||                 ] 14%

**Invoer:**

    Geef het percentage van de batterij: 79

**Uitvoer:**

    [||||||||||||||||    ] 79%

**Invoer:**

    Geef het percentage van de batterij: 100

**Uitvoer:**

    [||||||||||||||||||||] 100%
