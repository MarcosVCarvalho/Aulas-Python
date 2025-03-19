dado = {}
galera = []

while True:
    dado.clear()  # Corrigido para chamar o método clear()
    dado['nome'] = str(input('Nome: '))
    
    while True:
        dado['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if dado['sexo'] in 'MF':
            break
        else:
            print('ERRO - Por favor, digite apenas [M/F]')
    
    dado['idade'] = int(input('Idade: '))
    galera.append(dado.copy())  # Adiciona uma cópia do dicionário à lista
    
    while True:
        c = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).upper()
        if c in 'SN':
            break
        else:
            print('ERRO - Por favor, digite apenas [S/N]')
    
    if c == 'N':
        break  # Sai do loop se o usuário não quiser cadastrar mais
    
    print('=' * 30)

# Exibe a lista de pessoas cadastradas
print('Cadastro finalizado.')
print(galera)