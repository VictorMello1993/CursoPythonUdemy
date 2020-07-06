#Importando um pacote que representa uma "fachada" de outros pacotes
from calc import soma, subtracao

print('Soma', soma(3, 2))
print('Subtração', subtracao(3, 2))

'''Nesse exemplo foi possível acessar um pacote que contém funções do módulo
"modulo1" do pacote "pacote1" e do pacote "pacote2", todos eles agrupados
numa "fachada"'''
