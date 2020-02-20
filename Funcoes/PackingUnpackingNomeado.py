# %% [markdown]

## Packing e unpacking nomeados (parte 1)
# %%

# Packing nomeado
print('PACKING')
def podium_packing(**ranking):
    for posicao, piloto in ranking.items():
        print(f'{posicao} -> {piloto}')


podium_packing(primeiro='Victor Mello', 
       segundo='Camilla Lima', 
       terceiro='Vanderson Guidi')

'''
OBS: usando ** indica que os parâmetros individuais passados na 
chamada da função serão encapsulados (packing) em um dicionário, 
sendo necessário passar parâmetros nomeados para indicar
um par de chaves-valor
'''

def podium_unpacking(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')

print('\n')
podium = {'segundo': 'Victor Mello',
           'primeiro': 'Camilla Lima',
           'terceiro': 'Vanderson Guidi'}

#Unpacking nomeado
print('UNPACKING')
podium_unpacking(**podium)

'''
Neste caso, desencapsular o dicionário para imprimir 
os parâmetros nomeados exibe apenas o valor de cada chave
passado. É preciso ficar atento com os asterísticos, pois
passando com um só * indica que será utilizado uma
tupla, e a ordem dos parâmetros é importante
'''