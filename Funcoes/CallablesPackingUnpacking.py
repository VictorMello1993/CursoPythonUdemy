# %% [markdown]

## Callables com packing e unpacking
def calc_preco_final(preco_bruto, calc_imposto, *params):
    return preco_bruto + preco_bruto * calc_imposto(*params)

def imposto_x(importado):
    return 0.22 if importado else 0.13

def imposto_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0

preco_bruto = 1200.00
preco_final = calc_preco_final(preco_bruto, imposto_x, True)
print(f'Preço final: {preco_final}')

preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)
print(f'Preço final: {preco_final}')