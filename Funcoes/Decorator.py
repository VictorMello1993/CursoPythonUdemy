# %% [markdown]

# Decorators
# %%


def funcaoPrincipal(fn):
    def decorator(*args, **kargs):
        print(f'Início da chamada da função {fn.__name__}')
        print(f'args {args}')
        print(f'kargs {kargs}')
        resultado = fn(*args, **kargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator

#Declarando funções com padrão decorator
@funcaoPrincipal
def soma(x, y):
    return x + y


@funcaoPrincipal
def sub(x, y):
    return x - y

print(soma(5, 7))