#Forma declarativa (procedural) de se programar

from locale import setlocale, LC_ALL
from calendar import mdays, month_name

setlocale(LC_ALL, 'pt_BR')

#Listar todos os meses com 31 dias_meses - Modo procedural
print('Meses com 31 dias: ')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')

