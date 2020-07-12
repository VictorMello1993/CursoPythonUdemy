from mysql.connector.errors import ProgrammingError
from bd import nova_conexao 

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Victor', '91234-5678')

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit() #Confirmando a transação do banco de dados para replicar os dados inseridos para o MYSQL
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print('1 registro incluído, ID: ', cursor.lastrowid)
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')            


'''O auto-incremento despreza a ordem das chaves. Ele insere um novo registro baseado no último registro gravado, mesmo existindo  
"buracos"'''