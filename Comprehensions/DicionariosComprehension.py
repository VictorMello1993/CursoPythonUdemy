# %% [markdown]
##Dicionários comprehensions


#Sintaxe: {chave: valor->expressao for in dictionary condicional}
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

#Percorrendo dicionários comprehensions
for k, v in dicionario.items():
    print(f'{k} x 2 = {v}')