### Opgave

Eendjes vissen is een gekend spel van op de kermis. De eendjes komen één per één voorbij, en de speler kan er een aantal uit vissen. Elk eendje heeft als waarde een natuurlijk getal tussen 1 en 10. 

In deze opgave wordt een variant op het klassieke eendjes vissen beschouwd. De speler ziet op voorhand namelijk de waarden van alle eendjes die voorbij komen. Deze waarden zitten in een lijst. De bedoeling is nu om een welbepaald (maar variabel) aantal opeenvolgende eendjes te selecteren om een zo hoog mogelijke score te behalen. 

Schrijf een functie `eendjes_vissen(lijst, aantal)`. De variabele `lijst` stelt de eendjes voor die de speler voorbij ziet komen. De variabele `aantal` is het aantal eendjes dat de speler mag vissen. De functie geeft een tuple `(positie, score)` terug. Hierbij is `positie` de index van het eerste eendje dat de speler moet vissen, en `score` is de maximale score die hij/zij zo kan behalen.

### Voorbeeld 1

**Invoer:**

    > eendjes_vissen([5, 2, 4, 1, 1, 5, 4, 4, 3, 2], 4)

**Uitvoer:**

    (5, 16)

### Voorbeeld 1

**Invoer:**

    > eendjes_vissen([8, 3, 4, 5, 10], 3)

**Uitvoer:**

    (3, 23)