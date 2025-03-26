def soma(a=0, b=0, c = 0):
    s = a+ b + c
    return s
S1 = soma(4, 6, 5)
S2 = soma(3 , 5, 2)
print(f'os resultados foram {S1},{S2},')

def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'resultados foram:{f1},{f2},{f3}')

