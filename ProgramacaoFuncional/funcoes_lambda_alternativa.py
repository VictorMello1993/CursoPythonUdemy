#Funções lambida (versão alternativa - procedural
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14}
)

#No lugar da função lambda, foi utilizada uma função comum para realizar a mesma tarefa de processar os totais de preços
def obterPrecosTotais(compra):
    return compra['quantidade'] * compra['preco']

totais = tuple(map(obterPrecosTotais, compras))

print('Preços totais: ',totais)
print('Total geral: ', sum(totais))