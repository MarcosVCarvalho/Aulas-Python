mp = 0
np = 999999
for c in range(0,5):
    p =  float(input('digite seu peso: '))
    if p > mp :
        mp = p
    elif p < np :
        np = p
print('o maior peso foi de {:.2f}'.format(mp))
print('o menor peso foi de {:.2f}'.format(np))
