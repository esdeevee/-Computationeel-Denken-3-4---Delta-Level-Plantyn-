def som_Pascal(n):
    som = 0
    for k in range(n+1):
        som = som + Pascal_recursief(n, k)
    return som
