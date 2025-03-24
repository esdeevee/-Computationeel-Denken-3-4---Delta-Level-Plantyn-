def x_i(a, b, type):
    if type == 'LINKS':
        return a
    elif type == 'MIDDEN':
        return (a+b)/2
    elif type == 'RECHTS':
        return b
