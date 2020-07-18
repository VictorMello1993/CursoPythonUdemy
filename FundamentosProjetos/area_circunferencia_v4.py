# Área da circunferência: PI * (raio)^2

from math import pi

def circulo(raio):
    print(f'Área: {pi * float(raio) ** 2}')


if __name__ == '__main__':
    try:
        print('Informe o valor do raio: ')
        raio = input()
        circulo(raio)        
    except ValueError as e:
        print(f'Erro: {e}')    
    finally:        
        print('Fim do programa =)')    