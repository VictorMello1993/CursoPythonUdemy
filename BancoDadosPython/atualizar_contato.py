from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """UPDATE contatos 
        SET nome = %s
        WHERE id = %s"""

try:
    with nova_conexao() as conexao:
        try:
            datatable = conexao.cursor()
            datatable.execute(sql, ('Pedro', 49))
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')        
        else:
            print(f'{datatable.rowcount} registro(s) alterado(s).')                
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')
