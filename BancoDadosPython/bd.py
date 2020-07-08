from mysql.connector import connect
from mysql.connector import ProgrammingError
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    password='xxxxxxxxxxxxxxxxxxxxxxxxxx',
    database='agenda'
)

#Decorator para instanciar uma nova conexão de banco de dados. Futuramente será adaptado para que a conexão seja feita dentro do bloco 'with'
@contextmanager
def nova_conexao():    
    conexao = connect(**parametros)
    try:
        yield conexao                
    finally:
        if conexao and conexao.is_connected():
            conexao.close()  #Liberando recursos alocados se uma instância de banco de dados estiver aberta                  
                              