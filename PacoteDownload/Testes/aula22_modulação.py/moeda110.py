def resumo(v, taxaa = 0, taxad = 0):
    print('=' * 30)
    print('Tabela de Contas'.center(30))
    print('=' * 30)
    print(f'analisando valor de: {real(v)}')
    print(f'Dobro de: {real(v)} = {dobro(v)}')
    print(f'Metade de: {real(v)} = {metade(v)}')
    print(f'{taxaa}% a mais de: {real(v)} = {aumento(v)}')
    print(f'{taxaa}% a menos de: {real(v)} = {diminuição(v)}')
    print('=' * 30)
    

def dobro(n = 0):
    r = (n * 2)
    return real(r)

def metade(n = 0,):
    r = (n / 2)
    return real(r)

def aumento(n = 0,taxaa = 10):
    r = (n + (n * taxaa / 100))
    return real(r)

def diminuição(n = 0,taxad=10):
    v = (n /100) * taxad
    r = (n - v)
    return real(r)

def real(n = 0, moeda =  'R$'):
    return f'{moeda}{n:>.2f}'.replace('.',',')
