# %% [markdown]
## Parâmetros opcionais e Unpacking
# %%
# Gerador de HTML (versão 4)
def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'

def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens)) #Generator
    return f'<ul>{lista}</ul>'

print(tag_bloco('bloco'))
print(tag_bloco('inline e classe', classe='info', inline=True))
print(tag_bloco('inline', inline=True))
print(tag_bloco(conteudo='inline', inline=True))
print(tag_lista('Item 1', 'Item 2', 'Item 3'))
print(tag_bloco(tag_lista('Item 1', 'Item 2', 'Item 3'), classe='Info'))
print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='Info', inline=True))
