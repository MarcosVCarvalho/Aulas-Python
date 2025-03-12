alu = []
while True:
    nome = (str(input('nome: ')))
    n1 = (float(input('nota1: ')))
    n2 = (float(input('nota2: ')))
    med = (n1 + n2) / 2
    alu.append([nome, [n1,n2], med])
    r = str(input('deseja continuar:[S/N] ')).upper()
    if r == 'N':
        break
print('='*30)
print(f'{'n':<4}{'nome':<10}{'media':>8}')
print('='*30)
for i, c in enumerate(alu):
    print(f'{i:<4}{c[0]:<10}{c[2]:>8.1f}')
k = str(input('deseja ver nota de algum aluno[S/N]: ')).upper()
if k == 'S':
    a =  int(input('qual aluno deseja ver a nota: '))
    print(f'{alu[a][1]}')
else:
    print('fim')

