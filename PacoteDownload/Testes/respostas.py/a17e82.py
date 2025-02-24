lis = []
lisi = []
lisp = []
while True:
    n = int(input('digite um numero: '))
    lis.append(n)
    if n % 2 == 0:
        lisp.append(n)
    else:
        lisi.append(n)
    v = str(input('deseja continuar[S/N] ')).upper()
    if v == 'N':
        break
print(f'essa e a lista completa {lis}')
print(f'essa e com numeros pares {lisp}')
print(f'essa e com numeros impares {lisi}')