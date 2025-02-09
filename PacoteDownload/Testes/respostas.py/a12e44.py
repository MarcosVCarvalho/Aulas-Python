from random import randint
item = ('pedra' , 'papel' , 'tesoura')
c = randint(0, 2)
print('''vamos jogar um jogo, qual jogada deseja fazer
      [0] Pedra 
      [1] Papel 
      [2] Tesoura''')
j = int(input('digite sua jogada: '))
if c == 0:
    if j == 0:
        print('vc escolheu {} e o computador {} deu empate'.format(item[j],item[c]))
    elif j == 1:
        print('vc escolheu {} e o computador {} vc venceu'.format(item[j],item[c]))
    elif j == 2:
        print('vc escolheu {} e o computador {} vc perdeu'.format(item[j],item[c]))
    else:
        print('opção invalida')
if c == 1:
    if j == 0:
        print('vc escolheu {} e o computador {} vc perdeu'.format(item[j],item[c]))
    elif j == 1:
        print('vc escolheu {} e o computador {} deu empate'.format(item[j],item[c]))
    elif j == 2:
        print('vc escolheu {} e o computador {} vc venceu'.format(item[j],item[c]))
    else:
        print('opção invalida')
if c == 2:
    if j == 0:
        print('vc escolheu {} e o computador {} vc venceu'.format(item[j],item[c]))
    elif j == 1:
        print('vc escolheu {} e o computador {} vc perdeu'.format(item[j],item[c]))
    elif j == 2:
        print('vc escolheu {} e o computador {} deu empate'.format(item[j],item[c]))
    else:
        print('opção invalida')

