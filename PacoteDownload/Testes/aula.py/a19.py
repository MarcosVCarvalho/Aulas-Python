pessoas = []
dados = {'nome':'mv','idade':25,'sexo':'M'}
dados2 = {'nome':'carol','idade':21,'sexo':'F'}
pessoas.append(dados)
pessoas.append(dados2)

dados['nome'] = 'Marcos'
dados['peso'] = 69
for k,n in dados.items():
    print(f'{k:<6} => {n}')
print(f'O {dados["nome"]} tem {dados["idade"]} anos')
print('')
print(pessoas[1]['nome']) 
print(' ')

filmes = {}
lis = []
for c in range(0,2):
    filmes['nome'] = str(input('nome: '))
    filmes['nota'] = float(input('nota: '))
    lis.append(filmes.copy())
for e in lis:
    for f, n in e.items():
        print(f'o filme {f} tem nota {n}')