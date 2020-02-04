#%% [markdown]

## Tipos numéricos (parte 1)

dir(int)
dir(float)

a = 5
b = 2.5
a / b
a + b
a * b

type(a)
type(b)
type(a - b)

#Verificando se uma variável é do tipo int
b.is_integer()
5.0.is_integer()

int.__add__(2, 3) #Equivalente a 2 + 3

#Número absoluto
(-2).__abs__() #É equivalente a abs(-2)
(-2.5).__abs__() #É equivalente a abs(-2.5)

dir(float)

# %% [markdown]

## Tipos numéricos (parte 2)

# 1.1 + 2.2

"""
Decimal não existe no builtins. Logo, será necessário 
realizar a importação, conforme o exemplo abaixo
"""
from decimal import Decimal, getcontext
getcontext().prec = 4 #Definindo 4 casas decimais
Decimal(1) / Decimal(7)
Decimal(1.1) + Decimal(2.2)

dir(Decimal)
import decimal

"""Importando decimals, os módulos getcontext() e Decimal
agora pertence ao escopo global do Python
"""
dir(decimal)
dir()