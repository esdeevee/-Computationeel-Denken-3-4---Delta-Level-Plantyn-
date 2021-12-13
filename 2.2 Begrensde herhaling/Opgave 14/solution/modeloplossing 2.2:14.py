# lees een natuurlijk getal in
# bewaar het getal als datatype string
# zo kun je itereren over de verschillende karakters van de string 
# deze verschillende karakters zijn de afzonderlijke cijfers van het getal
getal = input('Geef een natuurlijk getal: ')

# definieer een numerieke variabele som
# bij het begin van het programma is de waarde van som gelijk aan nul
som = 0

for cijfer in getal:
    # cijfer is van het datatype string
    # zet deze om naar een integer en tel deze bij de vorige waarde van de variabele som
    som = som + int(cijfer)
print(som)
