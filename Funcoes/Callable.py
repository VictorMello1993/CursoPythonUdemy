# %% [markdown]

# Callable
# Callables são objetos que são passíveis de serem invocadas, ou seja, que representam funções
# %%
# Exemplo: passando uma função como parâmetro em outra função

def executar(funcao):
    if callable(funcao):
        funcao()
    else:
        print('Este objeto não é uma função')


def bom_dia():
    print('Bom dia!')


def boa_tarde():
    print('Boa tarde!')


def boa_noite():
    print('Boa noite!')


executar(bom_dia)
executar(boa_tarde)
executar(boa_noite)
executar(1)