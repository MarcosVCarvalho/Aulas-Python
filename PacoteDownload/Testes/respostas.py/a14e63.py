t = int(input('quantos termos deseja ver: '))
c = 0
s1 = 0
s2 = 1
s3 = 0
s4 = 0
while c != t:
    print('{} , {} , '.format(s1,s2),end='')
    s3 = s1 + s2
    s4 = s2 + s3
    s1 = s3
    s2 = s4
    c += 2
print('fim')
