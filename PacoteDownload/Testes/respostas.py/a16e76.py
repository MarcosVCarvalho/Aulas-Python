lista = ('lapis', 1.72,
         'borraça', 0.50,
         'caderno', 30,
         'mochila',200,)
print('='*40)
print(f'{"lista de preços":.^40}')
print('='*40) 
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$:{lista[pos]:>7.2f}')
print('='*40)