try: #tente fazer X
    dividendo = int(input('digite um numero: '))   
    divisor = int(input('digite um numero: '))   
    resultado = dividendo / divisor
except ZeroDivisionError : #caso a tentativa der errado faça Y
    print('='*40)
    print(f'Erro! não é possivel dividir por 0'.center(40))
    print('='*40)
except (ValueError, TypeError) : #caso a tentativa der errado faça Y
    print('='*60)
    print(f'Erro! problema com seu tipo de digitação'.center(60))
    print('='*60)
except KeyboardInterrupt : #caso a tentativa der errado faça Y
    print('='*40)
    print(f'Erro! sem informações de dados'.center(40))
    print('='*40)
else: #se deu certo fazer x , faca Z
    print(f'{dividendo} / {divisor} = {resultado:.2f}')
finally: #no final de tudo faça A
    print('FIM! Volte sempre'.center(60))