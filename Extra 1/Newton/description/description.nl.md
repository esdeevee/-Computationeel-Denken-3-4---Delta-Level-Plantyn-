### Inleiding

We gaan nog even verder met numerieke wiskunde, een ideale toepassing om je verder te bekwamen in lussen en functies.

We gaan opnieuw doel een n-de machtswortel berekenen. Net als vorige week gaan we dus de veeltermvergelijking $$f(x)$$ = x**n - c = 0 oplossen. Alleen gaan we deze keer een efficiënter algoritme gebruiken.

De methode van Newton-Raphson heeft een startwaarde ($$x_0$$) nodig voor het gezochte nulpunt ($$x_r$$). We nemen aan dat $$x_0$$ in de buurt ligt van $$x_r$$. Tenzij je extreem veel geluk hebt, is $$x_0$$ geen oplossing van onze vergelijking. We willen nu een $$x_1$$ vinden die een betere schatting is voor $$x_r$$ dan de oorspronkelijke $$x_O$$. We doen dat door $$f(x)$$ rond $$x_0$$ te benaderen door de raaklijn aan $$f(x)$$ in $$x_0$$. Deze raaklijn snijdt de x-as in $$x_1$$. Zoals je grafisch kan inzien, ligt $$x_1$$ dichter bij $$x_r$$ dan $$x_0$$.

Je blijft deze methode toepassen tot je een x gevonden hebt waarvoor $$f(x)$$ in absolute waarde kleiner is dan een waarde $$e$$ (die we de toleratie noemen), met $$e$$ een heel klein getal. Pas als dat het geval is, mag de lus onderbroken worden. De waarde van $$x$$ op dat moment is dan een benadering voor de gezochte n-de machtswortel van $$c$$.

### Opgave

1. Gebruik je wiskundige kennis om een formule te vinden voor $$x_1$$ in functie van $$x_0$$.

**Let op**: je mag in deze opgave *géén hoofdprogramma* schrijven! Dus er mag *géén input() of print()* in de code staan die je evalueert.

2. Schrijf een functie f(x, n, c) die de functiewaarde van $$f(x) = x**n - c$$ teruggeeft. Probeer Voorbeeld 1 te begrijpen.

2. Schrijf een functie afgeleide(x, n, c) die de $$f'(x_0)$$ teruggeeft (met $$f(x) = x**n - c$$). Probeer Voorbeeld 2 te begrijpen.

3. Schrijf een functie nulpunt_raaklijn(x, n, c) die de x-coördinaat van het snijpunt geeft van de raaklijn aan de grafiek van $$f(x) = x**n - c$$ voor $$x=x_0$$. Maak maximaal gebruik van functies die je al gedefinieerd hebt. Probeer Voorbeeld 3 te begrijpen.

4. Schrijf een functie n_de_machtswortel_Newton(n, c, x_0, e) die de vergelijking $$f(x) = 0$$ oplost via de methode van Newton-Raphson, met een startwaarde x_O en een tolerantie e. Probeer Voorbeeld 4 te begrijpen: we lossen de vergelijking x**2 - 3 = 0 op door de bisectiemethode toe te passen met een startwaarde van 5. De tolerantie is 1e-15.

### Voorbeeld 1

**Invoer:**

    > f(5, 2, 3)

**Uitvoer:**

    22

### Voorbeeld 2

**Invoer:**

    > afgeleide(5, 2, 3)

**Uitvoer:**

    10

### Voorbeeld 3

**Invoer:**

    > nulpunt_raaklijn(5, 2, 3)

**Uitvoer:**

    2.8

### Voorbeeld 4

**Invoer:**

    > n_de_machtswortel_Newton(2, 3, 5, 1e-15)

**Uitvoer:**

    1.7320508075688774
