dados = {}
v = 0
dados['nome'] = str(input('nome: '))
v = int(input('data de nascimento: '))
dados['idade'] = 2025 - v
dados['carteira'] = int(input('carteira de trabalho[0 caso não tenha]: '))
if dados['carteira'] != 0:
    dados['ano'] = int(input('ano de contratação: '))
    dados['salario'] = float(input('salario: '))
    dados['anoap'] = (dados['idade'] + ((dados['ano'] + 35) - 2025))
print('='*30)
print(f'- nome:{dados["nome"]}')
print(f'- idade:{dados["idade"]}')
if dados['carteira'] != 0:
    print(f'- carteira de trabalho:{dados["carteira"]}')
    print(f'- salario:R${dados["salario"]:.2f}')
    print(f'- vai se aposentar com:{dados["anoap"]} anos')

    

