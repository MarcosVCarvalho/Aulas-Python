c = ('\033[m',             #0 sem cor
     '\033[0;30;41m',)       #1 vermelho)

def ajuda(n):
    try:
        help(n)
    except Exception as e:
        print(f"Erro: {e}")

def titulo(msm, cor=0):
    tam = len(msm) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msm}')
    print('~' * tam)
    print(c[cor], end='')

comando = ''
while True:
    titulo('Sistema de Help', 1)
    comando = str(input('biblioteca ou Função >'))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('ate logo')
