#%% [markdown]
# ## Variáveis
#%% [markdown]

# Atribuição
a = 10
b = 5.2
print(a + b)

#OBS: Python é uma linguagem dinamicamente tipada, ou seja,
#     permite atribuir valores de diferentes tipos para uma
#     mesma variável.

# Antes
print(a)
a = 'Agora sou uma string'

# Depois
print(a)
b
#print(a + b) #Ambiguidade, uma vez que 'a' é uma string, 
              #e o interpretador não sabe se está fazendo 
              #concatenação ou de fato uma soma com 
              #valor real 'b'

