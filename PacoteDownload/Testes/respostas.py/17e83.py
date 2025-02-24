print('verificador de expreção')
e = (str(input('digite sua expreção: ')))
cd = e.count('(')
ce = e.count(')')
if cd == ce:
    print('expreção valida')
else:
    print('expreção invalida')
