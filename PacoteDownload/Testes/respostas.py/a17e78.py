l = []
mn = pn = 0
ppn = []
pmn = []
for c in range(0,4):
    l.append(int(input(f'digite o valor para posição {c} : ')))
    if c == 0:
        mn = pn = l[c]
    else:
        if l[c] > mn:
            mn = l[c]
        if l[c] < pn:
            pn = l[c]

print(f'sua lista foi {l}')
print(f'o maior valor foi {mn} nas posições ',end='')
for p, v in enumerate(l):
    if v == mn:
        print(f'{p} ...',end='')
print()
print(f'o menor valor foi {pn} nas posições ',end='')   
for p, v in enumerate(l):
    if v == mn:
        print(f'{p} ...',end='')