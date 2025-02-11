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
    return s, aantal_iteraties

print(n_de_machtswortel_Newton(17, 82, 1, 10**-12))
