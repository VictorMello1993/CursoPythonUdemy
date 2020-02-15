# %% [markdown]

# FOR com else

PALAVRAS_PROIBIDAS = ('religião', 'política', 'esquerdista', 'direita')
textos = [
    'Victor não gosta de política',
    'Gosto de assistir Netflix',
    'Victor não é esquerdista nem de direita',
    'Nunca se mistura política com religião'
]

#Versão 1
for texto in textos:    
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:            
            print('Texto possui ao menos uma palavra proibida', palavra)            
            break    
    else:
        print('Nenhuma palavra proibida encontrada')
else:
    print('Fim')            