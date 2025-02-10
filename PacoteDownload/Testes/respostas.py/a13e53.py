f = str(input('digite sua frase: ')).strip().upper()
pa = f.split()
jun = ''.join(pa)
inverso = ''
for le in range(len(jun)-1 , -1 , -1):
    inverso += jun[le]
if inverso == jun:
    print('a frase e um palindromo')
else:
    print('nao e palindromo')
