# Desafio: Obter todos os meses do ano com 31 dias, utilizando map, filter e reduce

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Setando a localização para o idioma PT-BR
setlocale(LC_ALL, 'pt_BR')

# --------------------------------------------------------------------------------MINHA RESOLUÇÃO-------------------------------------------------------------------------------------------
# Ignorando o índice 0 devido às limitações da biblioteca calendar
num_dias_mes = mdays[1:]
nome_meses = month_name[1:]
# print(num_dias_mes, nome_meses)

dias_meses = zip(num_dias_mes, nome_meses)
# print(list(dias_meses))

# Usando filter para obter 31 dias
meses_31_dias = list(filter(lambda mes: mes[0] == 31, dias_meses))

# Usando map para pegar os nomes dos meses com 31 dias
nome_meses_31_dias = list(map(lambda mes: mes[1], meses_31_dias))

# print(f'Meses com {meses_31_dias[0][0]} dias: {nome_meses_31_dias}')
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Solução 2, conforme desmonstrada na aula:
# 1) (filter) - pegar os índices de todos os meses com 31 dias
# 2) (map) - transformar os índices em nomes
# 3 (reduce) juntar tudo para imprimir

#1)
meses_31_dias = list(filter(lambda mes: mdays[mes] == 31, range(1, 13)))
print(meses_31_dias)

#2)
nome_meses_31_dias = list(map(lambda mes: month_name[mes], meses_31_dias))
print(nome_meses_31_dias)                                                                                                                                                                                             

#3)                                                                                                                                                                                                                                                                
nome_meses_dias = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}', nome_meses_31_dias, 'Meses com 31 dias:')
print(nome_meses_dias)