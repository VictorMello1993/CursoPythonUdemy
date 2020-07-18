# Área da circunferência: PI * (raio)^2

from math import pi

def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    try:
        print('Informe o valor do raio: ')
        raio = input()
        area = circulo(raio)
        print(f'Área da circunferência: {area}')
    except ValueError as e:
        print(f'Erro: {e}')    
    finally:        
        print('Fim do programa =)')    