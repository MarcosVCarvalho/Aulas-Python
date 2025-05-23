import moeda109
valor = float(input('digite um valor: '))
print(f'o dobro de {moeda109.real(valor)} = {moeda109.dobro(valor, True)}')
print(f'a metade de {moeda109.real(valor)} = {moeda109.metade(valor, True)}')
print(f'10% a mais de {moeda109.real(valor)} = {moeda109.dez_porcento(valor, True)}')
print(f'13% a menos de {moeda109.real(valor)} = {moeda109.menos_13(valor, True)}')