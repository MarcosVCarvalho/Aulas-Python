m = 0
n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
while m != 5:
    print('''oque deseja fazer
          [1] somar
          [2] subitrair
          [3] multilicar
          [4]novos numeros
          [5] sair''')
    m = int(input('digite sua opção: '))
    if m == 1:
        print('o resultado deu {}'.format(n1+n2))
    elif m == 2:
        print('o resultado foi {}'.format(n1-n2))
    elif m == 3:
        print('o resultado foi {}'.format(n1*n2))
    elif m == 4:
        n1 = int(input('diga o valor: '))
        n2 = int(input('diga o segundo valor: '))
    else:
        print('opção invalida')
        print('''oque deseja fazer
          [1] somar
          [2] subitrair
          [3] multilicar
          [4]novos numeros
          [5] sair''')
        m = int(input('oq deseja fazer: '))

