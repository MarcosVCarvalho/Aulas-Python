a=float(input('qual a altura da parede: '))
l=float(input('qual a largura da parede'))
ap = a * l
tt = ap / 2

print('sua parede tem {} metros quadrados e precisamos de {:.2f} galoes de tintas'.format(ap,tt))

p=float(input('qual o valor do seu salario: '))
fp = p + (p/100*15)
print('vc recebeu 15% de aumento, seu salario tem o valor de {:.2f}'.format(fp))

d = int(input('quantos dias ficou com o veiculo: '))
k = int(input('quantos km foram rodados: '))
cd = d * 60
ck = k * 0.15
print('o custo do aluguel ficou em {:.2f} reais'.format(cd+ck ))