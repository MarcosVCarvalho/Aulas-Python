import moeda
valor = float(input('digite um valor: '))
print(f'o dobro de {valor} = {moeda.dobro(valor):2f}')
print(f'a metade de {valor} = {moeda.metade(valor):2f}')
print(f'10% a mais de {valor} = {moeda.dez_porcento(valor):2f}')
print(f'13% a menos de {valor} = {moeda.menos_13(valor):2f}')