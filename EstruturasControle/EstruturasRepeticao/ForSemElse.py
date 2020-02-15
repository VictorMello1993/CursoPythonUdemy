# %% [markdown]

# FOR sem else

PALAVRAS_PROIBIDAS = ('religião', 'política', 'esquerdista', 'direita')
textos = [
    'Victor não gosta de política',
    'Gosto de assistir Netflix',
    'Victor não é esquerdista nem de direita',
    'Nunca se mistura política com religião'
]

#Versão 1
for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:            
            print('Texto possui ao menos uma palavra proibida', palavra)
            found = True
            break
    if not found:
        print('Texto autorizado')

print('\n')

#Versão 2
palavras_proibidas_todas = []
for texto in textos:       
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:            
            palavras_proibidas_todas.append(palavra)

print('PALAVRAS PROIBIDAS')
for palavra_proibida in palavras_proibidas_todas:
    print(palavra_proibida)