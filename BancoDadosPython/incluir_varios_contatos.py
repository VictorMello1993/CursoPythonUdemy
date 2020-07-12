#Incluindo vários contatos de uma só vez
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao 

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Victor', '91234-5678'),
    ('Camilla', '98910-1112'),
    ('Pedro', '98989-8787'),
    ('Maxuel', '94444-5555'),
    ('Vanderson', '92323-5656'),
    ('Humberto', '98585-6666'),
    )

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.executemany(sql, args) #Inserindo vários registros
            conexao.commit() #Confirmando a transação do banco de dados para replicar os dados inseridos para o MYSQL
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print(f'Foram incluídos {cursor.rowcount} registro(s)')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')            


'''O auto-incremento despreza a ordem das chaves. Ele insere um novo registro baseado no último registro gravado, mesmo existindo  
"buracos"'''