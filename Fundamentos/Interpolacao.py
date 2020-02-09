# %% [markdown]

## Interpolação


from string import Template
nome, idade = 'Victor', 26

#Interpolação (forma 1 - C like)
print('Nome: %s Idade: %d' % (nome, idade))

#Interpolação (forma 2) - Python < 3.6
print('Nome: {0} Idade: {1}'.format(nome, idade))

#Interpolação (forma 3) - Python >= 3.6
print(f'Nome: {nome} Idade: {idade} {2 **8 + 1}')

#Interpolação (forma 4) - Usando a biblioteca Template
s = Template('Nome: $nm Idade: $age')
print(s.substitute(nm=nome, age=idade))