'''
Introdução ao try/except
try -> tentar executar o código
execpt -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Vou dobrar o número que você digitar: ')
#Com try except
try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2} ')
except:
    print('Isso não é um número')


# Com if e else    
# if numero_str:
#     print('STR: ', numero_str)
#     numero_float = float(numero_str)
#     print('FLOAT: ', numero_float)
#     print(f'O dobro de {numero_str} é {numero_float * 2} ')
# else:
#     print('Isso não é um número')