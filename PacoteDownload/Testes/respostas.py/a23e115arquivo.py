def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um erro na criação do arquivo')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo')
    else:
        print('Pessoas Cadastradas'.center(50))
        for linha in a:
            if isinstance(linha, str):  # Verifica se linha é uma string
                dado = linha.split(';')
                if len(dado) > 1:  # Verifica se há pelo menos dois elementos
                    dado[1] = dado[1].replace(';', '')
                    print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade ='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nome};{idade};')
    finally:
        a.close()
    