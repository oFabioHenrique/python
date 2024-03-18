"""
Operadores Lógicos
and (e) or (ou) not (não)
and - todas condições precisam ser verdadeiras se não será avaliada como False
or - se uma das condição for verdadeira será avaliada como True 
not - negação 
OBS: São considerados falsy no python: 0 | 0.0 |
'' | False 
também existe o tipo None que é usado para representar um não valor
"""
entrada = input('[E]ntrar [S]air: ')

senha_digitada = input('Insira sua senha: ')
senha_permitida = '123456'

## and ##
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Você entrou')
else:
    print('Você não entrou')

#Avaliação de curto circuito
print(True and False and True) # para no false e retorna ele
print(True and 0 and True) # para no 0 (False) e retorna ele


## OR ## o parentêses dita a precedência da verificação da expressão
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Você entrou')
else:
    print('Você não entrou')

#Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha' # para no false e retorna ele

## not ##
# ele vai inverter a expressão
print(True)
print(not True)
print(False)
print(not False)
