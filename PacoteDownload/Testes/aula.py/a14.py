r = 'S'
t = 0
while r == 'S' :
    n = int(input('digite um numero: '))
    r = input('deseja continuar [S/N]').upper()
    t += n
print('a somas dos numeros foi {}'.format(t))
