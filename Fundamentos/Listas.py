#%% [markdown]
## Listas (parte 1)

lista = [] #Lista vazia
type(lista)

dir(list)

"""
Em Python a lista é heterogênea (todos os elementos podem
ser de tipos distintos)
"""
#Exibindo o tamanho da lista (nº de elementos)
len(lista)

#Adicionando elementos à lista
lista.append(1)
lista.append(5)
lista.append([1, 2, 3])
lista

len(lista)

nova_lista = [1, 6, 'Victor', 'Pedro']
nova_lista

#Removendo elementos da lista
nova_lista.remove('Victor')
nova_lista

#Invertendo a lista
nova_lista.reverse()
nova_lista

# %% [markdown]
## Listas (parte 2)

lista = [1, 5, 'Victor', 'Camilla', 3.1415]

#Obtendo o índice correspondente ao parâmetro passado 
lista.index('Victor')
lista

#Obtendo o elemento a partir de um índice especificado
lista[3]

#Acessando elementos com operador membro
1 in lista
'Victor' in lista
'Camilla' in lista