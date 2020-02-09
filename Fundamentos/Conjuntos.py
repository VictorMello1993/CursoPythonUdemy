# %% [markdown]

## Conjuntos
"""
São estruturas de dados que armazenam apenas um conjunto de 
valores, assim como as listas, diferentemente de tuplas
e dicionários que armazenam um conjunto de pares de
chaves-valor

Conjuntos não são estruturas indexadas, não garantem
uma ordem de inserção de elementos nem aceitam valores
repetidos, ao contrário das listas
"""

# Sintaxe de um conjunto (sets)
a = {1, 2, 3}
type(a)

"""
ERRO! Conforme dito acima, não é possível acessar um 
elemento pelo índice."""
# a[0]

a = set('Olá mundo!')
b = set('OlaaaaaaaaaMundoo')
print(a)
print(b) #Percebe-se que conjuntos não aceitam repetição 
         #nem garante a ordenação de elementos

#Utilizando operador membro em conjuntos
print('a' in b, 'Z' not in b, 'e' in b)  

#Comparando conjuntos
print({1, 2, 3} == {3, 2, 1, 3})

#Operações em conjuntos

c1 = {1, 2} 
c2 = {2, 3}

#União
c1.union(c2)

# Interseção
c1.intersection(c2)

#Atualizando um conjunto a partir dos valores de outro conjunto
c1.update(c2) #O resultado é o conjunto c1 com valores atualizados
c1

# Verificando se um conjunto é subconjunto do outro
c2 <= c1 #c2 está contido no c1
c1 >= c2 #c1 contém elementos do conjunto c2

# Difereça entre conjuntos
{1, 2, 3} - {2}
c1 - c2

#Operação de atribuição subtrativa entre conjuntos
c1 -= {2} #Retirando o elemento 2 do c1
c1