#%% [markdown]

## Coerção automática (conversão automática)
"""
#OBS: Em python, a divisão entre valores inteiros o 
resultado sempre será float
"""
#Exemplo 1
10 / 2
type(10 / 2)

#Exemplo 2
10 / 3
type(10 / 3)

#Exemplo 3 (divisão truncada)
10 // 3 #Neste caso, o resultado será int
type(10 // 3)

"""
Na divisão truncada, se tiver pelo menos um operando
float, o resultado será float com casa decimal
zerada, mesmo que o resultado seja uma divisão
exata.
"""
#Exemplo 1
10 // 3.3 

#Exemplo 2      
10 // 2.5        

#Situação especial
2 + True #Resultado: int, 
         #pois True assume como sendo valor 1, 
         #e False como valor 0
         
type(2 + True)

2 + False
type(2 + False)