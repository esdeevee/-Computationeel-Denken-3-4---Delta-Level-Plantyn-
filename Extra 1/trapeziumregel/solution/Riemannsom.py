def Riemannsom(a, b, n, type):
    som = 0
    Dx = Delta_x(a, b, n)
    for i in range(n):
        x = x_i(a + i*Dx, a + (i+1)* Dx, type)
        #print(x, f(x))
        som = som + f(x) * Dx
    return som
