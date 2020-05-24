#Classes abstratas

class Humano:
    # Atributo de classe (estática), onde a cada instância de uma classe
    # recebe o mesmo valor setado na classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def idade(self):
        return self._idade
    
    #Classe abstrata: Seus métodos não possuem implementação
    @property
    def inteligente(self):
        return False

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo')
        self._idade = idade

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

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    anonimo = Humano('Victor Santos')

    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('propriedade abstrata')   

    jose = HomoSapiens('José')     
    grogn = HomoNeanderthal('Grogn')
    
    print('{} da classe {}, inteligente: {}'.format(jose.nome, 
          jose.__class__.__name__, jose.inteligente))
    print('{} da classe {}, inteligente: {}'.format(grogn.nome, 
          grogn.__class__.__name__, grogn.inteligente))

