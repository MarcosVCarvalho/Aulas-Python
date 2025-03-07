pessoa = []
dado = []
tot = 0
while True:
    dado.append(str(input('nome: ')))
    dado.append(int(input('peso: ')))
    pessoa.append(dado[:])
    dado.clear()
    tot += 1
    v = str(input('deseja continuar[S/N]: ')).upper()
    if v == "N":
        break
print('='*30)
print(f'foram inscritas {tot} pessoas')
print('='*30)
print('pessoas acima do peso')
for p in pessoa:
    if p[1] >= 70:
        print(f'{p[0]} com {p[1]} quilos')
print('='*30)
print('pessoas abaixo do peso')
for p in pessoa:
    if p[1] < 70:
        print(f'{p[0]} com {p[1]} quilos')
print('='*30)