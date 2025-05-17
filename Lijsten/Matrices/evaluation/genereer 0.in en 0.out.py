from random import randint, sample

def is_matrix(lijst):
    for rij in lijst:
        if len(rij) != len(lijst[0]):
            return False
    return True

def dimensies(matrix):
    aantal_rijen = len(matrix)
    aantal_kolommen = len(matrix[0])
    return (aantal_rijen, aantal_kolommen)

def product(A, B):
    aantal_kolommen_A = dimensies(A)[1]
    aantal_rijen_B = dimensies(B)[0]
    if aantal_kolommen_A == aantal_rijen_B:
        aantal_rijen_A = dimensies(A)[0]
        aantal_kolommen_B = dimensies(B)[1]
        return (aantal_rijen_A, aantal_kolommen_B)
    else:
        return False

def transpose(A):
    aantal_rijen = len(A)
    aantal_kolommen = len(A[0])
    matrix = []
    for i in range(aantal_kolommen):
        rij = []
        for j in range(aantal_rijen):
            rij.append(A[j][i])
        matrix.append(rij)
    return matrix
        


# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()

for i in range(10):
    for j in range(10):
        aantal_rijen = randint(1, 4+j)
        aantal_kolommen = randint(1, 4+j)
        toss = randint(0, 1)
        matrix = []
        if toss == 1:
            for k in range(aantal_rijen):
                rij = sample(range(-10, 10), aantal_kolommen)
                matrix.append(rij)
        else:
            for k in range(aantal_rijen):
                rij = sample(range(-10, 10), aantal_kolommen + randint(-1, 1))
                matrix.append(rij)
        with open('0.in', 'a') as file:
            file.write('>>> is_matrix(' + str(matrix) + ')')
            file.write('\n')
            file.write(str(is_matrix(matrix)))
            file.write('\n')

# wis alle gegevens in in.csv
file = open("1.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("1.out", "w")
file.truncate()
file.close()

for i in range(10):
    for j in range(10):
        aantal_rijen = randint(1, 4+j)
        aantal_kolommen = randint(1, 4+j)
        matrix = []
        for k in range(aantal_rijen):
            rij = sample(range(-10, 10), aantal_kolommen)
            matrix.append(rij)
        
        with open('1.in', 'a') as file:
            file.write('>>> dimensies(' + str(matrix) + ')')
            file.write('\n')
            file.write(str(dimensies(matrix)))
            file.write('\n')

# wis alle gegevens in in.csv
file = open("2.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("2.out", "w")
file.truncate()
file.close()

for i in range(10):
    for j in range(10):
        aantal_rijen_A= randint(1, 4+j)
        aantal_kolommen_A = randint(1, 4+j)
        A = []
        B = []
        for k in range(aantal_rijen_A):
            rij = sample(range(-10, 10), aantal_kolommen_A)
            A.append(rij)
        toss = randint(0,1)
        if toss == 0:
            aantal_rijen_B = aantal_kolommen_A
            aantal_kolommen_B = randint(1, 4+j)
            for k in range(aantal_rijen_B):
                rij = sample(range(-10, 10), aantal_kolommen_B)
                B.append(rij)
        else:
            aantal_rijen_B= randint(1, 4+j)
            aantal_kolommen_B = randint(1, 4+j)
            for k in range(aantal_rijen_A):
                rij = sample(range(-10, 10), aantal_kolommen_B)
                B.append(rij)
        
        with open('2.in', 'a') as file:
            file.write('>>> product(' + str(A) + ', ' + str(B) + ')')
            file.write('\n')
            file.write(str(product(A, B)))
            file.write('\n')
            
# wis alle gegevens in in.csv
file = open("3.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("3.out", "w")
file.truncate()
file.close()

for i in range(10):
    for j in range(10):
        aantal_rijen_A= randint(1, 4+j)
        aantal_kolommen_A = randint(1, 4+j)
        A = []
        for k in range(aantal_rijen_A):
            rij = sample(range(-10, 10), aantal_kolommen_A)
            A.append(rij)
        
        
        with open('3.in', 'a') as file:
            file.write('>>> transpose(' + str(A) + ')')
            file.write('\n')
            file.write(str(transpose(A)))
            file.write('\n')
