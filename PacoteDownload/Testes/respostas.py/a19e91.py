from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),'jogador2': randint(1,6),'jogador3': randint(1,6),'jogador4': randint(1,6)}
rank = []
for j, k in jogo.items():
    print(f'o {j} tirou {k} no dado')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for c,i in enumerate(rank):
    print(f'{c} ficou {i[0]} tirando {i[1]}')