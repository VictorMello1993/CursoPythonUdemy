# %% [markdown]

# Desafio gerador de HTML

'''Criar uma função que retorne HTML genérico, abrindo e fechando as tags, 
suportando quaisquer atributos na tag e o seu conteúdo pode ser um texto 
ou uma lista com vários textos (ou outras tags já como texto).
Caso encontre um atributo chamado de css, renomeá-lo para class. 

Isso é necessário por que class é uma palavra reservada em Python, 
e não poderia ser usado como literal na chamada da função'''

# Resultado esperado:
# <p class="alert"><span >Curso de Python 3, por </span><strong id="jf">Juracy Filho</strong><span > e </span><strong id="ll">Leonardo Leitão</strong><span >.</span></p>


# %%

# Minha resolução
def tag(tag, *args, **kwargs):
    atrbs = ''.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in kwargs.items())

    html = ''.join((f'{conteudo}' for conteudo in args))
    return f'<{tag}{" " if atrbs else ""}{atrbs}>{html}</{tag}>'


print(tag('p',
          tag('span', 'Curso de Python 3, por '),
          tag('strong', 'Juracy Filho', id='jf'),
          tag('span', ' e '),
          tag('strong', 'Leonardo Leitão', id='ll'),
          tag('span', '.'),
          html_class='alert'))
# %%
# Correção


def tag2(tag, *args, **kwargs):
    #Eliminando o termo html_ da string
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    atrbs = ''.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in kwargs.items())

    html = ''.join((f'{conteudo}' for conteudo in args))
    return f'<{tag}{" " if atrbs else ""}{atrbs}>{html}</{tag}>'


print(tag2('p',
          tag2('span', 'Curso de Python 3, por '),
          tag2('strong', 'Juracy Filho', id='jf'),
          tag2('span', ' e '),
          tag2('strong', 'Leonardo Leitão', id='ll'),
          tag2('span', '.'),
          html_class='alert'))
