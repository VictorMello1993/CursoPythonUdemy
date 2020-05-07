#usando strip para eliminar espaços vazios nas bordas de uma string. Equivalente ao trim()
arquivo = open('pessoas.csv')
for linha in arquivo:
    print('Nome: {}, Idade: {}'.format(*linha.strip().split(','))) #Usando * irá extrair os elementos de uma coleção de dados (lista, tuplas dicionários, sets, etc)    
arquivo.close()