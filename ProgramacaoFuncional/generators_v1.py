'''Generators: Funções que possuem retornos parciais, ou seja, aqueles que
possuem memória interna'''

def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'índigo'
    yield 'violeta'

if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))

    while True:
        print(next(generator)) #Imprimindo elementos consecutivos