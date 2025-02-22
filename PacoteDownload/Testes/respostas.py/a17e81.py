lis = []
c = 0
while True:
    lis.append(int(input('diite um numero: ')))
    c += 1
    v = str(input('dejesa continuar[S/N]')).upper()
    if v == 'N':
        break
lis.sort(reverse=True)
print(f'{lis}')
print(f'foram digitados {c} valores')
if lis.count(5) == 0:
    print('Nao foi digitado no numero 5')
else:
    print(f'foi digitado o 5,{lis.count(5)} vezes')
