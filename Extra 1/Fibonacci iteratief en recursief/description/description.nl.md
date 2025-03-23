### Opgave

De rij van Fibonacci is wellicht het typevoorbeeld van een wiskundige rij die heel gemakkelijk recursief kan worden gedefinieerd:

* de eerste en de tweede term van de rij zijn gelijk aan 1;
* elke volgende term is gelijk aan de som van de twee voorgaande termen.

Als we het $n$-de getal van Fibonacci noteren als $$F_n$$, kan je de rij dus formeel definiëren als

$$F_1 = F_2 = 1$$

en 

$$F_n = F_{n-1} + F_{n-2}.$$

De rij van Fibonacci bestaat dus uit de getallen 1, 1, 2, 3, 5, 8, 13, 21, ...

1. Schrijf een functie `fibonacci_iteratief(n)` die op een *iteratieve* manier het $n$-de getal berekent in de rij van Fibonacci. De 17 leerlingen die Opgave 11 van Hoofdstuk 2.2 gemaakt hebben als voorbereiding op het examen in december, genieten hier een klein voordeel.
2. Schrijf een functie `fibonacci_recursief(n)` die op een *recursieve* manier het $n$-de getal berekent in de rij van Fibonacci.

Zoals steeds in dit soort opgaves mag er in de code die je door Dodona laat evalueren *geen hoofdprogramma* staan. Je code bestaat dus uit twee functiedefinities, en niet meer dan dat. Een eventueel hoofdprogramma dat je gebruikt hebt om je code te testen, moet je bij de evaluatie dus in commentaar zetten, of zelfs gewoon verwijderen.
 
### Voorbeeld 1

**Invoer:**

    > fibonacci_iteratief(6)

**Uitvoer:**

    8

### Voorbeeld 2

**Invoer:**

    > fibonacci_recursief(7)

**Uitvoer:**

    13