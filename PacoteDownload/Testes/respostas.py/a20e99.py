l = []
def mns(lis):
    c = 0
    mn = np = lis[0]
    
    while c < len(lis):
        if mn < lis[c]:
            mn = lis[c]
        if np > lis[c]:
            np = lis[c]
        c += 1
    print(f'foram digitados {len(lis)}')
    print(f'o maior numero digitado foi {mn} e o menos {np}')
while True:
    l.append(int(input('digite numero: ')))
    v = str(input('deseja continuar[S/N]: ')).upper()
    if v == 'N':
        break
mns(l)
    