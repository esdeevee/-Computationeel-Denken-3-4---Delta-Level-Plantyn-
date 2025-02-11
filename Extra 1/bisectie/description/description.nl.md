### Inleiding

We gaan nog even verder met numerieke wiskunde, een ideale toepassing om je verder te bekwamen in lussen en functies.

Het doel van deze opdracht is een n-de machtswortel berekenen. Uiteraard kan je de 17-de machtswortel van 82.3 berekenen als 82.3**(1/17), maar je zou deze opdracht ook met pen, papier en veel tijd moeten kunnen doen. Je mag vandaag dus alleen gehele machten gebruiken; een rationale exponent (zoals 1/17) is niet toegelaten.

Je gaat n-de machtswortels berekenen door de veeltermvergelijking f(x) = x**n - c = 0 op te lossen. De oplossing x van deze vergelijking is per definitie de n-de machtswortel van c. We gaan deze vergelijking numeriek oplossen met de bisectiemethode die we eerder al gezien hebben, een naïeve methode die weliswaar heel erg bruikbaar is voor beginners zoals wij. 

Het idee van de bisectiemethode is dat we beginnen met een interval [a,b] waarvoor f(a) en f(b) een verschillend teken hebben. Aangezien f(x) continu is, weten we met zekerheid dat er een oplossing van onze veeltermvergelijking ligt in [a,b]. Je berekent dan m, het midden van het interval [a,b]. Als f(a) en f(m) hetzelfde teken hebben, ligt er geen nulpunt in [a,m]: je moet dus verder zoeken in [m,b]. Als f(a) en f(m) een verschillend teken hebben, ligt het nulpunt in [a,m]. De breedte van het interval waarin je zoekt, halveert dus in elke stap. Na 10 stappen is de breedte nog 1/1024 van het oorspronkelijke interval. Na 30 stappen heb je bij benadering nog maar 1/10**9 van het oorspronkelijke interval. Als je begint met een interval van breedte 1, heb je na een 30-tal stappen 9 decimalen van de gezochte n-de machtswortel.

Je blijft deze methode toepassen tot je x gevonden hebt. Het probleem is dat de vergelijking f(x) = x**n - c = 0 in het algemeen geen exacte oplossing heeft. f(x) kan enorm dicht naar nul naderen, maar zal meestal nooit exact gelijk aan nul zijn. We stellen ons tevreden wanneer f(x) in absolute waarde kleiner is dan een waarde e (die we de toleratie noemen), met e een heel klein getal. Pas als dat het geval is, mag de lus onderbroken worden. De waarde van x op dat moment is dan een benadering voor de gezochte n-de machtswortel van c.

### Opgave

Let op: je mag in deze opgave géén hoofdprogramma schrijven! Dus er mag géén input() of print() in de code staan die je evalueert.

Schrijf een functie midden(a, b) die het midden van interval [a, b] teruggeeft. Probeer Voorbeeld 1 te begrijpen.

Schrijf een functie f(x, n, c) die de functiewaarde van f(x) = x**n - c teruggeeft. Probeer Voorbeeld 2 te begrijpen.

Schrijf een functie n_de_machtswortel_bisectie(n, x, a, b, e) die de n-de machtswortel van x berekent door de bisectiemethode toe te passen in het interval [a,b] met toleratie e. Probeer Voorbeeld 3 te begrijpen: we lossen de vergelijking x**2 - 3 = 0 op door de bisectiemethode toe te passen op het interval [0, 5]. De tolerantie is 1e-12.


### Voorbeeld 1

**Invoer:**

    > midden(15.4, 18.8)

**Uitvoer:**

    17.1

### Voorbeeld 2

**Invoer:**

  > f(2, 10, 1000)

**Uitvoer:**

  24

### Voorbeeld 3

**Invoer:**

  > n_de_machtswortel_bisectie(2, 3, 0, 5, 1e-12)

**Uitvoer:**

  1.7320508075687258
