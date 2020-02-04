#%% [markdown]

## Builtins

# Identificando o tipo de dado de uma variável, que pertence ao módulo builtins
nome = 'Victor Santos de Mello'
type(nome)

# 1 + 2
# _ * 3

# a = 7
# import math
# help(dir)

# Exibe uma lista de membros disponíveis no escopo global do Python
dir()

"""
OBS: Evite sobrescrever o objeto __builtins__ para substituir 
os valores, pois ao executar as funções que são disponíveis,
por padrão, nesse módulo, o interpretador irá retornar
inconsistência de tipos
"""
#Exemplo: 
# __builtins__ = 3
# print()

# Exibindo os tipos disponíveis no módulo __builtins__
# dir(__builtins__)