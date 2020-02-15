# %% [markdown]
# Desafio

"""Criar uma função que sorteie um número de 1 a 6,
percorrer o dado e se o número for ímpar, executar continue.
Caso seja par e for igual ao número sorteado, imprimir 'ACERTOU'
e depois executar o break. Se não acertar chamar o else e
imprimir alguma coisa"""

# %%

from random import randint


def sortear_dado():
    return randint(1, 6)


num = input('Informe um número de 1 a 6: ')
num_sorteado = sortear_dado()
for i in range(1, 7):
    if(i % 2 != 0):
        continue
    elif i == num_sorteado and i == int(num):
        print('ACERTOU!', num)
        break
else:
    print('QUE PENA! =(')        