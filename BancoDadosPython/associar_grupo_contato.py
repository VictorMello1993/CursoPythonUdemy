# Relacionando contatos com um grupos

from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

select_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
update_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
'Victor' : 'Maternal',
'Camilla' : 'Maternal',
'Pedro' : 'Maternal',
'Maxuel' : 'Família Buscapé',
'Vanderson' : 'Futebol',
'Humberto' : 'Futebol',
}

try:
    with nova_conexao() as conexao:
        try:
            comando = conexao.cursor()
            for contato, grupo in contato_grupo.items():
                comando.execute(select_grupo, (grupo,))
                grupo_id = comando.fetchone()[0]
                comando.execute(update_contato, (grupo_id, contato))
                conexao.commit()                
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')                    
        else:
            print(f'{len(contato_grupo)} contato(s) alterado(s).')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')