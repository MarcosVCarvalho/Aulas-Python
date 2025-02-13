n = s = tv = 0
from random import randint
while True:
    n = int(input('''vamos jogar par ou impar
diga seu numero: '''))
    v = str(input('vc deseja par ou impar[P/I]: ')).strip().upper()
    c = randint(1,10)
    s = n+c 

    ver = 'p' if s % 2 == 0 else 'i'

    if (v == 'P' and ver == 'p') or (v == 'I' and ver == 'i') :
        print(f'vc escolheu {n} o pc {c} deu {n+c} vc venceu')
        tv += 1
    else:
        print(f'vc escolheu {n} o pc {c} deu {n+c} vc perdeu')
        break
print(f'vc ganhou {tv} vezes')
    
    

