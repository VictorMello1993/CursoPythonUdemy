from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

'''Criar tabela grupos de contatos (relação 1 para N, onde cada grupo possui uma lista de contatos, 
onde cada um deles pertece unicamente a um determinado grupo)'''

criar_tabela_grupo = """CREATE TABLE IF NOT EXISTS grupos(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            descricao VARCHAR(30)
                        )"""

# Adicionando uma nova coluna na tabela de contatos que irá representar a FK
alterar_tabela_contatos_1 = """ALTER TABLE contatos ADD grupo_id INT"""

# Criando FK para a tabela de contatos para relacionar com a tabela de grupos
alterar_tabela_contatos_2 = """ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
                             REFERENCES grupos(id)"""

try:
    with nova_conexao() as conexao:
        try:
            comando = conexao.cursor()
            comando.execute(criar_tabela_grupo)
            comando.execute(alterar_tabela_contatos_1)
            comando.execute(alterar_tabela_contatos_2)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print('DDL realizada com sucesso.')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')             


                                
