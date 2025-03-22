from random import randint
l = []
def par(lis):
    c = 0
    print(f'os numeros pares são:',end='')
    while c < len(lis):
        if lis[c] % 2 == 0 and lis[c] != 0:
            print(f' {lis[c]}',end='')
        c += 1
n = int(input('quantos numeros deseja sortear: '))
for c in range(n):
    l.append(randint(0,9))
print(f'os numeros sorteados foram {l}')
par(l)



