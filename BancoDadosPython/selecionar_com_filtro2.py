from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like 'Max%'"

try:
    with nova_conexao() as conexao:
        try:
            datatable = conexao.cursor()
            datatable.execute(sql)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            for row in datatable:
                print(row)                    
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')            