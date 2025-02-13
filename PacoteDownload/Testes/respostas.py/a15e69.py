v  = 'S'
tmi = tm = mi = 0
while True:
    print('cadastro de pessoas')
    i = int(input('diga a idade: '))
    s = str(input('Sexo[M/F]: ')).strip().upper()
    v = str(input('deseja cadastrar mais alguem[S/N]: ')).strip().upper()
    if i > 18:
        mi += 1
    if s == 'M':
        tm += 1
    elif s == 'F' and i < 20:
        tmi += 1
    if v == 'N':
        break
print(f'''o total de pessoas acima de 18 foi {mi}
o total de homens foram {tm}
o total de mulheres abaixo de 20 foi {tmi}''')
