"""
# dit programma vraagt een lengte in centimeter
# het zet deze lengte om naar feet en inch
# het aantal feet is altijd een natuurlijk getal
# het aantal inch wordt afgerond naar 0,1 inch
cm = float(input('Geef een lengte (in cm): '))
# het aantal feet moet natuurlijk zijn, dus we gebruiken de functie int()
feet = int(cm // 30.48)
inch = round((cm % 30.48) / 2.54, 1)
print(feet, inch)
"""

def
