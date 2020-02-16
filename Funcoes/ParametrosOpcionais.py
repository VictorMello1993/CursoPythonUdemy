# %% [markdown]

## Parâmetros opcionais

def testeParametroOpcional(texto, opcional = True):
    return f'{texto} {opcional}'


"""Como o segundo parâmetro é opcional, será impresso o valor
padrão se não for passado à função"""
print(testeParametroOpcional('OlaMundo'))
print(testeParametroOpcional('OlaMundo', False))
print(testeParametroOpcional('OlaMundo', True)) 