from math import sin, pi
from random import randint

def f(x):
    return sin(x)

def Delta_x(a, b, n):
    return ((b-a) / n)

def x_i(a, b, type):
    if type == 'LINKS':
        return a
    elif type == 'MIDDEN':
        return (a+b)/2
    elif type == 'RECHTS':
        return b

def Riemann(a, b, n, type):
    som = 0
    Dx = Delta_x(a, b, n)
    for i in range(n):
        x = x_i(a + i*Dx, a + (i+1)* Dx, type)
        #print(x, f(x))
        som = som + f(x) * Dx
    return som



# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("1.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("1.out", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("2.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("2.out", "w")
file.truncate()
file.close()



for i in range(30):   
    with open('0.in', 'a') as file:
        exponent = randint(1, 3)
        veelvoud = randint(1, 9)
        teken = randint(0, 1)
        n = veelvoud * 10**exponent
        a = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        b = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> Delta_x(' + str(a) + ', ' + str(b) + ', ' + str(n) + ')')
        file.write('\n')

        file.write(str(Delta_x(a, b, n)))
        file.write('\n')
        #file.write('\n')

for i in range(10):   
    with open('1.in', 'a') as file:
        exponent = randint(1, 3)
        veelvoud = randint(1, 9)
        teken = randint(0, 1)
        a = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        b = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> x_i(' + str(a) + ', ' + str(b) + ', LINKS)')
        file.write('\n')

        file.write(str(x_i(a, b, 'LINKS')))
        file.write('\n')
        #file.write('\n')
        
for i in range(10):   
    with open('1.in', 'a') as file:
        exponent = randint(1, 3)
        veelvoud = randint(1, 9)
        teken = randint(0, 1)
        a = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        b = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> x_i(' + str(a) + ', ' + str(b) + ', MIDDEN)')
        file.write('\n')

        file.write(str(x_i(a, b, 'MIDDEN')))
        file.write('\n')
        #file.write('\n')
        
for i in range(10):   
    with open('1.in', 'a') as file:
        exponent = randint(1, 3)
        veelvoud = randint(1, 9)
        teken = randint(0, 1)
        a = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        b = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> x_i(' + str(a) + ', ' + str(b) + ', RECHTS)')
        file.write('\n')

        file.write(str(x_i(a, b, 'RECHTS')))
        file.write('\n')
        #file.write('\n')

for i in range(10):   
    with open('2.in', 'a') as file:
        exponent = randint(1, 3)
        veelvoud = randint(1, 9)
        teken = randint(0, 1)
        n = veelvoud * 10**exponent
        a = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        b = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> Riemann(' + str(a) + ', ' + str(b) + ', ' + str(n) + ', ' + 'LINKS)')
        file.write('\n')

        file.write(str(Riemann(a, b, n, 'LINKS')))
        file.write('\n')
        #file.write('\n')

for i in range(10):   
    with open('2.in', 'a') as file:
        exponent = randint(1, 3)
        veelvoud = randint(1, 9)
        teken = randint(0, 1)
        n = veelvoud * 10**exponent
        a = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        b = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> Riemann(' + str(a) + ', ' + str(b) + ', ' + str(n) + ', ' + 'MIDDEN)')
        file.write('\n')

        file.write(str(Riemann(a, b, n, 'MIDDEN')))
        file.write('\n')
        #file.write('\n')

for i in range(10):   
    with open('2.in', 'a') as file:
        exponent = randint(1, 3)
        veelvoud = randint(1, 9)
        teken = randint(0, 1)
        n = veelvoud * 10**exponent
        a = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        b = round((-1)**teken * randint(0, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> Riemann(' + str(a) + ', ' + str(b) + ', ' + str(n) + ', ' + 'RECHTS)')
        file.write('\n')

        file.write(str(Riemann(a, b, n, 'RECHTS')))
        file.write('\n')
        #file.write('\n')
