# %% [markdown]

# Problema de parâmetros padrão mutáveis
# %%


def fibonacci1(sequencia=[0, 1]):
    # Uso de parâmetros mutáveis como valor default (um erro)
    # Concatenação de listas. O resultado é a mesma lista com novos elementos inseridos
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


inicio = fibonacci1()
print(inicio, id(inicio))
print(fibonacci1(inicio))
restart = fibonacci1()
print(restart, id(restart), '\n')

# assert restart == [0, 1, 1] #Resultado esperado
'''Como os ids das variáveis inicio e restart são os mesmos
poque representam um mesmo objeto na memória que corresponde
à função fibonacci1, com append na lista (parâmetro padrão)
que é mutável, será retornado com valor diferente e, 
por consequência, será propagado para as próximas chamadas 
que forem realizadas.'''

# Solução 1: Alterar o parâmetro para uma tupla.


def fibonacci2(sequencia=(0, 1)):
    # Concatenação de tuplas. O resultado é uma nova tupla.
    return sequencia + (sequencia[-1] + sequencia[-2],)


inicio = fibonacci2()
print(inicio, id(inicio))
print(fibonacci2(inicio))
restart = fibonacci2()
print(restart, id(restart))

'''Como a função fibonacci2 não está modificando uma 
tupla, a concatenação resulta em uma nova tupla e,
portanto,  são objetos diferentes'''


# %%
# Solução 2 Atribuir o valor padrão para none no parâmetro mutável
def fibonacci3(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


inicio = fibonacci3()
print(inicio, id(inicio))
print(fibonacci3(inicio))
restart = fibonacci3()
print(restart, id(restart))

'''Se atribuir o valor None ao parâmetro mutável, isso
força que a variável sequencia seja diferente, graças
à verificação com operador or'''