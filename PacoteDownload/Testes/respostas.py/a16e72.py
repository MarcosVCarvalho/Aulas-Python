numero = "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
while True:
 n = int(input('diite um numero de 0 a 20: '))
 if n >20 or n<0:
    print('numero invalido,tente novamente')
 else:
    print(f'seu numero e : {numero[n]}')
    break