# Sequência de Fibonacci
# 0 1 1 2 3 5 8 13 21 ...

# Versão 5: Utilizando sum() para somar os elementos de um array


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:])) #Equivalente a resultado.append(sum([resultado[-1], resultado[-2]]))
    return resultado        


if __name__ == '__main__':    
    for fib in fibonacci(10000):
        print(f'{fib}', end=' ')
