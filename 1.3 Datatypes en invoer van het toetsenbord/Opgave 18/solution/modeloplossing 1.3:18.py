# dit programma vraagt een lengte in centimeter
# het zet deze lengte om naar foot en inch
# het aantal foot is altijd een natuurlijk getal
# het aantal inch wordt afgerond op 0,1 inch
cm = float(input('Geef een lengte (in cm): '))
# het aantal foot moet natuurlijk zijn, dus je gebruikt de functie round()
foot = round(cm // 30.48)
inch = round((cm % 30.48) / 2.54, 1)
print(foot, inch)
