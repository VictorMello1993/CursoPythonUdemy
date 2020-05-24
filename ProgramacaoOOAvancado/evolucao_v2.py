'''Três tipos de métodos:
1) Métodos de instância
2) Métodos de classe
3) Métodos estáticos
'''


class Humano:
    # Atributo de classe (estática), onde a cada instância de uma classe
    # recebe o mesmo valor setado na classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    # Método de istância (recebe sempre o parâmetro self como primeiro parâmetro)
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    # Métodos estáticos (não recebem nenhum parâmetro)
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # Métodos de classes (recebem como primeiro parâmetro o nome da classe)
    @classmethod
    def is_evolucao(cls):
        return cls.especie == cls.especies()[-1]


class HomoNeanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = HomoNeanderthal('Grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instância): {", ".join(jose.especies())}')

    # Acessando os métodos a partir das classes
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evolucao()}')
    print(f'Neanderthal evoluído? {HomoNeanderthal.is_evolucao()}')

    # Acessando os métodos a partir das instâncias
    print(f'José evoluído? {jose.is_evolucao()}')
    print(f'Grokn evoluído? {grokn.is_evolucao()}')

'''OBS: Tantos os métodos de classe quanto os métodos estáticos, podem
ser acessados diretamente a partir da classe ou a partir das instâncias.'''
