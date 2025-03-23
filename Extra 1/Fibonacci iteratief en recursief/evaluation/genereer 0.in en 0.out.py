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

def fibonacci_recursief(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_recursief(n-1) + fibonacci_recursief(n-2)



# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()



for i in range(1, 26):   
    with open('0.in', 'a') as file:
        file.write('>>> fibonacci_iteratief(' + str(i) + ')')
        file.write('\n')

        file.write(str(fibonacci_iteratief(i)))
        file.write('\n')
        #file.write('\n')

for i in range(1, 26):   
    with open('0.in', 'a') as file:
        file.write('>>> fibonacci_recursief(' + str(i) + ')')
        file.write('\n')

        file.write(str(fibonacci_recursief(i)))
        file.write('\n')
        #file.write('\n')
