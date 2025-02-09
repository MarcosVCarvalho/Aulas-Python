n1 = float(input('diga sua primeira nota: '))
n2 = float(input('diga sua segunda nota: '))
m = (n1 + n2) / 2
if m >= 7 :
    print('parabens esta aprovado com media {:.2f}'.format(m))
elif m>= 6 and m<=6.9 :
    print('sua media e {:.2f} e vc esta de recuperação'.format(m))
else:
    print('sua media e {:.2f} e vc esta reprovado'.format(m))
