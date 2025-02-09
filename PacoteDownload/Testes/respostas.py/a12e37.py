n = int(input('qual numero deseja converter: '))
print('''diga pra oq quer converter:
[1] binario
[2] hexadessimal
[3] octal''')
menu = int(input())
if menu == 1:
    print('{} convertido para binario e {}'.format(n,bin(n)[2:]))
elif menu == 2:
    print('{} convertido para hexadecimal e {}'.format(n,hex(n)[2:]))
elif menu == 3:
    print('{} convertido para octal e {}'.format(n,oct(n)[2:]))
else:
    print('opção invalida')
