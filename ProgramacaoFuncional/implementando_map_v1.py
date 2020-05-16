#Implementação da função map

def mapear(funcao, lista):        
#----------------------Minha resolução-------------------------------------------        
    # return (funcao(elemento) for elemento in lista)
#--------------------------------------------------------------------------------

#---------------------Resolução da aula------------------------------------------
    iteracao = 0
    for elemento in lista:        
        print(f'Passando pela iteração {iteracao + 1}')
        iteracao += 1
        yield funcao(elemento)
#--------------------------------------------------------------------------------

if __name__ == '__main__':
    # print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(next(resultado))
    print(next(resultado))
    print(next(resultado))
    print(next(resultado)) #Stop iteration indicando que já terminou a iteração