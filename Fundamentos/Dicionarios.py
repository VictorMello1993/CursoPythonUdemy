# %% [markdown]

## Dicionários (parte 1)

pessoa = {'Nome': 'Victor Mello', 'Idade': 26,
           'Idiomas': ['Inglês', 'Português']}

type(pessoa)

#Métodos disponíveis para dicionários
dir(pessoa)

#Tamanho do dicionário (nº de elementos presentes)
len(pessoa)

pessoa

#Acessando valores de uma chave
pessoa['Nome']
pessoa['Idade']
pessoa['Idiomas'] #Acessando lista contida no dicionário
pessoa['Idiomas'][1] #Acessando um elemento da lista contida no dicionário

#Obtendo uma lista de chaves disponíveis no dicionário
pessoa.keys()

"""Obtendo todos os valores correspondentes às suas respectivas
chaves contidos no dicionário"""
pessoa.values()

#Obtendo todos as combinações de chave e valoe
pessoa.items()

# Obtendo o valor da chave idade
pessoa.get('Idade')
pessoa.get('Idiomas')


"""OBS: Caso tente acessar um item que
não exista através do get(), diferetemente com os colchetes [],
o interpretador não emite o erro, mas sim o valor padrão"""
# pessoa.get('cursos')

"""Caso a propriedade não exista, com uso de colchetes
o interpretador emite o erro"""
# pessoa["cursos"]

#Caso não exista esta propriedade, será retornar o valor default (2º parâmetro)
pessoa.get('cursos', [])

# %% [markdown]

## Dicionários (parte 2)

#Alterando valores no dicionário
pessoa['Idade'] = 30

#Adicionando mais um elemento da lista contida no dicionário
# pessoa['Idiomas'].append('Alemão')
pessoa

#Removendo uma chave-valor do dicionário
# pessoa.pop('Idade')
# pessoa

# pessoa.pop('Idiomas')
pessoa.update({'Idade': 40, 'Sexo': 'M',
'Idiomas':['Inglês', 'Português', 'Alemão', 'Mandarim']})
pessoa

#Excluindo uma única chave
del pessoa['Idiomas']
pessoa

#Limpando o dicionário
pessoa.clear()
pessoa