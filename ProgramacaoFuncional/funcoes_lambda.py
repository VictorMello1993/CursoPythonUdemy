#Funções lambda (funções anônimas) e função map()

#Exemplo 1:
a = [1,2,3]
dobros1 = list(map(lambda i: i * 2, a))
dobros2 = tuple(map(lambda i: i * 2, a))

print(dobros1)
print(dobros2)

print('\n')

quadrados1 = list(map(lambda i: i ** 2, a))
quadrados2 = tuple(map(lambda i: i ** 2, a))

print(quadrados1)
print(quadrados2)

'''Função map() é responsável pela criação de uma nova coleção (lista ou tupla) a partir da transformação dos elementos da coleção 
   original, sem modificar os seus elementos.'''

print('\n')

# Exemplo 2
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14}
)

totais = tuple(
    map(lambda compra: compra['quantidade'] * compra['preco'], compras)
)

print('Preços totais: ', totais)
print('Total geral: ', sum(totais))
