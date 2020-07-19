# Sequência de Fibonacci
# 0 1 1 2 3 5 8 13 21 ...

# Versão 6: Limitar a execução de acordo com a quantidade de elementos contidos numa lista


def fibonacci(quantidade):
    resultado = [0, 1] 
    for _ in range(2, quantidade): #Usando o _ para indicar que a variável de controle do FOR não está sendo usada na iteração
        resultado.append(sum(resultado[-2:]))
    return resultado



if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=' ')
