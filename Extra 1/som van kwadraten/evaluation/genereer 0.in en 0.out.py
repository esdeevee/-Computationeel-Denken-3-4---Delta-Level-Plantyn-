from random import randint
from math import sqrt

def som_van_kwadraten(n):
    for a in range(1, 1 + int(sqrt(n))):
        b = sqrt(n - a**2)
        #print(a, b)
        if int(b) - b == 0:
            return a, int(b)
    return False



# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()



for i in range(25):   
    with open('0.in', 'a') as file:
        kwadraat_of_niet = randint(0, 1)
        if kwadraat_of_niet:
            a = randint(0, 10)
            b = randint(0, 10)
            c = a**2 + b**2
        else:
            c = randint(0, 200)
        file.write('>>> som_van_kwadraten(' + str(c) + ')')
        file.write('\n')

        file.write(str(som_van_kwadraten(c)))
        file.write('\n')
        #file.write('\n')

for i in range(25):   
    with open('0.in', 'a') as file:
        kwadraat_of_niet = randint(0, 1)
        if kwadraat_of_niet:
            a = randint(10, 100)
            b = randint(10, 100)
            c = a**2 + b**2
        else:
            c = randint(100, 10000)
        file.write('>>> som_van_kwadraten(' + str(c) + ')')
        file.write('\n')

        file.write(str(som_van_kwadraten(c)))
        file.write('\n')
        #file.write('\n')

for i in range(50):   
    with open('0.in', 'a') as file:
        kwadraat_of_niet = randint(0, 1)
        if kwadraat_of_niet:
            a = randint(100, 1000)
            b = randint(100, 1000)
            c = a**2 + b**2
        else:
            c = randint(1000, 1000000)
        file.write('>>> som_van_kwadraten(' + str(c) + ')')
        file.write('\n')

        file.write(str(som_van_kwadraten(c)))
        file.write('\n')
        #file.write('\n')
