s = 0
mt = 0
n = 0
while n != 999:
    s += n
    n = int(input('digite um numero[999 para parar]: '))
    if n > mt and n != 999:
        mt = n
print('a soma deu {} e o maior foi {}'.format(s,mt))

