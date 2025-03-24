from math import sin, cos, pi
from random import randint

def f(x):
    return cos(x)

def Delta_x(a, b, n):
    return ((b-a) / n)

def trapeziumregel(a, b, n):
    som = 0
    Dx = Delta_x(a, b, n)
    for i in range(n):
        x_i = a + i*Dx
        x_j = x_i + Dx
        som = som + (f(x_i) + f(x_j))/2 * Dx
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
        teken = randint(0, 1)
        veelvoud = randint(1,9 )
        n = veelvoud * 10**exponent
        a = round((-1)**teken * randint(1, 10**exponent) / (10**exponent + 1), exponent)
        exponent = randint(1, 3)
        teken = randint(0, 1)
        b = round(a +  randint(1, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> Delta_x(' + str(a) + ', ' + str(b) + ', ' + str(n) + ')')
        file.write('\n')

        file.write(str(Delta_x(a, b, n)))
        file.write('\n')
        #file.write('\n')



for i in range(30):   
    with open('1.in', 'a') as file:
        exponent = randint(1, 3)
        veelvoud = randint(1, 9)
        teken = randint(0, 1)
        x = round((-1)**teken * randint(1, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> f(' + str(x) + ')')
        file.write('\n')

        file.write(str(f(x)))
        file.write('\n')
        #file.write('\n')

for i in range(30):   
    with open('2.in', 'a') as file:
        exponent = randint(1, 3)
        teken = randint(0, 1)
        veelvoud = randint(1, 9)
        n = veelvoud * 10**exponent
        a = round((-1)**teken * randint(1, 10**exponent) / (10**exponent + 1), exponent)
        exponent = randint(1, 3)
        teken = randint(0, 1)
        b = round((-1)**teken * randint(1, 10**exponent) / (10**exponent + 1), exponent)
        file.write('>>> trapeziumregel(' + str(a) + ', ' + str(b) + ', ' + str(n) + ')')
        file.write('\n')

        file.write(str(trapeziumregel(a, b, n)))
        file.write('\n')
        #file.write('\n')
