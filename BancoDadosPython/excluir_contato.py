#Excluindo registros
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

#Excluindo os contatos cujo nome começa com 'Vic' e que tenham telefones duplicados, sobrando apenas o primeiro registro
#------------------------------------------------------------------------------------------------------------------------------------------
sql = """DELETE FROM contatos C1
         WHERE C1.id > (SELECT C2.id FROM (SELECT id FROM contatos)C2 LIMIT 1)
         AND C1.nome LIKE %s"""

# sql = """DELETE FROM contatos
#          WHERE id > (SELECT id FROM contatos WHERE nome LIKE %s LIMIT 1)"""   
# 1093 (HY000): You can't specify target table 'contatos' for update in FROM clause

try:
    with nova_conexao() as conexao:
        try:                
            datatable = conexao.cursor()
            datatable.execute(sql, ('Vic%',)) #Evitando SQL Injection
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print(f'{datatable.rowcount} registro(s) excluído(s).')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')            
#------------------------------------------------------------------------------------------------------------------------------------------





