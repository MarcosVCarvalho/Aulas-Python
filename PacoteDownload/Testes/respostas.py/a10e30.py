v = int(input('qual a distancia da viagem: '))
if (v <= 200):
    m = v * 0.50
    print('sua passagem deu {} reais'.format(m))
else:
    m = v * 0.45
    print('sua passagem deu {} reais'.format(m))
