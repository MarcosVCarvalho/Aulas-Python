lis = []
for c in range (0,5):
    n = int(input('digite um numero: '))
    if c == 0 or n > lis[-1]:
        lis.append(n)
        print(f'{n} adicionado no fim da lista')
    else:
        pos = 0
        while pos < len(lis):
            if n <= lis[pos]:
                lis.insert(pos, n)
                print(f'{n} adicionado na posição {pos}')
                break
            pos += 1
print('='*30)
print(f'sua lista e {lis}')
        
