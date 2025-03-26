from datetime import date
hj = date.today().year
def voto(a=0):
    i = hj - a 
    if i < 16:
        r = (f'com {i} anos voce não pode votar')
    elif i <= 16 and i < 18:
        r = (f'com {i} anos seu voto e opcional')
    elif i <= 18 and i < 60:
        r = (f'com {i} anos seu voto e obrigatorio')
    else:
        r = (f'com {i} anos seu voto e opcional')
    return r
a =  int(input('diga o ano do seu nascimento: '))
r = voto(a)
print(r)