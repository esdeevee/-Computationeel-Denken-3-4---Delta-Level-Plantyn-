# dit programma zet een lengte (uitgedrukt in centimeter) om naar foot en inch
# het aantal foot is altijd een natuurlijk getal
# het aantal inch wordt afgerond op 0,1 inch
cm = 168
foot = cm // 30.48
inch = round((cm % 30.48) / 2.54)
print(foot, inch)
