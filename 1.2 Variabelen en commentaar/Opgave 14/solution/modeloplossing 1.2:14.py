# dit programma berekent de waarde van de coefficienten a en b in het voorschrift y = ax + b van de rechte door P(x1, y1) en Q(x2, y2)
x1 = -1
y1 = 1
x2 = 7
y2 = 5
a = (y2 - y1)/(x2 - x1)
b = y1 - a * x1
print(a, b)
