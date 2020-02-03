#%% [markdown]

## Operadores ternários

esta_chovendo = False

print('Hoje estou de roupas ' + ('secas.', 'molhadas.')[esta_chovendo])

"""No Python, utilizando os colchetes como operador ternário,
o resultado é verdadeiro quando estiver próximo da expressão
(no caso, seria o segundo operando ('molhadas')), e falso
quando estiver distante da expressão"""

print('Hoje estou de roupas ' + ('molhadas.' if esta_chovendo else 'secas.'))

