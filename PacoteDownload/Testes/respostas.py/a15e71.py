print('='*20)
print('{:^20}'.format('banco do mv'))
print('='*20)
v = int(input('diite o valor que deseja sacar: '))
total = v
nc = 0
while total >= 50:
        total -= 50
        nc += 1
if nc != 0:
 print(f'cedulas de 50: {nc}')
nc = 0
while total >= 20:
      total -= 20
      nc += 1
if nc != 0:
 print(f'cedulas de 20: {nc}')
while total >= 10:
       total -= 10
       nc += 1
if nc != 0:
 print(f'cedulas de 10: {nc}')
nc = 0
while total >= 1:
      total -= 1
      nc += 1
if nc != 0:
 print(f'moedas de 1: {nc}') 