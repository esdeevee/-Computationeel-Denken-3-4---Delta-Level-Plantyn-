from random import randint

def f(x, n, c):
    return x**n - c

def midden(a, b):
    return (a + b)/2

def n_de_machtswortel_bisectie(n, c, a, b, e):
    aantal_iteraties = 0
    while True:
        m = (a+b)/2
        aantal_iteraties += 1
        if abs(f(m, n, c)) < e:
            break
        else:
            if f(a, n, c)*f(m, n, c) < 0:
                b = m
            else:
                a = m
    return m#, aantal_iteraties

def f(x, n, c):
    return x**n - c

def afgeleide(x, n, c):
    return n * x**(n-1)

def nulpunt_raaklijn(x, n, c):
    return x - f(x, n, c) / afgeleide(x, n, c)

def n_de_machtswortel_Newton(n, c, x, e):
    # herhaal tot |f(x, n, c)| < e
    # aantal_iteraties = 0
    while True:
        if abs(f(x, n, c)) < e:
            break
        else:
            x = nulpunt_raaklijn(x, n, c)
            # aantal_iteraties += 1
    return x #, aantal_iteraties



# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()

# wis alle gegevens in in.csv
file = open("1.in", "w")
file.truncate()
file.close()

# wis alle gegevens in in.csv
file = open("2.in", "w")
file.truncate()
file.close()

# wis alle gegevens in in.csv
file = open("3.in", "w")
file.truncate()
file.close()


# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()

# wis alle gegevens in in.csv
file = open("1.out", "w")
file.truncate()
file.close()

# wis alle gegevens in in.csv
file = open("2.out", "w")
file.truncate()
file.close()

# wis alle gegevens in in.csv
file = open("3.out", "w")
file.truncate()
file.close()




for i in range(25):   
    with open('0.in', 'a') as file:
        x = randint(-10, 10)
        n = randint(2, 5)
        c = x**n + randint(-10, 10)
        file.write('>>> f(' + str(x) + ', ' + str(n) + ', ' + str(c) + ')')
        file.write('\n')

        file.write(str(f(x, n, c)))
        file.write('\n')
        #file.write('\n')

for i in range(25):   
    with open('0.in', 'a') as file:
        x = randint(-100, 100)/10
        n = randint(2, 5)
        c = round(x**n + randint(-100, 100)/10, 1)
        file.write('>>> f(' + str(x) + ', ' + str(n) + ', ' + str(c) + ')')
        file.write('\n')

        file.write(str(f(x, n, c)))
        file.write('\n')
        #file.write('\n')



for i in range(25):   
    with open('1.in', 'a') as file:
        x = randint(-10, 10)
        n = randint(2, 5)
        c = x**n + randint(-10, 10)
        file.write('>>> afgeleide(' + str(x) + ', ' + str(n) + ', ' + str(c) + ')')
        file.write('\n')

        file.write(str(afgeleide(x, n, c)))
        file.write('\n')
        #file.write('\n')

for i in range(25):   
    with open('1.in', 'a') as file:
        x = randint(-100, 100)/10
        n = randint(2, 5)
        c = round(x**n + randint(-100, 100)/10, 1)
        file.write('>>> afgeleide(' + str(x) + ', ' + str(n) + ', ' + str(c) + ')')
        file.write('\n')

        file.write(str(afgeleide(x, n, c)))
        file.write('\n')
        #file.write('\n')



for i in range(25):   
    with open('2.in', 'a') as file:
        while True:
            x = randint(-10, 10)
            if x != 0:
                break
        n = randint(2, 5)
        c = round(x**n + randint(-10, 10), 1)
        file.write('>>> nulpunt_raaklijn(' + str(x) + ', ' + str(n) + ', ' + str(c) + ')')
        file.write('\n')

        file.write(str(nulpunt_raaklijn(x, n, c)))
        file.write('\n')
        #file.write('\n')

for i in range(25):   
    with open('2.in', 'a') as file:
        while True:
            x = round(randint(-100, 100)/10, 1)
            if x != 0:
                break
        n = randint(2, 5)
        c = round(x**n + randint(-100, 100)/10, 1)
        file.write('>>> nulpunt_raaklijn(' + str(x) + ', ' + str(n) + ', ' + str(c) + ')')
        file.write('\n')

        file.write(str(nulpunt_raaklijn(x, n, c)))
        file.write('\n')
        #file.write('\n')



for i in range(25):
    with open('3.in', 'a') as file:
        n = randint(2, 5)
        c = randint(10, 1000)
        exponent = randint(-12, -6)
        while True:
            x_0 = round(c**(1/n) + randint(-5, 5))
            if x_0 > 0:
                break
        e = 10**exponent
        file.write('>>> n_de_machtswortel_Newton(' + str(n) + ', ' + str(c) + ', '+ str(x_0) + ', ' + str(e) + ')')
        file.write('\n')
        
        file.write(str(n_de_machtswortel_Newton(n, c, x_0, e)))
        file.write('\n')
        #file.write('\n')
   
for i in range(25):
    with open('3.in', 'a') as file:
        n = randint(2, 10)
        c = randint(200, 30000)/100
        exponent = randint(-12, -6)
        while True:
            x_0 = round(c**(1/n) + randint(-5, 5))
            if x_0 > 0:
                break
        e = 10**exponent
        file.write('>>> n_de_machtswortel_Newton(' + str(n) + ', ' + str(c) + ', '+ str(x_0) + ', ' + str(e) + ')')
        file.write('\n')
        
        file.write(str(n_de_machtswortel_Newton(n, c, x_0, e)))
        file.write('\n')
        #file.write('\n') 
