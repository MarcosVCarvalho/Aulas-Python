def tit(tex):
    print('='*30)
    print(tex)
    print('='*30)
tit('Sejam Bem Vindos')

def soma(*valor):
    s = 0
    for v in valor:
        s += v
    print(f'a soma de {valor} e {s}')
soma(3, 6, 3 , 5)


def dobra(lis):
    c = 0
    lc = lis[:]
    while c < len(lis):
        lis[c] *= 2
        c += 1
    print(f'o dobro de {lc} e {lis}')

l = []
while True:
    l.append(int(input('diga o valor: ')))
    v = str(input('deseja adicionar mais um numero:[S/N] ')).upper()
    if v == 'N':
        break

dobra(l)