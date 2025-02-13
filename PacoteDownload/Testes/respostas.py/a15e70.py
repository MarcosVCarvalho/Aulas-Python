print('seja bem vindo ao Mercadinho Nana')
t = mv = mp = tv = 0
while True:
    t += 1
    p = str(input('qual o item: '))
    v = int(input('qual o valor da compra: '))
    c = str(input('deseja continuar[S/N]: ')).strip().upper()
    tv += v
    if v > mv:
        mv = v
        mp = p
    if c == 'N':
        break
print(f'''vc comprou {t} itens
o total da conta deu {tv}
o produto mais caro foi {mp} custando {mv}''')