n = int(input('qual numero deseja ver a tabuada: '))
t = int(input('ate qual numero deseja ve-lo sendo multiplicado: '))
for c in range(1,t+1):
    print('{} x {} = {}'.format(n,c,(n*c)))
print('fim da tabuada')