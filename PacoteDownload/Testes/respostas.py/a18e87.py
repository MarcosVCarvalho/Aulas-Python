from random import randint
lis = []
dado = []
c = int(input('quantos numeros deseja sorter: '))
for l in range(0,c):
    for k in range(0,6):
        n = randint(1,60)
        dado.append(n)
    lis.append(dado[:])
    dado.clear()
print('='*30)
for i, l in enumerate(lis):
    print(f'lista {i}: {l}')