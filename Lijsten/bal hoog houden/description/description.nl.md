### Inleiding

Je wilt een nieuwe klascompetitie organiseren. Deelnemers aan deze competitie moeten een bal zo lang mogelijk hooghouden, d.w.z. de bal raken zonder dat deze de grond raakt. Je telt voor elke kandidaat het aantal baltoetsen, en op basis daarvan bereken je een score:
* De speler start in niveau 1; elke baltoets is 1 punt waard.
* Vanaf de 11de baltoets zit de speler in niveau 2; de baltoetsen zijn nu elk 2 punten waard.
* Vanaf de 21ste baltoets zit de speler in niveau 3; de baltoetsen zijn nu elk 3 punten waard.
* ...

Een speler die de bal 22 keer hoog kan houden, behaalt daarmee dus een individuele score van 10x1 + 10x2 + 2x3 = 36 punten.

Per klas mogen verschillende leerlingen deelnemen. Elke leerling krijgt 1 kans. De totale score van een klas wordt berekend als het gemiddelde van de scores van alle deelnemende leerlingen. Dit gemiddelde wordt vervolgens afgerond naar beneden.

### Opgave

1. Schrijf een functie `niveau(n)`. De variabele `n` stelt de `n`-de baltoets voor. De functie geeft het niveau terug waarin de speler zit bij de `n`-de baltoets. Dit getal is gelijk aan de score die de kandidaat verdient met deze ene baltoets. 
2. Schrijf een functie `score(aantal)`. De variabele `aantal`stelt het aantal baltoetsen voor dat een kandidaat heeft behaald. De functie geeft de totale score terug van deze kandidaat.
3. Schrijf een functie `klasresultaat(lijst)`. In de variabele `lijst` zitten het aantal baltoetsen van alle deelnemers in een klas. Elk van deze aantallen is een natuurlijk getal. De uitvoer van je functie is de gemiddelde score van alle deelnemers in deze klas. 

### Voorbeeld 1

**Invoer:**

    > niveau(22)

**Uitvoer:**

    3

### Voorbeeld 2

**Invoer:**

    > score(22)

**Uitvoer:**

    36

### Voorbeeld 3

**Invoer:**

    > klasresultaat([3, 17, 42, 26])

**Uitvoer:**

    46