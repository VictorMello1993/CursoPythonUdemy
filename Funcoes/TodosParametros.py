# %% [markdown]

## Acessando todos os parâmetros (genérico)
# %%

def todos_params(*posicionais, **nomeados):
    print(f'Posicionais: {posicionais}')
    print(f'Nomeados: {nomeados}\n')

todos_params(1,2,3) #3 Parâmetros posicionais e nenhum parâmetro nomeado
todos_params(1,2,3, nome='Victor', solteiro=True) #3 parâmetros posicionais e 2 parâmetros nomeados
todos_params(nome='Victor', idade=26, solteiro=True) #3 parâmetros posicionais e nenhum parâmetro posicional
todos_params([1,2,3], 'a', 'b', 'c', nome='Victor', solteiro=True) #4 parâmetros posicionais e 2 parâmetros nomeados

# todos_params(nome='Victor', solteiro=True, 1, 2, 3) #Erro: neste caso, a função está aguardando primeiramente os parâmetros posicionais e depois os nomeados