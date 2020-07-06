with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida: #Gravando todo conteúdo do csv para um arquivo txt (escrita)
        for linha in arquivo:
            pessoa = linha.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida) #Imprimindo o conteúdo do arquivo csv diretamente no arquivo txt em vez de imprimir no console (por isso atribuir o parâmetro file no print())

if arquivo.closed:
    print('O arquivo já foi fechado')

if saida.closed:
    print('O arquivo de saída já foi fechado')

