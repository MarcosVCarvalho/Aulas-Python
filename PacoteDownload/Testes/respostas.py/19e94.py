dado = {}
galera = []
while True:
    dado.clear()
    dado['nome'] = str(input('nome: '))

    while True:
        dado['sexo'] = str(input('sexo[M/F] ')).upper()
        if dado['sexo'] in 'MF':
            break
        else:
            print('ERRO - Por favor digite apenas [M/F]')

    dado['idade'] = int(input('idade: '))
    galera.append(dado.copy())

    while True:
        c = str(input('deseja cadastrar mais uma pessoas[S/N] ')).upper()
        if c in 'SN':
            break
        print('ERRO - Por favor digite apenas [S/N]') 
    if c == 'N':
        break
print('='*30)
print(galera)