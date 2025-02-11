c = s = n = 0
v = 's'
while v != 'N':
    n =  int(input('digite um numero: '))
    v = str(input('deseja continuar[S/N]')).strip().upper()
    c += 1
    s += n
print('vc digitou {} numeros e a media deles e {:.2f}'.format(c,s/c))