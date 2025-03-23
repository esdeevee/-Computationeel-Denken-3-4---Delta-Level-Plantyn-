def fibonacci_recursief(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_recursief(n-1) + fibonacci_recursief(n-2)
