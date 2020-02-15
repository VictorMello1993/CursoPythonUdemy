# %% [markdown]
# Desafio simulando switch

# Cenário: Criar uma função que verifica se o dia pertence ao fim de semana ou se é durante a semana
# %%


def dia_semana_ou_final_de_semana(dia):
    dias = {1: 'Fim de semana',
            2: 'Dia de semana',
            3: 'Dia de semana',
            4: 'Dia de semana',
            5: 'Dia de semana',
            6: 'Dia de semana',
            7: 'Fim de semana',
            }
    return dias.get(dia, 'Valor inválido!')


for dia in range(0, 9):
    print(f'{dia}: {dia_semana_ou_final_de_semana(dia)}')
