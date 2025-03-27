def Pascal_recursief(n, k):
    if n == k or k == 0:
        return 1
    else:
        return Pascal_recursief(n-1, k-1) + Pascal_recursief(n-1, k)
