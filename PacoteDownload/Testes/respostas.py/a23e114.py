import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('='*40)
    print('Erro! Sem acesso'.center(40))
    print('='*40)
except:
    print('='*40)
    print('Erro! Sem acesso'.center(40))
    print('='*40)
else:
    print('='*40)
    print('Acesso Completo'.center(40))
    print('='*40)
