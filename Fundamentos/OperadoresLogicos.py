#%% [markdown]
## Operadores lógicos

True or False #Operador OR
7 != 3 and 2 > 3 #Operador AND

# Tabela verdade do AND
True and True #True
True and False #False
False and True #False
False and False #False
True and True and False and True and True and True

# Tabela verdade do OR
True or True #True
True or False #True
False or True #True
False or False #False
False or False or True or False or False or False

# Tabela verdade do XOR (ou exclusivo)
True != True #False
True != False #True
False != True #True
False != False #False

# Operador de negação (unário)
not True
not False

not 0 #Equivalente a not False
not 1 #Equivalente a not True

# Negação dupla retorna ao valor original
not not True #True
not not False #True

# Operadores bit a bit (números binários)
True & False #AND
False | True #OU
True ^ False #XOR

#3 = 11
#2 = 10
#_ = 10
3 & 2 #Resultado: 10 (2 em decimal)

#3 = 11
#2 = 10
#_ = 11
3 | 2 #Resultado: 11(3 em decimal)

#3 = 11
#2 = 10
#_ = 01
3 ^ 2 #Resultado: 01(1 em decimal)

# True && False #Operador inválido no Python

#Desafio: Calcula da meta do salário: 
#Se o saldo estiver positivo e o que sobrou no 
# mês foi mais de 20% do seu salário.

saldo = 1000
salario = 4000
despesas = 3967

meta = saldo > 0 and salario - despesas >= 0.2 * salario
meta

"""
Desafio 2: Se os dois trabalhos (Terça e Quinta) se 
concretizarem, a pessoa irá para o shopping comprar uma TV de 
50 polegadas. Em caso de um dos dois trabalhos se concretizarem,
irá comprar uma TV de 32 polegadas. Então, irá comprar sorvete
para comemorar. Se nenhum trabalho se concretizar, não irá
para o shopping para comprar TV nem tomar sorvete, mas terá
mais saúde
"""

trabalho_terca = True
trabalho_quinta = True
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
tv_50 = trabalho_terca and trabalho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
.format(tv_50, tv_32, sorvete, mais_saudavel))