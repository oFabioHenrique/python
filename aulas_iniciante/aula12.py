nome = input(f'insira seu nome: ')
nome_title = nome.title() # deixa a primeira letra da cada palvra em maiúsculo
altura = float(input(f'insira sua altura em metros: ')) 
peso = float(input('insira seu peso em Kgs: '))

imc = peso / (altura * altura)

print(f'Meu nome é {nome_title}, tenho altura de {altura}M, meu peso é {peso}Kg e meu IMC é: {imc}')
