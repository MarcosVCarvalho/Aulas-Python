c = 0
while c == 0:
    try: 
        n = int(input('Digite um número inteiro: '))
        n2 = float(input('Digite um número Real: '))
        c += 1
    except (ValueError, TabError):
        print('='*60)
        print(f'Erro! Por Favor digite um número valido'.center(60))
        print('='*60)
    except:
        print('='*60)
        print(f'Erro! Por Favor digite um número valido'.center(60))
        print('='*60)
print('='*60)
print('Fim do Progama - Volte sempre'.center(60))
print('='*60)