# Área da circunferência: PI * (raio)^2

from math import pi
import sys  
import errno


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print('Favor, preencher o valor do raio de uma circunferência.')
    print(f'Sintaxe: {sys.argv[0][2:]} <raio>')


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            help()            
            sys.exit(errno.EPERM) # Fazendo a chamada do sistema operacional para abortar o programa.
                                  # Por padrão é passado o valor 1 como sugere a constante EPERM

        if not sys.argv[1].isnumeric(): #Validando se o argumento passado é um valor numérico
            help()
            print('O raio deve ser um valor numérico!')        
            sys.exit(errno.EINVAL) #A constante EINVAL indica o valor 2

        raio = sys.argv[1] 
        area = circulo(raio)
        print(f'Área da circunferência: {area}')            
    except Exception as e:
        print(f'Erro inesperado: {e}')
    finally:
        print('Fim do programa =)')
