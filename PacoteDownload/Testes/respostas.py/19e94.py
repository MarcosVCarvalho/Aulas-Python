dado = {}
galera = []
tp = idades = medidade = 0
mulheres = []
acima = []
while True:
    tp += 1
    dado.clear()
    dado['nome'] = str(input('nome: '))

    while True:
        dado['sexo'] = str(input('sexo[M/F] ')).upper()
        if dado['sexo'] in 'MF':
            break
        else:
            print('ERRO - Por favor digite apenas [M/F]')
    if dado['sexo'] == 'F':
        mulheres.append(dado['nome'])
    dado['idade'] = int(input('idade: '))
    idades += dado['idade']
    medidade = idades / tp
    if dado['idade'] > medidade:
        acima.append(dado['nome'])
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
print(f'ao todo foram cadastradas {tp} pessoas')
print(f'a media de idades foi de {medidade} anos')
print(f'as mulheres são:{mulheres}')
print(f'as pessoas acima da media são:{acima}')