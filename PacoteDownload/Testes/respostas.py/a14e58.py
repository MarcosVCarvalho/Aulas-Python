from random import randint
tt = 1
t = int(input('vamos jogar um game,tente adivinhar em que numero estou pensando de 1 a 10: '))
n =  randint(1,10)
while n != t:
    if t != n:
        tt += 1
    if t > n :
        print('menos')
    elif t < n:
        print('mais')
    t = int(input('vc errou! Tente novamente: '))
print('parabens vc acertou em {} tentativas, meu numero era {}'.format(tt,n))

