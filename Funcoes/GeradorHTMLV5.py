# %% [markdown]

## Gerador de HTML (versão 5) - Passando parâmetros nomeados
# %%

#Tuplas de tags suportadas pelo HTML
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')

'''Função filtrar_atrbs é responsável por retornar uma string que representa um elemento com par de chaves-valor,
onde a chave é uma substring obtida a partir de um split com _ e acessando o último elemento da array de string resultante do método
split, eliminando o prefixo, e o valor é representado pela atribuição de um parâmetro nomeado passado na função tag_bloco()'''

'''Restrição: a função só irá gerar um par de chaves-valor se
o elemento chave estiver contido em uma das duas tuplas
declaradas acima'''
# k-> chave v-> valor
def filtrar_atrbs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' 
    for k, v in informados.items() if k in suportados)

def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **novos_atrs)        
    return f'<{tag} {filtrar_atrbs(novos_atrs, bloco_atrs)} class="{classe}">{html}</{tag}>'

def tag_lista(*itens, **novos_atrs):    
    return f'<ul>{filtrar_atrbs(novos_atrs, ul_atrs)}</ul>'

print(tag_bloco(tag_lista, 'Item 1', 'item 2', classe='info',
                bloco_accesskey='m', bloco_id='conteudo', ul_id='lista', blabla='blabla', ul_style='color:red'))