#Implementação da função map (usando expressão generator)

def mapear(funcao, lista):        
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(next(resultado))
    print(next(resultado))
    print(next(resultado))
    # print(list(resultado))