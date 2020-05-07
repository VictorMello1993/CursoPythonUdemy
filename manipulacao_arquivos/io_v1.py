arquivo = open('pessoas.csv')
dados = arquivo.read() #Lendo o arquivo e atribuindo todo o conteúdo em uma variável
arquivo.close()

#Percorrendo o arquivo
for linha in dados.splitlines():
    # print(linha.split(',')) #Retorna cada registro de um arquivo representado por um array de strings a partir de um split por vírgula
    print('Nome: {}, Idade: {}'.format(*linha.split(','))) #Usando * irá extrair os elementos de uma coleção de dados (lista, tuplas dicionários, sets, etc)    