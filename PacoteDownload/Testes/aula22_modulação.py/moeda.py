def dobro(n = 0):
    n *= 2
    return(n)

def metade(n = 0):
    n /= 2
    return(n)

def dez_porcento(n = 0):
    n *= 1.1
    return(n)

def menos_13(n = 0):
    v = (n /100) * 13
    n -= v
    return(n)

def real(n = 0, moeda =  'R$'):
    return f'{moeda}{n:>.2f}'.replace('.',',')
