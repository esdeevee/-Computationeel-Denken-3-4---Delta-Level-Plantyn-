def gemiddelde(lijst):
    som = 0
    for getal in lijst:
        som += getal
    return round(som / len(lijst), 1)
    
def mediaan(lijst):
    n = len(lijst)
    lijst.sort()
    if n % 2 == 1:
        return round(lijst[int((n-1)/2)], 1)
    else:
        return round(gemiddelde([lijst[int(n/2 - 1)], lijst[int(n/2)]]), 1)

def Q1(lijst):
    n = len(lijst)
    lijst.sort()
    if n % 2 == 1:
        return round(mediaan(lijst[:int((n+1)/2)]), 1)
    else:
        return round(mediaan(lijst[:int(n/2)]), 1)

def Q3(lijst):
    lijst.sort()
    n = len(lijst)
    if n % 2 == 1:
        return round(mediaan(lijst[int((n-1)/2):]), 1)
    else:
        return round(mediaan(lijst[int(n/2):]), 1)

def IKA(lijst):
    return Q3(lijst) - Q1(lijst)

def standaardafwijking(lijst):
    from math import sqrt
    n = len(lijst)
    som = 0
    gem = gemiddelde(lijst)
    for getal in lijst:
        som += (getal - gem)**2
    return round(sqrt(som / (n-1)), 1)
