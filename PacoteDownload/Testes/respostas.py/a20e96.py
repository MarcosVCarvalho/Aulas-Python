def area(a, b):
    t = a * b
    print(f'com as dimenções {a}m x {b}m a area e {t:.2f}M2')
print('calculador de area')
n1 = float(input('diga a altura(m): '))
n2 = float(input('diga a largura(m): '))
area(n1, n2)