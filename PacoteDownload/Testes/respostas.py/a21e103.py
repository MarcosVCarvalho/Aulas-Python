def ficha(n,g):
    print(f'o jogador {n} fez {g} gols')
n = str(input('nome do jogador: ')).strip()
g = str(input('numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    n = 'desconhecido'
ficha(n,g)


