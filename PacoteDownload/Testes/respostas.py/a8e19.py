import random
a1 = input('diga o nome do aluno: ')
a2 = input('diga o nome do aluno: ')
a3 = input('diga o nome do aluno: ')
a4 = input('diga o nome do aluno: ')
lista = [a1,a2,a3,a4]
e = random.shuffle(lista) #random,choise e pra escolher so 1
print('a ordem foi {}'.format(lista))
