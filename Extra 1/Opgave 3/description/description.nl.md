Wanneer je tijdens de zomervakantie met de auto door Europa trekt, hoor je soms wel eens dat het een zwart verkeersweekend wordt. Dat betekent: monsterfiles en uren vertragingen. Om daar iets aan te doen, worden in heel Europa camera's geplaatst die het verkeer meten. De camera's staan telkens in paren opgesteld: één op het eerste rijvak om het vrachtwagenverkeer in kaart te brengen en één op het tweede rijvak om het personenvervoer te meten.

De camera's meten per rijvak twee verschillende grootheden:
* De snelheid v van het voorbijrijdende verkeer. Dit kan bijvoorbeeld 93 km/u zijn.
* De verkeersdichtheid d van het rijvak. Bijvoorbeeld 37% van de tijd wordt een voertuig gemeten.

Met deze twee grootheden kan je de kans op een file op het betreffende rijvak berekenen. De formule wordt gegeven door:


$$
\mathsf{P(v,d) = min(\frac{v \cdot d}{40}, 1)}
$$

Wanneer je de kans op file P_v op het rijvak van de vrachtwagens en de kans op file P_a op het rijvak van de personenauto's berekend hebt, dan kan je de kleur als volgt toekennen:
* Het minimum van P_v en P_a is groter dan 0.7:	zwart
* Het maximum van P_v en P_a is groter dan 0.7 en de absolute waarde van het verschil van P_v en P_a kleiner dan 0.2: rood
* De absolute waarde van het verschil van P_v en P_a is groter dan 0.7:	geel
* Alle andere gevallen:	groen

### Opgave

Schrijf een programma dat achtereenvolgens vier gegevens inleest:
* De verkeersdichtheid van het vrachtvervoer op het eerste rijvak;
* De snelheid van het vrachtverkeer op het eerste rijvak;
* De verkeersdichtheid van het personenvervoer op het tweede rijvak;
* De snelheid van de personenwagens op het tweede rijvak.

Je programma toont de kleurcode. Gebruik minstens twee functies in je programma.

### Voorbeeld

**Invoer:**

    0.38
    68
    0.14
    113

**Uitvoer:**

    groen

**Invoer:**

    0.93
    76
    0.74
    83

**Uitvoer:**

    zwart
