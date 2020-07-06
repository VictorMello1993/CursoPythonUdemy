#Resolvendo o problema do arquivo não fechar quando ocorrer erro no código
try:
    arquivo = open('pessoas.csv')
    for linha in arquivo:
        print('Nome: {}, Idade: {}'.format(*linha.strip().split(','))) #Usando * irá extrair os elementos de uma coleção de dados (lista, tuplas dicionários, sets, etc)    

except IndexError:
    pass
finally:
    print('fim do programa')
    arquivo.close()

if arquivo.closed:
    print('O arquivo já foi fechado')


'''OBS: O bloco finally sempre será executado independetemente se ocorrerá erro ou não dentro do bloco try, mas não irá executar
   a linha arquivo.closed se ocorrer erros. Para contornar isso, utiliza-se o bloco except com o pass que irá passar diretamente para
   as próximas linhas, inclusive o arquivo.closed'''    