import a23e115arquivo
arq = 'mv.txt'
def mostrarmenu():
    print('='*50)
    print('Menu de Cadastro'.center(50))
    print('='*50)
    print('1:Ler Arquivo')
    print('2:Cadastrar nova pessoa')
    print('3:Sair do Menu')
    print('='*50)
def opcao():
    try:
        t = int(input('Digite sua opção: '))
        return t
    except:
        print('Erro! Digite uma opção valida'.center(50))
        return None
def menu(numero):
    if numero == 1:
        print('='*50)
        a23e115arquivo.lerarquivo(arq)
        print('='*50)
        return 0
    elif numero == 2:
        print('='*50)
        nome = str(input('Diga o nome: '))
        idade = int(input('Diga a idade: '))
        a23e115arquivo.cadastrar(arq, nome, idade)
        print('Novo cadastro realizado'.center(50))
        print('='*50)
        return 0

    elif numero == 3:
        print('='*50)
        print('Saindo! Volte Sempre'.center(50))
        print('='*50)
        return(3)
    else:
        return None

