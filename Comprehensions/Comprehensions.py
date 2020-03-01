# %% [markdown]
## Listas comprehension (versão 1)

#Sintaxe: [expressão for item in list]
dobros = [i * 2 for i in range(10)]
print('COMPREHENSIONS SEM CONDICIONAIS', dobros)
# %%
#Versão normal
dobros = []
for i in range(10):
    dobros.append(i * 2)
print('VERSÃO NORMAL ', dobros)
# %%
#Declarando lista comprehensions com condicionais

#Exemplo: Lista onde cada elemento será o dobro do índice se o mesmo for par
dobros_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print('COMPREHENSIONS COM CONDICIONAIS', dobros_dos_pares)