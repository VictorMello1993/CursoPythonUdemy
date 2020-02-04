#%% [markdown]
## Conversao de tipos

2 + 3 #Soma
'2' + '3' #Concatenação
# 2 + '3'

a = 2
b = '3'

print(type(a))
print(type(b))

#Convertendo uma string para int
print(a + int(b))

#Convertendo a variável a (tipo int) para string. Resultado: concatenação
print(str(a) + b)

#Resultado: string (resultado da conversão)
type(str(a))

"""
#Erro: Caracteres de uma string que não são números não 
suportam a conversão para int
"""
#Exemplo
# print(2 + int('2 Victor'))

#Convertendo para float
print(2 + float('3.4'))
print(2 + float('3'))