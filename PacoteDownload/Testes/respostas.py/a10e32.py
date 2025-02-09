s1 = float(input('diga o seguimmento 1 '))
s2 = float(input('diga o seguimento 2 '))
s3 = float(input('diga o seguimento 3 '))
if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print('e triangulo')
else:
    print('nao e triangulo')
    