#Recuperando dados do contato
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos'

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
                 print(f'{contato[2]:3d} - {contato[0]:10s} Telefone: {contato[1]}') #Obtendo dados da tabela 'contatos' em um looping             
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')