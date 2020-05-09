#Desafio, usar função map para retornar frase <nome> tem <idade> anos.

pessoas = [
    {'Nome' : 'Victor', 'Idade': 26},
    {'Nome' : 'Vanderson', 'Idade': 33},
    {'Nome' : 'Camilla', 'Idade': 25}
]

frase = ' '.join(list(map(lambda pessoa: f"{pessoa['Nome']} tem {pessoa['Idade']} anos.", pessoas)))
print(frase)