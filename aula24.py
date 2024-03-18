# Operadores 'in' e 'not in'
# Strings são iteráveis
# 0 1 2 3 4
# F a b i o
#-5-4-3-2-1 

nome = 'Fabio'

print(nome[0])

print('bio' in nome)
print('af' in nome)

print('bio' not in nome)
print('af' not in nome)

nome_jogo = input('Digite seu nome: ')

encontrar = input('Digite a letra que quer  encontrar: ')

if encontrar in nome_jogo:
    index_nome = nome_jogo.index(encontrar)
    print(f'a letra que você procurou é: {encontrar} e seu index é: {index_nome}')