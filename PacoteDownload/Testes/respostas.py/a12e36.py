c = int(input('ola contribuinte,qual o valor da casa :'))
a = int(input('em quantos anos deseja pagar: '))
s = int(input('qual o seu salario: '))
p = c / (a * 12)
if p > (s * 0.3 ):
    print('a valor das parcelas seria de {:.2f} por isso vamos negar'.format(p))
else:
    print('o valor das parcelas seriam de {:.2f} por isso vamos aprovar'.format(p))