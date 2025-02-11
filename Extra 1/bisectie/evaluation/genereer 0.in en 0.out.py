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

def afgeleide(x, n):
    return n * x**(n-1)

def nulpunt_raaklijn(x, n, c):
    return x - f(x, n, c) / afgeleide(x, n)

def n_de_machtswortel_Newton(n, c, s, e):
    aantal_iteraties = 0
    while True:
        if abs(f(s, n, c)) < e:
            break
        else:
            s = nulpunt_raaklijn(s, n, c)
            aantal_iteraties += 1
    return s#, aantal_iteraties



# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in out.csv
file = open("0.out", "w")
file.truncate()
file.close()


for i in range(50):
    with open('0.in', 'a') as file:
        x = randint(10, 300)/100
        n = randint(2, 20)
        c = randint(10, 1000)/10
        file.write('f(' + str(x) + ', ' + str(n) + ', ' + str(c) + ')')
        file.write('\n')

    with open('0.out', 'a') as file:
        file.write(str(f(x, n, c)))
        file.write('\n')
        #file.write('\n')
        
    with open('0.in', 'a') as file:
        n = randint(2, 20)
        c = randint(200, 3000)/100
        exponent = randint(-12, -6)
        a = c**(1/n) - randint(1, 3)
        b = c**(1/n) + randint(1, 3)
        e = 10**exponent
        file.write('n_de_machtswortel_bisectie(' + str(n) + ', ' + str(c) + ', '+ str(a) + ', ' + str(b) + ', ' + str(e) + ')')
        file.write('\n')
        
    with open('0.out', 'a') as file:
        file.write(str(n_de_machtswortel_bisectie(n, c, a, b, e)))
        file.write('\n')
        #file.write('\n')
    
