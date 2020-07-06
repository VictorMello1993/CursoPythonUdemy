#Resolvendo conflitos de módulos com o mesmo nome (usando apelidos)
from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_sub #apelidando um módulo

print('Soma', modulo1.soma(3, 2))
print('Subtração', modulo1_sub.subtracao(3, 2))