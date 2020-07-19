# Sequência de Fibonacci
# 0 1 1 2 3 5 8 13 21 ...

# Versão 1: utilizando laço infinito


def fibonacci():
    penultimo = 0
    ultimo = 1

    print(f'{penultimo}, {ultimo}', end=' ')

    while True:
        proximo = penultimo + ultimo
        penultimo = ultimo
        ultimo = proximo
        print(f'{proximo}', end=' ')


if __name__ == '__main__':
    fibonacci()
