def dobro(n = 0, format = False):
    r = (n * 2)
    return r if format == False else real(r)

def metade(n = 0, format = False):
    r = (n / 2)
    return r if format == False else real(r)

def dez_porcento(n = 0,taxaa = 10, format = False):
    r = (n * taxaa)
    return r if format == False else real(r)

def menos_13(n = 0,taxad=10, format = False):
    v = (n /100) * taxad
    r = (n - v)
    return r if format == False else real(r)

def real(n = 0, moeda =  'R$'):
    return f'{moeda}{n:>.2f}'.replace('.',',')