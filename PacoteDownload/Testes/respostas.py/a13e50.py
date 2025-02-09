tp = 0
ti = 0
for c in range(0,6):
    n = int(input('diga um numero: '))
    if n % 2 == 0:
        tp += n
    else:
        ti += n
print('a soma dos pares foi {} e dos impares {}'.format(tp,ti))