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
    if n % 2 == 1:
        return round(mediaan(lijst[:int((n+1)/2)]), 1)
    else:
        return round(mediaan(lijst[:int(n/2)]), 1)

def Q3(lijst):
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
    
"""
lijst1 = [5, 3, 1, 4, 2]

print(gemiddelde(lijst1))
print(mediaan(lijst1))
print(Q1(lijst1))
print(Q3(lijst1))
print(IKA(lijst1))
print(standaardafwijking(lijst1))

print('\n')

lijst1 = [5, 3, 6, 1, 4, 2]

print(gemiddelde(lijst1))
print(mediaan(lijst1))
print(Q1(lijst1))
print(Q3(lijst1))
print(IKA(lijst1))
print(standaardafwijking(lijst1))
"""

from random import randint

# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()

for i in range(1, 11):
    for k in range(10):  
        lijst = []
        aantal = randint(5, 10*i)
        for j in range(aantal):
            getal = randint(-10*i, 10*i)
            lijst.append(getal)
        """
        with open('0.in', 'a') as file:
            file.write('>>> gemiddelde(' + str(lijst) + ')')
            file.write('\n')
            file.write(str(gemiddelde(lijst)))
            file.write('\n')
        """
        print('>>> standaardafwijking(' + str(lijst) + ')')
        #print('\n')
        print(str(standaardafwijking(lijst)))
        #print('\n')