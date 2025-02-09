import random
n = random.randint(1,5)
t = int(input('eu escolhi um numero de 1 a 5,consegue adivinhar qual: '))
if ( n == t): 
    print('parabens vc acertou')
else:
    print('errou corno')
print('o numero que eu escolhi era {}'.format(n))
