# lees de invoer in
getal_1 = float(input('Geef een eerste getal: '))
getal_2 = float(input('Geef een tweede getal: '))
bewerking = input('Geef een bewerking (+, -, *, / of **): ')

# afhankelijk van de ingelezen bewerking bereken en toon je de uitkomst van de bewerking
if bewerking == "+":
    print(getal_1 + getal_2)
elif bewerking == "-":
    print(getal_1 - getal_2)
elif bewerking == "*":
    print(getal_1 * getal_2)
elif bewerking == "/":
    print(getal_1 / getal_2)
elif bewerking == "**":
    print(getal_1 ** getal_2)
