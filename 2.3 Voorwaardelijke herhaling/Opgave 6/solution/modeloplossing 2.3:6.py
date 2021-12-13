# lees twee natuurlijke getallen in
getal_1 = int(input('Geef een eerste natuurlijk getal: '))
getal_2 = int(input('Geef een tweede natuurlijk getal: '))

# je moet weten welk van deze getallen het grootste is
grootste = max(getal_1, getal_2)
kleinste = min(getal_1, getal_2)

# blijf herhalen
while True:
    if kleinste == 0:
        # als kleinste gelijk is aan nul, is de ggd gelijk aan grootste
        ggd = grootste
        # onderbreek de while-lus
        break
    else:
        # ggd(grootste, kleinste) = ggd(kleinste, rest)
        rest = grootste % kleinste
        grootste = kleinste
        kleinste = rest
        
# toon de berekende ggd
print(ggd)
