# Sequência de Fibonacci
# 0 1 1 2 3 5 8 13 21 ...

# Versão 1: Fibonacci recursivo (correção)


def fibonacci(quantidade, sequencia = (0, 1)):
    if len(sequencia) == quantidade:        
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),)) #Utilizando a concatenação de tuplas (sobrecarga de operadores)             


if __name__ == '__main__':   
    for fib in fibonacci(20): 
        print(fib, end=' ')


