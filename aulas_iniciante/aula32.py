'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
'''
#inicio função
def par_ou_impar(x, y = 2):
    num_par = x % y
    if num_par == 0:
        print(f'Seu número {valor_int_int} é par, pois o resto da divisão por 2 é {num_par}\n')
    else:
            print(f'Seu número {valor_int_int} é impar, pois o resto da divisão por 2 não é 0\n')
#fim função
            
valor_int_input = input('Digite um número inteiro, por favor \n')

if valor_int_input.isdigit():
    valor_int_int = int(valor_int_input)
    par_ou_impar(valor_int_int)
else:
     print('Você não digitou um número inteiro!')
'''
Faça um programa que pegunte a hora ao usuário e, baseando-se no horário descrito, 
exiba a saudação apropriada. Ex: Boa Madrugada 1-4, Bom dia 5-11, Boa tarde 12-18, Boa noite 19-00.
'''
hora_user = input('Digite o seu horário de agora, por favor \n')
hora_user_int = int(hora_user)

lista_madrugada = [1, 2, 3, 4]
lista_dia = [5, 6, 7, 8, 9, 10, 11]
lista_tarde = [12, 13, 14, 15, 16, 17, 18]
lista_noite = [19, 20, 21, 22, 23, 0]

if hora_user_int != str:

    if hora_user_int in lista_dia:
        print(f'Bom dia, agora são {hora_user} horas da manhã')
    elif hora_user_int in lista_tarde:
        print(f'Boa tarde, agora são {hora_user} horas da tarde')
    elif hora_user_int in lista_noite:
        print(f'Boa noite, agora são {hora_user} horas da noite')
    else:
        print(f'Boa madrugada, agora são {hora_user} horas da madrugada')
else:
    print('Você não digitou um horário válido.')
        
'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal", maior que 6 letras escreva "Seu nome é muito grande".
'''   

# primeiro_nome = input('Escreva somente seu primeiro nome, por favor \n')

# qnt_letras = len(primeiro_nome)  #- nome.count(" ")

# if qnt_letras > 6:
#     print(f"Seu nome é muito grande, pois tem {qnt_letras} letras")
# elif qnt_letras >= 5 and qnt_letras <= 6:
#     print(f"Seu nome é normal, pois tem {qnt_letras} letras")
# else:
#     print(f"Seu nome é curto, pois tem {qnt_letras} letras")

