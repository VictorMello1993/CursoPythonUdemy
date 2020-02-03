#%% [markdown]

## Mais operadores

lista = [1, 2, 3, 'Victor', 'Mello']

#Operador de membro
# print(2 in lista)
# print('Victor' in lista)
# print('Mello' not in lista)

#Operador de identidade
x = 3
y = x
z = 3
print(x is y)
print(y is z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

lista_a[0] = 300
lista_b[1] = 200

print(lista_a is lista_b) 
print(lista_a is lista_c) 

"""
No último print, o resultado será falso, pois lista_c
não recebeu uma cópia da lista_a. Neste caso, são listas
com espaços de memória diferentes mesmo que os seus membros
possuam o mesmo valor
"""
                            