no = input('diga seu nome: ')
a = int(input('qual ano vc nasceu: '))
from datetime import date
ano = date.today().year
i = ano - a
if i <= 9 :
    print('sua idade e {} e competi em Junior'.format(i))
elif i > 9 and i <= 14 :
    print('sua idade e {} e competi em Infantil'.format(i))
elif i > 14 and i <= 19 :
    print('sua idade e {} vc competi em Adolescente'.format(i))
elif i == 20 :
    print('sua idade e {} e competi em A'.format(i))
else:
    print('sua idade e {} e competi em MAster'.format(i))
    