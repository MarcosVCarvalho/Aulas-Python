import math
n = float(input('digite um numero: '))
a = math.trunc(n)
print('vc digitou {} e ele inteiro e {}'.format(n,a))

co = int(input('qual a valor do cateto 1: '))
ca = int(input('qual a valor do cateto 2: '))
h = math.pow(co, 2) + math.pow(ca, 2) #elevaar ao quadrado
r = math.sqrt(h)                      #a soma
print('a hipotenusa e {}'.format(r))


