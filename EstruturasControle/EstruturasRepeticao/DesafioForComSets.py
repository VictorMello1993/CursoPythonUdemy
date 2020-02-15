# %% [markdown]

# Desafio: percorrer com os sets (conjuntos)

PALAVRAS_PROIBIDAS = {'religião', 'política', 'esquerdista', 'direita'}
textos = [
    'Victor não gosta de política',
    'Gosto de assistir Netflix',
    'Victor não é esquerdista nem de direita',
    'Nunca se mistura política com religião'
]
dir(PALAVRAS_PROIBIDAS)

#Versão 1 (versão mais burra - FOR aninhado)
for texto in textos:
    for palavra in texto.lower().split():        
        if {palavra}.intersection(PALAVRAS_PROIBIDAS): #Interseção
            print('Texto possui ao menos uma palavra proibida', palavra)
            break
    else:
        print('Texto autorizado')
else:
    print('Fim')

"""Opcionamente poderia utilizar:
if not {palavra} - PALAVRAS_PROIBIDAS: Operador de diferença 
if {palavra} <= PALAVRAS_PROIBIDAS: Operador de subconjunto (um elemento de um conjunto está contido em outro conjunto)
if PALAVRAS_PROIBIDAS >= {palavra}: Operador de subconjunto (um conjunto contém elemento do outro conjunto)
"""
# %%

# Versão 2 (mais eficiente)
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui ao menos uma palavra proibida', intersecao)
    else:
        print('Texto autorizado')                            
        