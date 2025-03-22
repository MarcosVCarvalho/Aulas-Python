from time import sleep
def cont(a, b, c):
    if a < b:
        v = a
        while v <= b:
            print(v)
            v += c
            sleep(0.3)
        print('fim')
    else:
        v = a
        while v >= b:
            print(v)
            v -= c 
            sleep(0.3)
        print('fim')

print('vamos fazer um contador')
i = int(input('diga o inicio: '))
f = int(input('diga o fim: '))
p = int(input('diga o passo: '))
cont(i, f, p)