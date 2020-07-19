# Sequência de Fibonacci
# 0 1 1 2 3 5 8 13 21 ...

# Versão 3: Utilizando o recurso de packing para a troca de variáveis


def fibonacci(limite):
    penultimo = 0
    ultimo = 1

    print(f'{penultimo}, {ultimo}', end=' ')

    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(f'{ultimo}', end=' ')


if __name__ == '__main__':
    fibonacci(10000)
