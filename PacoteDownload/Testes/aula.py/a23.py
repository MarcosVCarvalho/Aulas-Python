try:
    dividendo = int(input('digite um numero: '))   
    divisor = int(input('digite um numero: '))   
    resultado = dividendo / divisor
except:
    print('='*30)
    print('tivemos um problema'.center(30))
    print('='*30)
else:
    print(f'{dividendo} / {divisor} = {resultado:.2f}')
finally:
    print('FIM! Volte sempre')