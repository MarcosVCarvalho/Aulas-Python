joga = {}
ng = []
gt = 0
joga['nome'] = str(input('digite o nome do jogador: '))
np = int(input('quantas partidas ele jogou: '))
for c in range(0,np):
    g = int(input(f'quantos gols ele fez na {c} partida: '))
    gt+= g
    ng.append(g)
joga['gol'] = ng
joga['total'] = gt
print('='*30)
print(joga)
print('='*30)
for k, i in joga.items():
    print(f'o campo {k} tem valor {i}')
print('='*30)
print(f'o jogador {joga["nome"]} jogou {np} partidas')
for c,g in enumerate(joga['gol']):
    print(f'na partida {c} ele fez {g} gols')
print(f'no total {joga["total"]}')