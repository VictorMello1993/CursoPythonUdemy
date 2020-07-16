# Consultas com JOINs

from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
        SELECT 
            g.descricao AS grupo,
            c.nome AS nome
        FROM contatos c
        INNER JOIN grupos g ON c.grupo_id = g.id
        ORDER BY grupo, nome
        """

try:
    with nova_conexao() as conexao:
        try:
            comando = conexao.cursor(dictionary=True) #Esse parâmetro indica que o result set do select será representado por um dicionário
                                                    #em vez de ser uma tupla
            comando.execute(sql)
            contatos = comando.fetchall()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            for contato in contatos:
                print(f'{contato["grupo"]}: {contato["nome"]}') #Com isso, é possível acessar as colunas através das chaves que são representadas pelos alias do select 
                                                                #em vez de ser pelos índices que são acessíveis em uma tupla.
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')
                