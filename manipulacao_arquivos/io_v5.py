#Usando o bloco with para garantir que no final da execução da leitura de um arquivo, o mesmo será fechado, sem a necessidade de utilizar close
with open('pessoas.csv') as arquivo:
    for linha in arquivo:
        print('Nome: {}, Idade: {}'.format(*linha.strip().split(','))) #Usando * irá extrair os elementos de uma coleção de dados (lista, tuplas dicionários, sets, etc)    

if arquivo.closed:
    print('O arquivo já foi fechado')