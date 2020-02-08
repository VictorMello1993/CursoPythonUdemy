# %% [markdown]

## Tuplas

#Ao contrário de listas, tuplas não podem ser alteradas

#Sintaxe:
tupla = tuple()

#Ou
tupla = ()
tupla

# tipo: tupla
type(tupla)

# métodos disponíveis para tuplas
dir(tupla)

# help(tuple)

tupla = ('Ola mundo')
type(tupla) #Os parênteses definem uma expressão, logo
            #o tipo deixa de ser uma tupla    

"""Para o interpretador entender de que se trata de uma tupla,
basta por uma vírgula (,)"""
tupla = ('Ola mundo',)
type(tupla)

#Acessando um elemento da tupla
tupla[0]
# tupla[0] = 'Teste' #Erro! Tuplas são estruturas imutáveis

cores = ('verde', 'amarelo', 'azul', 'branco')
cores[0]
cores[-1]
cores[1:]

#Obtendo o índice correspondente ao parâmetro passado
cores.index('amarelo') #índice 1
cores.count('branco')

#Se passar um elemento que não existe na tupla, retornará 0
cores.count('Branco')

#Tamanho da tupla (nº total de elementos)
len(cores)