from bd import nova_conexao
from mysql.connector import ProgrammingError

#Criando a tabela 'contatos'
tabela_contatos = """
CREATE TABLE contatos(
    nome VARCHAR(50), 
    tel VARCHAR(40)
    )
"""

#Criando a tabela 'emails'
tabela_emails = """
    CREATE TABLE emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

#Tratando erros de conexão com banco de dados DENTRO do módulo 'criar_tabela'
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')

#Tratando erros que ocorrem na conexão FORA do módulo 'criar_tabela'
# with nova_conexao() as (conexao, erro):
#     try:
#         cursor = conexao.cursor()
#         cursor.execute(tabela_contatos)
#         cursor.execute(tabela_emails)
#     except ProgrammingError as e:
#         print(f'Erro: {e.msg}')

    
    