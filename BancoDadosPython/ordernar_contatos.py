#Order by
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos ORDER BY nome'

try:
    with nova_conexao() as conexao:
        try:
            datatable = conexao.cursor()
            datatable.execute(sql)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:                                         
            print('\n'.join(str(row) for row in datatable))
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')            