# %% [markdown]

## Criando uma classe Data

class Data:
    # def toStr(self):
    #     print(f'{self.dia}/{self.mes}/{self.ano}')

    '''Chamando o método mágico que retorna um objeto 
       em formato de string. Este método é padrão
       para todos os objetos do Python'''
    def __str__(self):
        return(f'{self.dia}/{self.mes}/{self.ano}')
    

# Instanciando Data
d1 = Data()
d1.dia = 3
d1.mes = 3
d1.ano = 2020


'''
Em Python, toda a criação dos métodos de uma classe deve 
sempre começar com o objeto self como primeiro parâmetro,
que representa um objeto que está sendo referenciado
ao realizar a chamada de um método'''

#Instanciando mais um objeto data
d2 = Data()
d2.dia = 15
d2.mes = 12
d2.ano = 1993

#Invocando o método da classe Data
# d1.toStr() #O objeto self aponta para objeto d1
# d2.toStr() #O objeto self aponta para objeto d2

#Invocando um método de um objeto implicitamente (método mágico)
print(d1) 
print(d2) 