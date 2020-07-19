# Sequência de Fibonacci
# 0 1 1 2 3 5 8 13 21 ...

# Versão 4: Utilizando lista para substituição de variáveis


def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado        


if __name__ == '__main__':    
    for fib in fibonacci(10000):
        print(f'{fib}', end=' ')
