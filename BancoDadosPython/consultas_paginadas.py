#Obtendo apenas a parte dos dados da tabela de contatos
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

# sql = 'SELECT nome, tel FROM contatos'
sql = 'SELECT nome, tel FROM contatos LIMIT 2 OFFSET 3' #Obtendo 3 registros a partir do 3º elemento da consulta

try:
    with nova_conexao() as conexao:
        try:
            datatable = conexao.cursor()
            datatable.execute(sql)     
            contatos = datatable.fetchall()       
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            for row in contatos:
                print(f'\t'.join(str(column) for column in row))            
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')


#OBS: OFFSET determina a posição do registro que será considerado como o primeiro elemento da consulta
#Implicitamente, o primeiro registro é aquele que está na posição 0 (zero) da consulta original.