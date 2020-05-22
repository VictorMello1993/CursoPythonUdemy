class Humano:
    #Atributo de classe (estática), onde a cada instância de uma classe
    #recebe o mesmo valor setado na classe
    especie = 'Homo Sapiens'


    def __init__(self, nome):
        self.nome = nome
    

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn')
    grokn.das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')