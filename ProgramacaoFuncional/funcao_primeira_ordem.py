#Funções de primeira ordem: Conceito que tratam funções como parâmetros de outras funções

from funcao_primeira_classe import dobro, quadrado #importando as funções implementadas do módulo 'funcao_primeira_classe.py'


def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(f'{i} => {funcao(i)}')
    print('\n')    

if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro) #Passando a função 'dobro' como parâmetro da função 'processar'
    processar('Dobros de 1 a 10', range(1, 11), quadrado) #Passando a função 'quadrado' como parâmetro da função 'processar'