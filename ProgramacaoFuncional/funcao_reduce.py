#Função reduce(acumulador, função que será executada a cada iteração, valor inicial)
#Essa função é responsável por reduzir a coleção de elementos para um valor único após a transformação dos elementos da coleção original

from functools import reduce

pessoas = [
    {'Nome' : 'Victor', 'Idade': 26},
    {'Nome' : 'Vanderson', 'Idade': 33},
    {'Nome' : 'Camilla', 'Idade': 25},
    {'Nome' : 'Tomaz', 'Idade': 13},
    {'Nome' : 'Helena', 'Idade': 7},
    {'Nome' : 'Luiza', 'Idade': 3}
]


#Exemplo 1: 
somente_idades = list(map(lambda p: p['Idade'], pessoas))
# soma_idades = reduce(lambda total_parcial_idades, p: total_parcial_idades + p['Idade'], pessoas, 0)
soma_idades = reduce(lambda total_parcial_idades, idade: total_parcial_idades + idade, somente_idades, 0)
print(soma_idades)

#Exemplo 2:
#Juntando todos os conceitos (map + filter + reduce)
menores_idade = list(filter(lambda idade: idade < 18, somente_idades))
soma_menores_idades  = reduce(lambda idades, idade: idades + idade, menores_idade, 0)
print(soma_menores_idades)
