"""
fatiamento de strings
 012345678
 Olá Mundo
-987654321

Fatiamento[i:f:p] [::]          i = inicio f = fim p = passo

OBS: a função len retorna  a qntd de caracteres  da str
"""
variavel = 'Olá Mundo'
print(variavel[4:]) #marca o inicio e omiti o fim, então ele vai até o final.
print(variavel[:5]) #omiti o inicio e marca o fim, então ele vai do inicio até o index marcado.

print(len(variavel))