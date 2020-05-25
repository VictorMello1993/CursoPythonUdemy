# Iterators: Objetos que são iteráveis


class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    #Definindo a classe que será instanciada como um objeto iterável
    def __iter__(self):
        return self

    # Definindo a classe como sendo um iterator
    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()


if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

try:
    print(next(cores))
except StopIteration:
    print('Acabou')

# Percorrendo objeto iterável (graças ao método mágico __iter__)
for cor in RGB():
    print(cor)
