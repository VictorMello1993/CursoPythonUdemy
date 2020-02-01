# %% [markdown]
# ## Operadores aritméticos

print(2 + 3) # Soma
print(4 - 7) # Subtração
print(2 * 5.3) # Multiplicação
print(9.4 / 3) # Divisão
print(9.4 // 3) # Divisão (truncado)
print(2 ** 8) # Exponenciação
print(10 % 4) # Resto da divisão

a = 12
b = a
print(a + b)
# %% [markdown]
# Desafio: Calcular a porcentagem de comprometimento do salário em relação às despesas
# %%
salario = 3450.45
despesas = 2456.2

comprometimento = despesas / salario
# print(round(comprometimento, 2) * 100)
print('{0:.0%}'.format(comprometimento)) #Especificando a porcentagem


# %%
