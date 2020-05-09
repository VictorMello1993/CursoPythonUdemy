'''Funções de imutabilidade: Funções que manipulam coleções sem modificar
os seus elementos originais'''

from functools import reduce
from operator import add

valores = (30, 10, 25, 70, 100, 94)

#Funções de imutabilidade
print(sorted(valores)) #Ordenando a lista
print(min(valores)) #Obtendo o menor valor da lista
print(max(valores)) #Obtendo o maior valor da lista
print(sum(valores)) #Obtendo a soma dos elementos da lista
print(reduce(add, valores)) #Obtendo a soma dos elementos da lista - reduce 
print(valores) #Lista original
print(tuple(reversed(valores))) #Obtendo a lista de trás para frente

print('\n')

#Forma funcional
# valores.sort()
# print(valores) #Os elementos da lista original foram modificados


'''Atenção: Trabalhar com coleções de dados imutáveis (tuplas) 
poderá gerar efeitos colaterais no código, pois não existem
funções de mutabilidade no contexto de tuplas'''