#Propriedades (getters e setters)

class Humano:
    # Atributo de classe (estática), onde a cada instância de uma classe
    # recebe o mesmo valor setado na classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def get_idade(self):
        return self._idade
    
    def set_idade(self, idade):
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


if __name__ == '__main__':
    jose = HomoSapiens('José')
    jose.set_idade(40)
    # jose._idade = - 40
    print(f'Nome: {jose.nome} - Idade: {jose.get_idade()}')    
