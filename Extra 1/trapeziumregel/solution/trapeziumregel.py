def trapeziumregel(a, b, n):
    som = 0
    Dx = Delta_x(a, b, n)
    for i in range(n):
        x1 = x_i(a, i, Dx)
        x2 = x1 + Dx
        som = som + (f(x1) + f(x2))/2 * Dx
    return som
