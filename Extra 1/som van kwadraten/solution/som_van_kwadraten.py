from math import sqrt

def som_van_kwadraten(n):
    for a in range(1, 1 + int(sqrt(n))):
        b = sqrt(n - a**2)
        #print(a, b)
        if int(b) - b == 0:
            return a, int(b)
    return False
