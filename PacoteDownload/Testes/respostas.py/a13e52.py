n = int(input('digite um numero e descubra se e primo: '))
t = 0
for c in range(1,n+1):
    if n % c == 0 :
        t += 1
if t > 2 :
    print('{} não e primo ele e divisivel {} vezes'.format(n,t))
else:
    print('{} e primo ele e divisivel {} vezes'.format(n,t))