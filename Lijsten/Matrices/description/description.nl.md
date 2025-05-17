### Herhaling matrices
We zullen het in deze opgave hebben over matrices. Matrices zouden voor niemand een probleem mogen zijn, maar om zeker te zijn dat je niet struikelt over de wiskunde, wil ik toch graag een paar zaken opfrissen. Wie deze herhaling niet nodig denk te hebben, kan dit deel probleemloos overslaan.

Beschouw de matrix 

$$A = \begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix}$$.

We zeggen dat $$A$$ 2 rijen heeft en 3 kolommen. Formeel wordt dat genoteerd als $$A \in \mathbb{R}^{2 \times 3}$$, of ook als $$\dim A = 2 \times 3$$.

Je hebt vorig jaar geleerd hoe je matrices moet vermenigvuldigen. De details doen er niet toe, maar de dimensies zijn wel belangrijk voor deze opgave. Het is namelijk zo dat 

$$\forall A \in \mathbb{R}^{m \times n}, \forall B \in \mathbb{R}^{n \times p}: A \cdot B \in \mathbb{R}^{m \times p}$$.

De getransponeerde van een matrix $$A$$ vind je door de rijen en kolommen van $$A$$ onderling te wisselen. Het element op de $$i$$-de rij en $$j$$-de kolom van $$A$$ komt zo op de $$j$$-de rij en $$i$$-de kolom van $$A^T$$. Formeel: 

$$\forall A \in \mathbb{R}^{m \times n}: B = A^T \in \mathbb{R}^{n \times m} \Leftrightarrow b_{ij} = a_{ji} \hspace{1cm} (\forall i, j)$$. 

Voor onze matrix $$A$$ is dus 

$$A^T = \begin{bmatrix}
1 & 4\\
2 & 5\\
3 & 6
\end{bmatrix}$$.

### Matrices in Python

Matrices kunnen in Python voorgesteld worden als een lijst van lijsten. Zo kan bovenstaande matrix voorgesteld worden als de lijst `A = [[1, 2, 3], [4, 5, 6]]`. 

Om te verwijzen naar het element op de `i`-de rij en `j`-de kolom, gebruik je `A[i][j]`. Zo is bv. `A[1][2] = 6`. Als je het hier niet meteen mee eens bent, bedenk dan dat `i` en `j` beginnen bij 0, en niet bij 1, zoals je gewoon bent.

### Opgave

*Je zou het stilaan zelf moeten weten, maar ik herhaal nog eens dat de automatische evaluatie van Dodona in de problemen komt wanneer je code een hoofdprogramma bevat. In de code die je indient, mag dus geen `input()`, `print()` of iets dergelijks voorkomen.*

1. Schrijf een functie `is_matrix(lijst)`. Wanneer `lijst` voldoet aan de wiskundige definitie van een matrix, geeft je functie `True` terug. Als dat niet zo is, geeft je functie `False` terug.
2. Schrijf een functie `dimensies(matrix)`. `matrix` stelt een wiskundig correcte matrix voor. Je functie geeft een tuple `(m, n)` terug, waarin `m` het aantal rijen en `n` het aantal kolommen voorstelt van de matrix.
3. Schrijf een functie `product(A, B)`. `A` en `B` stellen wiskundig correcte matrices voor. Als het product $$A \cdot B$$ bestaat, geeft je programma een tuple `(m, n)` terug, waarin `m` het aantal rijen en `n` het aantal kolommen voorstelt van het product van `A` en `B`. Als het product $$A \cdot B$$ niet bestaat, geeft je programma `False` terug.
3. Schrijf een functie `transpose(A)`. `A` stelt een wiskundig correcte matrix voor. Je functie geeft de getransponeerde van `A` terug.


### Voorbeeld 1

**Invoer:**

    > is_matrix([[1, 2, 3], [4, 5, 6]])


**Uitvoer:**

    True


### Voorbeeld 2

**Invoer:**

    > is_matrix([[1, 2, 3], [4, 5, 6, 7]])


**Uitvoer:**

    False


### Voorbeeld 3

**Invoer:**

    > dimensies([[1, 2, 3], [4, 5, 6]])


**Uitvoer:**

    (2, 3)


### Voorbeeld 4

**Invoer:**

    > product([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]])


**Uitvoer:**

    False

### Voorbeeld 5

**Invoer:**

    > product([[1, 2], [3, 4], [5, 6]], [[7, 8, 9], [10, 11, 12]])


**Uitvoer:**

    (3, 3)


### Voorbeeld 6

**Invoer:**

    > transpose([[1, 2, 3], [4, 5, 6]])


**Uitvoer:**

    [[1, 4], [2, 5], [3, 6]]
