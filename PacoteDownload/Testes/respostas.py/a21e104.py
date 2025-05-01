def valido(msm):
    c = 1
    while c == 1:
        n = str(input(msm))
        if n.isnumeric():
            n = int(n)
            c += 1
        else:
            print('por favor digite um texto valido')
    return(n)
n = valido('digite um numero: ')
print(f'{n} e um numero')