def fibonacci_iteratief(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
