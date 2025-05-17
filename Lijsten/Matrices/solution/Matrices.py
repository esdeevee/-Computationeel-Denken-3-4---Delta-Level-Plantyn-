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
