c = int(input('qual o valor da compra: '))
print('''qual a forma de pagamento:
[1] a vista em dinheiro
[2] a vista no cheque
[3] fiado
[4] parcelado em 3 ou mais vezes''')
menu = int(input('digite a opção: '))
if menu == 1:
    print('{} ficou {:.2f} a vista'.format(c, (c * 0.9)))
elif menu == 2:
    print('{} ficou {:.2f} no cheque'.format(c,(c * 1.1)))
elif menu == 3:
    print('{} ficou {:.2f} fiado'.format(c,(c * 1.4)))
elif menu == 4:
    v = int(input('em quantas vezes deseja parcelar: '))
    p = (c * (1.2)) / v
    print('{} ficou {:.2f} parcelado em {} vezes'.format(c,p,v))
else:
    print('opção invalida')
    



          