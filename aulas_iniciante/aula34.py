'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
'''
condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    nome_upper = nome.upper()
    print(f'Seu nome é {nome_upper}')

    if nome_upper == 'SAIR':
        break

print('Acabou')