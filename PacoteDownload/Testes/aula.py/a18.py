dado = []
pessoa = []

dado.append('marcos')
dado.append(19)
pessoa.append(dado[:])
dado[0] = 'carol'
dado[1] =  21
pessoa.append(dado[:])
print(pessoa)
print()
galera = [['miguel',18],['lais',20],['diego',12]]
print(galera[0][0], galera[1])

print()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')