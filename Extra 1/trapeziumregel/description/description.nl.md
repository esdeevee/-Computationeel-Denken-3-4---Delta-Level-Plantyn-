### Inleiding

Je hebt bij wiskunde geleerd dat je een bepaalde integraal kunt beschouwen als de som van een oneindig aantal termen.  De details zijn hier niet van belang, maar grafisch komt deze methode neer op het optellen van de oppervlakte van een groot aantal rechthoekjes. Onderstaande figuur geeft een mogelijke manier om de riemannsom te berekenen.

![riemannsom](media/riemannsom.png){:width="25%"}

Je zou kunnen zeggen dat je $$f(x)$$ in elk deelinterval benadert door een functie van de nulde graad (een constante functie). Al bij al is dit een vrij grove benadering, die weliswaar nadert naar de correcte georiënteerde oppervlakte naarmate het aantal deelintervalletjes toeneemt.

We gaan in deze opgave een kleine verfijning doorvoeren aan de riemannsom die je kent. In plaats van de georiënteerde oppervlakte te beschouwen als de som van rechthoekjes, kunnen we misschien beter de som berekenen van een groot aantal trapeziums. Zo benaderen we $$f(x)$$ in elk deelinterval door een functie van de eerste graad. Onderstaande figuur illustreert dat deze *trapeziumregel* voor een zelfde aantal deelintervalletjes in het algemeen een betere benadering geeft dan de riemannsom die je kent.

![trapeziumregel](media/trapeziumregel.png){:width="25%"}

De oppervlakte van een trapezium met grote basis $$B$$, kleine basis $$b$$ en hoogte $$h$$ kun je berekenen als $$\frac{B+b}{2} \cdot h$$. Als we het $$i$$-de deelinterval definiëren als $$[x_i, x_{i+1}]$$, vind je de oppervlakte van de $$i$$-de deeltrapezium dus als $$\displaystyle \frac{f(x_i) + f(x_{i+1})}{2} \cdot \Delta x$$. De totale oppervlakte van alle deeltrapeziums wordt dus gegeven door $$\sum _{i=1}^{n} \frac{f(x_{i}) + f(x_{i+1})}{2} \cdot \Delta x \,$$.

### Opgave

1. Schrijf een functie `Delta_x(a, b, n)` die de breedte $$\Delta x$$ van elk deelinterval berekent wanneer je $$[a,b]$$ verdeelt in $$n$$ gelijke deelintervallen.
2. We maken in deze opgave gebruik van $$f(x) = \cos x$$. Schrijf een functie `f(x)` die de waarde van $$\cos(x)$$ teruggeeft.
3. Schrijf een functie `trapeziumregel(a, b, n)` die de waarde van $$\displaystyle \sum _{i=1}^{n}f(x_{i}) \cdot \Delta x \,$$ teruggeeft, waarbij $$\Delta x$$ en $$x_i$$ berekend worden zoals hierboven beschreven. *Uiteraard steun je in deze definitie zo veel mogelijk op de functies die je in 1 en 2 al gedefinieerd hebt.*

Zoals steeds in dit soort opgaves mag er in de code die je door Dodona laat evalueren *geen hoofdprogramma* staan. Je code bestaat dus uit drie functiedefinities, en niet meer dan dat. Een eventueel hoofdprogramma dat je gebruikt hebt om je code te testen, moet je bij de evaluatie dus in commentaar zetten, of zelfs gewoon verwijderen.
 
### Voorbeeld 1

**Invoer:**

    >>> Delta_x(0, 1, 1000)

**Uitvoer:**

    0.001

