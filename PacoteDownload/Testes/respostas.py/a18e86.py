matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tot = col = lin = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f'valor da posição [{l}, {c}] ')))
        tot += matriz[l][c]
        if c == 2:
            col += matriz[l][c]
        if l == 1:
            lin += matriz[l][c]

print('='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
print('='*30)
print(f'o total foi {tot}')
print(f'a soma da 3 coluna foi {col}')
print(f'a soma da 2 linha foi {lin}')