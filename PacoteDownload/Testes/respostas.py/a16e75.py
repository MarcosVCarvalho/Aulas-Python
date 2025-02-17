n = (int(input('digite um numero: ')),int(input('digite um numero: ')),int(input('digite um numero: ')),int(input('digite um numero: ')),int(input('digite um numero: ')))
print(f'vc digitou {n}')
print(f'o 9 apareceu {n.count(9)}')
if 3 in n:
    print(f'o 3 apareceu em {n.index(3)+1} posição')
else:
    print('nao apareceu o 3')

print('os valores pares foram ' ,end='')
for c in n:
    if c %2 == 0:
        print(f'{n}',end='')


