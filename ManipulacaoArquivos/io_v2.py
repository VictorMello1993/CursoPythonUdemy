arquivo = open('pessoas.csv')
for linha in arquivo:
    print('Nome: {}, Idade: {}'.format(*linha.split(','))) #Usando * irá extrair os elementos de uma coleção de dados (lista, tuplas dicionários, sets, etc)    
arquivo.close()