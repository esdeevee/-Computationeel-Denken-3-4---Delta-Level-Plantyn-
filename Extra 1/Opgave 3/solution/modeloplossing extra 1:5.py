def P(v,d):
    P = min(v*d/40, 1)
    return P
def bepaal_kleur(P_v, P_a):
    if min(P_v, P_a) > 0.7:
        return 'zwart'
    elif max(P_v, P_a) > 0.7 and abs(P_v - P_a) < 0.2:
        return 'rood'
    elif abs(P_v - P_a) > 0.7:
        return 'geel'
    else:
        return 'groen'
v_v = float(input('Geef de snelheid van het vrachtverkeer'))
d_v = float(input('Geef de verkeersdichtheid van het vrachtverkeer'))
v_a = float(input('Geef de snelheid van het autoverkeer'))
d_a = float(input('Geef de verkeersdichtheid van het autoverkeer'))
P_v = P(v_v, d_v)
P_a = P(v_a, d_a)
print(bepaal_kleur(P_v, P_a))
