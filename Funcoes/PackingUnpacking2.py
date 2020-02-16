# %% [markdown]

# Packing e unpacking (parte 2)

# %%

# %% [markdown]

## Packing e Unpacking (parte 2) 
# %%

def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

print(tag_bloco('bloco'))
print(tag_bloco('inline e classe', 'info', True))

# Chamando função com parâmetros nomeados
print(tag_bloco('inline', inline=True))
print(tag_bloco(texto='inline', inline=True))
# %%

#Criando uma lista <ul> utilizando packing
def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens)) #Generator
    return f'<ul>{lista}</ul>'

print(tag_lista('Item 1', 'Item 2', 'Item 3'))

#Empacotando com uma div
print(tag_bloco(tag_lista('Item 1', 'Item 2', 'Item 3'), 'Info'))
