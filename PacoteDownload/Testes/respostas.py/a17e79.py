lis = []
v = 0
while True:
    n = (int(input('digite um valor: ')))
    if n not in lis:
        lis.append(n)
    else:
        print('numero repitido')
    v = str(input('deseja continuar[S/N]')).upper()
    if v in 'Nn':
        break
lis.sort
print(f'a lista digita foi: {lis}')