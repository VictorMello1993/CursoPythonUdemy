'''Funções de primeira classe: Conceito que trata as funções como se fossem dados, ou seja, 
armazenam funções que retornam valores dentro de uma coleção (listas, tuplas, dicionários ou sets)'''

#Exemplo:
def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2

#Armazenando funções como se fossem dados em uma lista
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
funcs = [dobro, quadrado] * 5 #Repetindo a lista 5 vezes
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Armazenando funções como se fossem dados em variáveis
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
d = dobro
# print(d(5))

q = quadrado
# print(q(10))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Usando o zip para juntar os elementos de 2 coleções em uma só coleção
if __name__ == '__main__':
    for func, numero in zip(funcs, range(1, 11)):
     print(f'O {func.__name__} de {numero} é: {func(numero)}')
