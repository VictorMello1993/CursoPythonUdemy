# Área da circunferência: PI * (raio)^2

from math import pi

try:
    print('Informe o valor do raio: ')
    raio = input()

    area = pi * pow(float(raio), 2)
except ValueError as e:
    print(f'Erro: {e}')    
else:    
    print(f'Área: {area}')
    print('Fim do programa =)')

print('Nome do módulo', __name__)  #__main__ -> escopo global da aplicação
print('Nome do pacote', __package__)  
print(dir())