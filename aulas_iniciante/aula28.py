# Exercicio
# Peça ao usuario para digitar seu nome
# Peça ao usuario para digitar sua idade

# Se nome  e idade forem digitados:
#     Exiba:
#         Seu nome é: {nome}
#         Seu nome invertido é: {nome_invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é: {primeira_letra}
#         A última letra do seu nome é: {ultima_letra}

# Se nada for digitado em nome ou idade:
#     Exiba 'Desculpe, você deixou campos vazios'

nome = input('Digite seu nome ')
idade = input('Digite sua idade ')

if nome and idade:
    print(f'Seu nome é: {nome}')

    nome_invertido = nome[::-1]
    print(f'Seu nome invertido é: {nome_invertido}')

    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome NÃO tem espaços')

    letras = len(nome) - nome.count(" ")
    print(f'Seu nome tem {letras} letras')

    primeira_letra = nome[0]
    print(f'A primeira letra do seu nome é: {primeira_letra}')
    ultima_letra = nome[len(nome) - 1]
    print(f'A ultima letra do seu nome é: {ultima_letra}')

else:
    print(f'Desculpe, você deixou campos vazios!')

