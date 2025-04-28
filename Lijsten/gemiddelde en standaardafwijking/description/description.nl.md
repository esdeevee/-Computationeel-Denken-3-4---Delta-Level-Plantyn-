### Inleiding

Er zijn verschillende manieren om het centrum van een aantal getallen te karakteriseren. De bekendste zijn wellicht het gemiddelde en de mediaan. 
Je berekent het gemiddelde van de getallen $$x_1, x_2, \ldots, x_n$$ als volgt:

$$\overline x = \frac{1}{n} \cdot \sum_{i=1}^n x_i.$$

De mediaan van een aantal getallen vind je door ze te sorteren van klein naar groot. Bij een oneven aantal getallen is de mediaan dan gelijk aan het middelste getallen. Voor een even aantal getallen is de mediaan gelijk aan het gemiddelde van de twee middelste getallen.

Er zijn ook verschillende manieren om de spreiding van een aantal getallen te karakteriseren. Je kent misschien de interkwartielafstand. Deze is het verschil van het derde met het eerste kwartiel. Het eerste kwartiel ($$Q_1$$) is de mediaan van de kleinste helft waarnemingsgetallen. Het derde kwartiel ($$Q_3$$) is de mediaan van de grootste helft waarnemingsgetallen. 
Daarnaast ken je misschien ook de standaardafwijking als maat voor de spreiding van een aantal getallen. Je berekent deze als volgt:

$$s = \sqrt{\frac{1}{n-1} \cdot \sum_{i=1}^n (x_i - \overline x)^2}.$$

### Opgave
1. Schrijf een functie `gemiddelde(lijst)`. De variabele `lijst` bevat een aantal getallen. Je functie geeft het gemiddelde van de al deze getallen terug, afgerond op 1 cijfer na de komma.
2. Schrijf een functie `mediaan(lijst)`. De variabele `lijst` bevat een aantal getallen. Je functie geeft de mediaan van de al deze getallen terug, afgerond op 1 cijfer na de komma.
3. Schrijf een functie `Q1(lijst)`. De variabele `lijst` bevat een aantal getallen. Je functie geeft het eerste kwartiel van de al deze getallen terug, afgerond op 1 cijfer na de komma.
4. Schrijf een functie `Q3(lijst)`. De variabele `lijst` bevat een aantal getallen. Je functie geeft het derde kwartiel van de al deze getallen terug, afgerond op 1 cijfer na de komma.
5. Schrijf een functie `IKA(lijst)`. De variabele `lijst` bevat een aantal getallen. Je functie geeft de interkwartielafstand van de al deze getallen terug, afgerond op 1 cijfer na de komma.
6. Schrijf een functie `standaardafwijking(lijst)`. De variabele `lijst` bevat een aantal getallen. Je functie geeft de standaardafwijking van de al deze getallen terug, afgerond op 1 cijfer na de komma.


### Voorbeeld 1

**Invoer:**

    > gemiddelde([-8, 5, 8, 0, 2])

**Uitvoer:**
	
	1.4
    
### Voorbeeld 2

**Invoer:**

    > mediaan([-2, -1, -10, -7, 7, -2])

**Uitvoer:**

	-2.0

 ### Voorbeeld 3

**Invoer:**

    > Q1([-2, -1, -10, -7, 7, -2])

**Uitvoer:**

	-2.0

 ### Voorbeeld 4

**Invoer:**

    > Q3([-2, -1, -10, -7, 7, -2])

**Uitvoer:**

	-2.0
    
