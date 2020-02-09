# %% [markdown]
## Estruturas de seleção
#Versão de execução no Jupyter

#--------------------------Cenário-------------------------------------------------------------------------------------------

#Conceitos          Notas
# A                 De 10,0 à 9,1
# A-                De 9,0 à 8,1    
# B                 De 8,0 à 7,1
# B-                De 7,0 à 6,1
# C                 De 6,0 à 5,1
# C-                De 5,0 à 4,1
# D                 De 4,0 à 3,1
# D-                De 3,0 à 2,1
# E                 De 2,0 à 1,1
# E-                De 1,0 à 0,0
#-----------------------------------------------------------------------------------------------------------------------------
# Para notas maiores que 10 e menores que 0 será impresso "Nota inválida"
#Desafio: Criar uma função que converte a nota em conceito (retorno: string)

#Sintaxe para criação de uma função
def ObterConceito(nota):
    if(nota >= 9.1 and nota <= 10):
        return "A"
    elif(nota >= 8.1 and nota <= 9.0):
        return "A-"
    elif(nota >= 7.1 and nota <= 8.0):
        return "B"
    elif(nota >= 6.1 and nota <= 7.0):
        return "B-"
    elif(nota >= 5.1 and nota <= 6.0):
        return "C"
    elif(nota >= 4.1 and nota <= 5.0):
        return "C-"
    elif(nota >= 3.1 and nota <= 4.0):
        return "D"
    elif(nota >= 2.1 and nota <= 3.0):
        return "D-"
    elif(nota >= 1.1 and nota <= 2.0):
        return "E"
    elif(nota >= 0.0 and nota <= 1.0):
        return "E-"
    else:
        return "Nota inválida!"

nota = input('Informe a nota:')
print(ObterConceito(float(nota)))  