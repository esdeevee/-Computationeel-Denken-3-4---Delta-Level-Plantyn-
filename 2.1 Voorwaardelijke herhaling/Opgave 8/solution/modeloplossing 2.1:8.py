# lees de gemiddelde score in
gemiddelde = float(input('Geef de gemiddelde score: '))

# bepaal de graad
if gemiddelde < 68:
    graad = 'V'
elif 68 <= gemiddelde < 77:
    graad = 'O'
elif 77 <= gemiddelde < 85:
    graad = 'GO'
elif 85 <= gemiddelde < 90:
    graad = 'GGO'
elif gemiddelde >= 90:
    graad = 'F'

# schrijf de graad uit
print(graad)
