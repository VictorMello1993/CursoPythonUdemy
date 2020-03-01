# %% [markdown]

##Generators

#Sintaxe = (expressao for item in tuple condicional)
generator = (i ** 2 for i in range(10) if i % 2 == 0)
print('Imprimindo cada elemento sob demanda usando next(): \n')
print(next(generator)) #Saída: 0
print(next(generator)) #Saída: 4
print(next(generator)) #Saída: 16
print(next(generator)) #Saída: 36
print(next(generator)) #Saída: 64
# print(next(generator)) #Erro!

# %%
#Percorrendo generators
print('Imprimindo cada elemento do generator')
for num in generator:
    print(num)