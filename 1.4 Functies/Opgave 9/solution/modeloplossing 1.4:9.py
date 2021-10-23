# lengte_PQ() heeft als invoer de x- en y-coordinaten (floats) van de punten P en Q. De functie stuurt de lengte van het lijnstuk PQ (float) terug.
def lengte_PQ(x1, y1, x2, y2):
    from math import sqrt
    l = sqrt((x2-x1)**2 + (y2-y1)**2)
    return(l)
