# Área da circunferência: PI * (raio)^2

from math import pi
import sys #Esse módulo irá fazer com que seja obtido o argumento via terminal

def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    try:        
        raio = sys.argv[1] #Passando o valor como argumento via terminal, que está na posição 1 do argv. A posição 0 irá retornar o nome do módulo
        area = circulo(raio)
        print(f'Área da circunferência: {area}')
    except ValueError as e:
        print(f'Erro: {e}')
    finally:
        print('Fim do programa =)')                
            