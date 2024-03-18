a = 'A'

b = 'B'

c = 1.1

string_0 = 'a = {} b = {} c = {:.2f}'
string_1 = 'a = {0} a = {0} a = {0} a = {0} b = {1} c = {2:.2f}'
string_2 = 'a = {nome1} b = {nome2} c = {nome3:.2f}'

formato0 = string_0.format(a, b, c)
formato_1 = string_1.format(a, b, c)
formato_2 = string_2.format(nome1=a, nome2=b, nome3=c)

print(formato0)
print(formato_1)
print(formato_2)



