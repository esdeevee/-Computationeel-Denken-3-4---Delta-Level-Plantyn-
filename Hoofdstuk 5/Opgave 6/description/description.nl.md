### Heuvelrace (VPW 2016)

Je wil een nieuw spel, heuvelrace, op de markt brengen waarbij een heuvelend parcours wordt afgelegd met een wagentje. Het doel van het spel is zoveel mogelijk punten te scoren. Eén manier om punten te scoren is door snel een heuvel op te rijden om zo een sprong te maken met het wagentje. Hoe langer het wagentje in de lucht is tijdens een sprong, hoe meer punten de speler verzamelt.

Jouw taak is om te berekenen hoeveel punten de speler heeft verdiend met de sprongen die hij of zij heeft uitgevoerd. Het puntensysteem voor één sprong werkt als volgt:
* Voor de eerste 4 seconden verdient men 25 punten per seconde;
* de volgende 4 seconden leveren 100 punten per seconde op;
* de daaropvolgende 4 seconden leveren 500 punten per seconde op;
* hierna levert elke bijkomende seconde 1000 punten op.

Een sprong van 11 seconden levert dus 25 + 25 + 25 + 25 + 100 + 100 + 100 + 100 + 500 + 500 + 500 = 2000 punten op.

Alle getallen in de invoer die op dezelfde regel voorkomen, worden gescheiden door 1 enkele spatie. De eerste regel bevat het aantal opgaven n (1 ≤ n ≤ 100). Daarna volgen n opgaven. Elke opgave bestaat uit twee regels. Op de eerste regel staat het aantal sprongen s voor dit spel. Het aantal sprongen is steeds minstens één en is hoogstens 50. Op de tweede regel staan dan s strikt positieve natuurlijke getallen telkens van elkaar gescheiden door één enkele spatie; elk getal geeft de duur van een sprong in seconden.

De uitvoer bestaat uit n regels. Op elke regel staan twee natuurlijke getallen van elkaar gescheiden door één spatie. Het eerste getal is het volgnummer van de opgave. Het tweede getal is het totaal aantal punten verdiend in dit spel.

### Voorbeeld

**Invoer:**

    3
    1
    11
    2
    13 1
    3
    2 6 10

**Uitvoer:**

    1 2000
    2 3525
    3 1850
