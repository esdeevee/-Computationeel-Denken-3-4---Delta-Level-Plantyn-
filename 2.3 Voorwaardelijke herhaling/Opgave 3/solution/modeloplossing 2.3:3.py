# lees een natuurlijk getal in
getal = input('Geef een natuurlijk getal: ')

# je kunt verwijzen naar het i-de karakter van een string
# je kunt niet verwijzen naar het i-de karakter van een integer
# kies daarom voor getal het datatype string

# blijf herhalen
while int(getal) > 9:
    # zet de waarde van som op 0
    som = 0
    # bereken de som van alle cijfers van getal
    for i in range(len(getal)):
        som = som + int(getal[i])
    # som heeft nog minstens 2 cijfers
    # met deze waarde van som moet je verder
    # getal neemt nu de waarde aan van som
    # som is een integer, dus je moet deze eerst nog converteren naar het datatype string 
    getal = str(som)
    # je zou de tussenstappen kunnen (moeten) controleren door getal te printen:
    # print(getal)
    
# print het gezochte cijfer
print(som)
