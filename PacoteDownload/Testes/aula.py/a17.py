num = [2,4,3,8,5,28]
num[0] = 3
num.append(7)
num.sort(reverse=True)
num.pop(0)
num.remove(3)
print(f'a lista tem {len(num)} itens')
for v in num:
    print(f'{v}..')


val = list()
for cont in range(0,4):
    val.append(int(input('digite um valor: ')))
for c, v in enumerate(val):
    print(f'na posição {c} esta {v}')

    