# %% [markdown]

# Simulando switch (parte 1)

# Em python não existe o comando switch, mas é possível simular

# Simulando o comando switch usando dicionários
def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return dias.get(dia, 'Valor inválido!')


for dia in range(0, 9):
    print(f'{dia}: {get_dia_semana(dia)}')