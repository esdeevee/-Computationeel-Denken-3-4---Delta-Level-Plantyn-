# dit programma vraagt naar de x- en y-coordinaten van twee punten P en Q
# het berekent de waarde van de coefficienten a en b in het voorschrift y = ax + b van de rechte door P en Q
# a en b worden op een lijn getoond
x1 = float(input('Geef de x-coordinaat van P: '))
y1 = float(input('Geef de y-coordinaat van P: '))
x2 = float(input('Geef de x-coordinaat van Q: '))
y2 = float(input('Geef de y-coordinaat van Q: '))
a = (y2 - y1)/(x2 - x1)
b = y1 - a * x1
print(a, b)
