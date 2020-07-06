# Desafio: Extrair o nono e o quarto campos do arquivo csv sobre Região de Influência das Cidades do IBGE

# Minha resolução
# with open('desafio-ibge.csv') as arquivo:
#     for linha in arquivo:
#        print(f"{linha.split(',')[8]}: {linha.split(',')[3]}")


# Resolução 2: acessar arquivo diretamente da URL (o que foi abordado na aula)
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o arquivo...')
        dados = entrada.read().decode('latin1') #encoding latin1 equivale a ISO 8859-1
        print('Download concluído!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
