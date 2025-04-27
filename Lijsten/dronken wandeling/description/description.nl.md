### Opgave

Een man komt uit het café en is te dronken om nog de weg naar huis te vinden. Hij wandelt dus doelloos door de stad. Merkwaardig genoeg is hij wel nog in staat om zich te oriënteren volgens het magnetisch veld van de aarde, want elke stap is ofwel pal naar het noorden, het oosten, het zuiden of het westen.

De positie van het café komt overeen met de oorsprong van een orthonormaal assenstelsel. De wandeling van de man wordt voorgesteld door een lijst met als mogelijke elementen
* N: de man zet een stap volgens de positieve oriëntatie van de y-as;
* O: de man zet een stap naar rechts, volgens de positieve oriëntatie van de x-as;
* Z: de man zet een stap omlaag, volgens de negatieve oriëntatie van de y-as;
* W: de man zet een stap naar links, volgens de negatieve oriëntatie van de x-as.

Schrijf een functie `dronken_wandeling(lijst)` die een tuple teruggeeft. Het eerste element van de tuple is opnieuw een tuple met daarin de x- en y- coördinaat van de man op het einde van zijn wandeling. Het tweede element van de tuple is het aantal stappen dat de man in totaal gezet heeft.

### Voorbeeld 1

**Invoer:**

    > dronken_wandeling(['N', 'N', 'N', 'Z', 'Z', 'O', 'W', 'W', 'O'])

**Uitvoer:**

    ((0, 1), 9)

### Voorbeeld 1

**Invoer:**

    > dronken_wandeling(['N', 'W', 'O', 'W', 'O', 'Z', 'N', 'Z', 'W', 'Z', 'W', 'Z', 'N', 'O'])

**Uitvoer:**

    ((-1, -1), 14)