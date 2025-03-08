nume = []
par = []
impar = []
for c in range(1,8):
    n =  int(input(f'digite o {c} valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
nume.append(par[:])
nume.append(impar[:])
print('='*30)
print(f'os valores pares:{nume[0]}')
print(f'os valores impares:{nume[1]}')
