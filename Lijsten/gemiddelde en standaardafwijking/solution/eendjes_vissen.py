def eendjes_vissen(lijst, aantal):
    maximum = 0
    positie = 0
    for i in range(len(lijst)):
        som = 0
        for j in range(aantal):
            print(lijst[(i+j) % len(lijst)])
            som += lijst[(i + j) % len(lijst)]
        print(i, som)
        print('\n')
        if som > maximum:
            maximum = som
            positie = i
    return (positie, maximum)

"""
print(eendjes_vissen([5, 2, 4, 1, 1, 5, 4, 4, 3, 2], 4))

print(eendjes_vissen([4, 3, 2, 5, 2, 4, 1, 1, 5, 4], 4))
"""
# print(eendjes_vissen([1, 1, 1, 1, 1], 2))

print(eendjes_vissen([4, 1, 6, 1, 7], 2))
