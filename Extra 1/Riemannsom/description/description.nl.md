### Opgave

Je hebt bij wiskunde ongetwijfeld geleerd dat je een bepaalde integraal kunt beschouwen als de limiet van de som van een oneindig aantal termen. 

Stel dat we voor een functie $$f(x$$) de oppervlakte onder de grafiek willen uitrekenen in het interval $$[a,b]$$. Riemann bedacht de volgende methode om deze oppervlakte te benaderen:

verdeel het interval 
[
a
,
b
]
{\displaystyle [a,b]} in een eindig aantal, zeg 
n
{\displaystyle n}, deelintervallen,
noem de lengte van het 
i
{\displaystyle i}-de deelinterval 
Δ
n
i
{\displaystyle \Delta _{ni}},
kies een punt 
x
i
{\displaystyle x_{i}} in het 
i
{\displaystyle i}-de deelinterval,
dan wordt de gevraagde oppervlakte benaderd door de som van de te berekenen oppervlakten van de rechthoeken boven de deelintervallen met hoogten 
f
(
x
i
)
{\displaystyle f(x_{i})}. Deze som, de riemannsom, is:

∑
i
=
1
n
f
(
x
i
)
Δ
n
i
{\displaystyle \sum _{i=1}^{n}f(x_{i})\Delta _{ni}}

Zoals steeds in dit soort opgaves mag er in de code die je door Dodona laat evalueren *geen hoofdprogramma* staan. Je code bestaat dus uit twee functiedefinities, en niet meer dan dat. Een eventueel hoofdprogramma dat je gebruikt hebt om je code te testen, moet je bij de evaluatie dus in commentaar zetten, of zelfs gewoon verwijderen.
 
### Voorbeeld 1

**Invoer:**

    >>> fibonacci_iteratief(6)

**Uitvoer:**

    8

### Voorbeeld 2

**Invoer:**

    >>> fibonacci_recursief(7)

**Uitvoer:**

    13