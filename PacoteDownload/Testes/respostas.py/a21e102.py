def fatorial(n=1,s=False):
    r  = 1
    m = '.'
    if s == True:
        for c in range(n,0,-1):
            r *= c
            m = print(f'{c}',end='')
    else:
        for c in range(n,0,-1):
            r *= c
    return r , m
a = int(input('digite um numero: '))
s = True
