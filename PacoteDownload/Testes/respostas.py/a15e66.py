n = s = t = 0
while True:
 s += n
 n = int(input('''digite um numero 
digite [999] para parar: '''))
 if n == 999:
    break
 t += 1
print(f'a soma deu: {s} e vc digitou {t} numeros')