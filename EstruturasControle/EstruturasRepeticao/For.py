# %% [markdown]

# FOR (parte 1)

for i in range(1, 11):
    print('i = {0}'.format(i))


print('\n')
"""OBS 1: o limite superior no range() não é considerado no
intervalo
OBS 2:Um só parâmetro no range() indica que que o intervalo
varia de 0 até o parâmetro passado que corresponde
ao limite superior(exclusive) conforme dito no OBS1"""

for j in range(10):
    print('j = {0}'.format(j))

print('\n')

# Tabuada
for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')

# %% [markdown]

# FOR (parte 2)

# Percorrendo strings
palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=' ')  # Por padrão, o end recebe \n após o print

print('\n')
"""
É importante observar que uma vez substituído o \n, 
o próximo a ser executado imprime ainda na mesma linha"""

# Percorrendo uma lista
aprovados = ['Victor', 'Paula', 'Camilla', 'Vanderson']

for nome in aprovados:
    print(nome)
print('\n')

# Percorrendo os elementos e seus respectivos índices de uma lista em um FOR
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

# Imprimindo tuplas
dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')

print('\n')

for dia in dias_semana:
    print(f'Hoje é {dia}')

# Percorrendo sets (conjuntos)
print('\n')
for numero in set('Muito legal'):
    print(numero)
