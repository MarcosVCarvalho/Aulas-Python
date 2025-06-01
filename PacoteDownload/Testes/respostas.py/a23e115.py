import a23e115teste
import time
import a23e115arquivo

arq = 'mv.txt'
if not a23e115arquivo.arquivoexiste(arq):
    a23e115arquivo.criararquivo(arq)

while True:
    a23e115teste.mostrarmenu()
    op = a23e115teste.opcao()
    resultado = a23e115teste.menu(op)
    time.sleep(1)
    if resultado == 3:
        break