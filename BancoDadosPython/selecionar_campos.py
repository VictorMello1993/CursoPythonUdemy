#Selecionando campos específicos (anteriormente foi feito uma consulta de todos os dados)

from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT nome, tel FROM contatos'

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            contatos = cursor.fetchall()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            for contato in contatos:
                # print(contato[0]) #Imprimindo o nome de cada contato (coluna índice 0)
                # print(contato[1]) #Imprimindo o telefone de cada contato (coluna índice 1)
                # print(type(contato)) #Cada registro é uma tupla de dados, com suas respectivas colunas que é uma string
                # print(type(contato[0])) #Tipo: string

                print('\t'.join(campo for campo in contato))
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')                                