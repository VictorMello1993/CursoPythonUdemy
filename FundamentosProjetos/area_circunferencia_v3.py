# Área da circunferência: PI * (raio)^2

from math import pi


if __name__ == '__main__':
    try:
        print('Informe o valor do raio: ')
        raio = input()

        area = pi * pow(float(raio), 2)
    except ValueError as e:
        print(f'Erro: {e}')    
    else:    
        print(f'Área: {area}')
        print('Fim do programa =)')    