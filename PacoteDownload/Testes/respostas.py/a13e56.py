tm = 0
mi = 0
pmv = 0 
media = 0 
for c in range(0,4):
    nome = str(input('digite o nome: '))
    idade = int(input('digite a idade: '))
    sexo = str(input('diga o sexo[M/F]')).upper()
    media += idade
    if sexo == 'F' and idade <= 20 :
        tm += 1
    if idade > mi:
        mi = idade
        pmv = nome
print('a media de idades foi {:.2f}'.format(media/4))
print('a pessoa mais velha foi {} com {} anos'.format(pmv,mi))
print('ao todo tivemos {} mulheres com menos de 20 anos'.format(tm))
