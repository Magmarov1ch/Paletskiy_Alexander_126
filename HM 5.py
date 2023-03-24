def eqv(A, B, C):
    eps = 0.0001 * max(A, B)
    return abs(A + B - C) <= eps

A = 46879.37
B = 3048.14
C = 16879.16

if eqv(A, B, C):
    print("Сумма A и B равна C с учетом точности eps.")
else:
    print("Сумма A и B не равна C с учетом точности eps.")