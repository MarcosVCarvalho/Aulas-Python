def fatorial(v=1,s=True):
    f = 2
    if s == True:
        while v > 1:
            if v % f == 0:
             print(f"{v:>5} | {f}")
             v //= f
            else:
                f += 1
        print(f'{"1":>5} |')
    else:
        while v > 1:
            if v % f == 0:
                v //= f
            else:
                f += 1
        print(v)
v = int(input('qual numero inteiro deseja fatorar: '))
c = input('deseja mostar a fatoração:[S/N]').upper()
s = c == 'S'

fatorial(v,s)
