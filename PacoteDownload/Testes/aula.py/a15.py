n = s = 0
while True:
 s += n
 n = int(input('digite um numero: '))
 if n == 999:
    break
print(f'a soma deu: {s-2}')

