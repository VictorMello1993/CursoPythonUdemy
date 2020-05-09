#Função filter(): Retorna uma nova coleção a partir do resultado da filtragem da coleção original, sem modificar os elementos originais

#Exemplo:
pessoas = [
    {'Nome' : 'Victor', 'Idade': 26},
    {'Nome' : 'Vanderson', 'Idade': 33},
    {'Nome' : 'Camilla', 'Idade': 25},
    {'Nome' : 'Tomaz', 'Idade': 13},
    {'Nome' : 'Helena', 'Idade': 7},
    {'Nome' : 'Luiza', 'Idade': 3}
]

menores_idade = list(filter(lambda p: p['Idade'] < 18, pessoas))
print(menores_idade)


#Desafio: utilizar função filter para obter pessoas com nomes grandes (com mais de 6 caracteres)
pessoas_nomes_grandes = list(filter(lambda p: len(p['Nome']) > 6, pessoas))
print(pessoas_nomes_grandes)