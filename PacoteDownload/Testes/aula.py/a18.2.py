galera = []
dado = []
for c in range(0,3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} tem {p[1]} anos,e de maior')
    else:
        print(f'{p[0]} e menor de idade')
