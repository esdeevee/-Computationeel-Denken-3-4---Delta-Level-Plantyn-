### Inleiding

Je hebt bij wiskunde geleerd dat je een bepaalde integraal kunt beschouwen als de som van een oneindig aantal termen. De Duitse wiskundige Bernhard Riemann (1826-1866) bedacht immers de volgende methode om een benadering te vinden voor de (georiënteerde) oppervlakte onder de grafiek van $$f(x)$$ in het interval $$[a,b]$$:
1. verdeel het interval $$[a,b]$$ in $$n$$ gelijke deelintervallen met breedte $$\Delta x$$;
2. kies een willekeurige waarde $$x_{i}$$ in het $$i$$-de deelinterval;
3. bereken de functiewaarde $$f(x_{i})$$;
4. $$\displaystyle \sum _{i=1}^{n}f(x_{i}) \cdot \Delta x \,$$ is dan een benadering voor de exacte oppervlakte $$\displaystyle \int _{a}^{b} f(x) \, dx$$. 

### Opgave

1. Schrijf een functie `Delta_x(a, b, n)` die de breedte $$\Delta x$$ van elk deelinterval berekent wanneer je $$[a,b]$$ verdeelt in $$n$$ gelijke deelintervallen.
2. Schrijf een functie `x_i(x1, x2, type)` die een waarde teruggeeft in het (deel)interval $$[x_1, x_2]$$:
    * als `type` gelijk is aan `'LINKS'`, geeft de functie de waarde van `x1` terug;
    * als `type` gelijk is aan `'MIDDEN'`, geeft de functie het midden van $$[x_1, x_2]$$ terug;
    * als `type` gelijk is aan `'RECHTS'`, geeft de functie de waarde van `x2` terug.
3. We maken in deze opgave gebruik van $$f(x) = \sin x$$. Schrijf een functie `f(x)` die de waarde van $$\sin(x)$$ teruggeeft.
4. Schrijf een functie `Riemannsom(a, b, n, type)` die de waarde van $$\displaystyle \sum _{i=1}^{n}f(x_{i}) \cdot \Delta x \,$$ teruggeeft, waarbij $$\Delta x$$ en $$x_i$$ berekend worden zoals hierboven beschreven.

Zoals steeds in dit soort opgaves mag er in de code die je door Dodona laat evalueren *geen hoofdprogramma* staan. Je code bestaat dus uit drie (vier?) functiedefinities, en niet meer dan dat. Een eventueel hoofdprogramma dat je gebruikt hebt om je code te testen, moet je bij de evaluatie dus in commentaar zetten, of zelfs gewoon verwijderen.
 
### Voorbeeld 1

**Invoer:**

    >>> Delta_x(0, 1, 1000)

**Uitvoer:**

    0.001

### Voorbeeld 2

**Invoer:**

    >>> x_i(0, 0.001, 'LINKS')

**Uitvoer:**

    0

### Voorbeeld 3

**Invoer:**

    >>> x_i(0, 0.001, 'MIDDEN')

**Uitvoer:**

    0.0005

### Voorbeeld 4

**Invoer:**

    >>> x_i(0, 0.001, 'RECHTS')

**Uitvoer:**

    0.001

### Voorbeeld 5

**Invoer:**

    >>> f(1.5707963267948966)

**Uitvoer:**

    1.0

### Voorbeeld 6

**Invoer:**

    >>> Riemannsom(0, 1.0471975511965976, 1000, 'MIDDEN')

**Uitvoer:**

    0.5000000228463071

### Voorbeeld 7

**Invoer:**

    >>> Riemannsom(0, 3.141592653589793, 1000000, 'LINKS')

**Uitvoer:**

    1.9999999999983495
    