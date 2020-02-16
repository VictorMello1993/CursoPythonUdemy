# %% [markdown]

## Parâmetros posicionais e parâmetros nomeados

"""Parâmetros posicionais são aqueles que recebem valores
esperados na chamada da função, ou seja, a ordem dos 
parâmetros é respeitada na chamada da função"""

"""Já os parâmetros nomeados são aqueles que, independente
da ordem, apontam para o valor atribuído ao argumento passado 
para a função só pelo nome. Isso é comum quando são criadas as funções 
cujos parâmetros são do mesmo tipo e nunca se sabe ao qual
parâmetro, o nome dele, o valor atribuído se refere."""

# %%

def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

print(tag_bloco('bloco'))
print(tag_bloco('inline e classe', 'info', True))

#Chamando função com parâmetros nomeados
print(tag_bloco('inline', inline=True))
print(tag_bloco(texto='inline', inline=True))