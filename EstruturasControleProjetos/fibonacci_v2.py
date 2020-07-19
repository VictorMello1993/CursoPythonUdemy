# Sequência de Fibonacci
# 0 1 1 2 3 5 8 13 21 ...

# Versão 2: Estabelecendo o limite de execução do Fibonacci


def fibonacci(limite):
    penultimo = 0
    ultimo = 1

    print(f'{penultimo}, {ultimo}', end=' ')

    while ultimo < limite:
        proximo = penultimo + ultimo
        penultimo = ultimo
        ultimo = proximo
        print(f'{proximo}', end=' ')


if __name__ == '__main__':
    fibonacci(10000)
