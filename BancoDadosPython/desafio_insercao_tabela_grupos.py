#Desafio: inserir dados na tabela de grupos

from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

inserir_grupos = """
                    INSERT INTO grupos (descricao)
                    VALUES(%s)                    
                    """

args = (('Trabalho',),
        ('Futebol',),
        ('Bird Memes',),
        ('Periféricos High-End',),
        ('Maternal',),
        ('Família Buscapé',),
        ('Hey Sisters',),
        ('Blood Brothers',),)

try:
    with nova_conexao() as conexao:
        try:
            comando = conexao.cursor()
            comando.executemany(inserir_grupos, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print(f'{comando.rowcount} registro(s) criado(s).')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')            
