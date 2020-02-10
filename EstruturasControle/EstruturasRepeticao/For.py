# %% [markdown]

## FOR (parte 1)


for i in range(1, 11):
    print('i = {0}'.format(i))


print('\n')
"""OBS 1: o limite superior no range() não é considerado no
intervalo
OBS 2:Um só parâmetro no range() indica que que o intervalo
varia de 0 até o parâmetro passado que corresponde
ao limite superior(exclusive) conforme dito no OBS1"""

for j in range(10): 
    print('j = {0}'.format(j))

print('\n')

#Tabuada
for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')