### Opgave

Schrijf een programma dat een willekeurig getal genereert tussen 0 en 10. Laat de gebruiker een getal raden. Bij elke poging zegt het programma `Hoger` als het geheime getal groter is dan het ingevoerde getal. Het programma zegt `Lager` als het geheime
getal kleiner is dan het ingevoerde getal. Wanneer het ingevoerde getal juist is, wordt ook het aantal pogingen getoond om het getal te raden.

Voor deze opgave kan je je programma niet testen met Dodona.

Om een willekeurig geheel getal te genereren in het interval $$\mathsf{[a, b]}$$, kun je gebruik maken van deze code:

```python
from random import randint
getal = randint(a,b)         # randint = random integer
```

Tip: bij het testen van je programma is het handig als je het getal kent dat de computer gegenereerd heeft. Zo verlies je niet te veel tijd: je kunt altijd zelf beslissen of je het juiste of een fout antwoord invoert. In de testfase kun je het geheime getal daarom best printen. Zet deze lijn in commentaar zodra je programma klaar is.


### Voorbeeld

**Invoer:**

    Geef een natuurlijk getal: 7


**Uitvoer:**

    Lager

**Invoer:**

    Geef een natuurlijk getal: 4


**Uitvoer:**

    Hoger

**Invoer:**

    Geef een natuurlijk getal: 6


**Uitvoer:**

    Proficiat! Je had 3 pogingen nodig om het juiste getal te raden.
