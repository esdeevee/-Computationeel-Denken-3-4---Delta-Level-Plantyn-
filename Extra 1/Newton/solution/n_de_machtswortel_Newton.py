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
