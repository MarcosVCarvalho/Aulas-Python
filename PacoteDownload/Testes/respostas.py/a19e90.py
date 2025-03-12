dados = {}

dados['nome'] = str(input('nome do aluno: '))
dados['nota'] = float(input(f'media do {dados["nome"]}: '))
if dados['nota'] <= 5.9:
    dados['situacao'] = 'REPROVADO'
elif dados['nota'] <= 6.9:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'APROVADO'
print(f'o aluno {dados["nome"]} com media {dados["nota"]} estar: {dados["situacao"]}')
