num = [2,4,3,8,5,28]
num[0] = 3
num.append(7)
num.sort(reverse=True) #sort ordena 
num.pop(0) #pop remove um casa
num.remove(3) #remove um valor
print(f'a lista tem {len(num)} itens')
for v in num:
    print(f'{v}..',end='')
print()

val = []
for cont in range(0,4):
    val.append(int(input('digite um valor: ')))
    
for c, v in enumerate(val): #enumerate pega o valor e a possição
    print(f'na posição {c} esta {v}')

b = val[:]   