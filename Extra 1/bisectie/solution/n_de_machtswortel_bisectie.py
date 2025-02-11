def f(x, n, c):
    return x**n - c

def midden(a, b):
    return (a + b)/2

#def n_de_machtswortel_bisectie(wortelexponent, getal, ondergrens, bovengrens, tolerantie):
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
    return m, aantal_iteraties

print(n_de_machtswortel_bisectie(17, 82, -178, 123, 10**-13))

    
