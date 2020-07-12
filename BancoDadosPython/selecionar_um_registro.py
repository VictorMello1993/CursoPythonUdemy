#Obtendo apenas a parte dos dados da tabela de contatos
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

# sql = 'SELECT nome, tel FROM contatos'
sql = 'SELECT nome, tel FROM contatos LIMIT 3 OFFSET 10' #Obtendo 3 registros a partir do 10º elemento da consulta

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)            
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            #Obtendo apenas um registro a partir do resultado gerado pelo SELECT
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
            print(cursor.fetchone()) 
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')