def Pascal(n, k):
    if n == k or k == 0:
        return 1
    else:
        return Pascal(n-1, k-1) + Pascal(n-1, k)
