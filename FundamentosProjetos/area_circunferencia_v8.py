# Área da circunferência: PI * (raio)^2

from math import pi
import sys  # Esse módulo irá fazer com que seja obtido o argumento via terminal


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print('Favor, preencher o valor do raio de uma circunferência.')
    print(f'Sintaxe: {sys.argv[0][2:]} <raio>')


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            help()
        else:            
            raio = sys.argv[1] # Passando o valor como argumento via terminal, que está na posição 1 do argv.
                               # A posição 0 irá retornar o nome do módulo atual que está sendo executado
            area = circulo(raio)
            print(f'Área da circunferência: {area}')
    except ValueError as e:
        print(f'Valor inválido: {e}')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    finally:
        print('Fim do programa =)')
