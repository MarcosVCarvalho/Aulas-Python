joga = {}
ng = []
atle = []
tot = 0
while True:
    joga.clear()
    ng.clear()
    joga['nome'] = str(input('digite o nome do jogador: '))
    tot = int(input('quantas partidas ele jogou: '))
    for c in range(0,tot):
        ng.append(int(input(f'quantos gols ele fez na {c} partida: ')))
    joga['gol'] = ng[:]
    joga['total'] = sum(ng)
    atle.append(joga.copy())

    c = str(input('deseja cadastrar mais alguem[S/N]: ')).upper()
    if c == 'N':
        break
print('='*50)
for k, v in enumerate(atle):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<10}', end='')
    print()
print('='*50)
while True:
    b = int(input('diga o jogador que deseja ver:(999 para parar) '))
    if b == 999:
        break
    if b > len(atle):
        print('ERRO, não existe esse jogador')
    else:
        print(f'levantamento do jogador {atle[b]['nome']}')
        for i, g in enumerate(atle[b]['gol']):
            print(f'no jogo {i} ele marcou {g}')
    print('='*50)
print('finalizado')