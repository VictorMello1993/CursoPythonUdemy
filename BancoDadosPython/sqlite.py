# Banco de dados usando SQLite

from sqlite3 import connect, ProgrammingError, Row

tabela_grupo = 'CREATE TABLE IF NOT EXISTS grupos (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao VARCHAR(30))'

tabela_contatos = """CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50),
    tel INTEGER,
    grupo_id INTEGER)
    """
insert_grupos = 'INSERT INTO grupos (descricao) VALUES (?)'
select_grupos = 'SELECT id, descricao FROM grupos'
insert_contatos = 'INSERT INTO contatos (nome, tel, grupo_id) VALUES (?, ?, ?)'

select_contatos = """SELECT G.descricao AS grupo, 
                            C.nome AS contato 
                            FROM contatos C
                            INNER JOIN grupos G ON C.grupo_id = G.id
                            ORDER BY grupo, contato"""
try:
    conexao = connect(':memory:') #Conectando ao SQLite num banco de dados em memória
    conexao.row_factory = Row #Instanciando uma factory responsável pela tranformação do result set que seria uma tupla em um dicionário
    cursor = conexao.cursor()
    cursor.execute(tabela_grupo)
    cursor.execute(tabela_contatos)
    cursor.executemany(insert_grupos, (('Casa',), ('Trabalho',)))
    cursor.execute(select_grupos)
    grupos = {row['descricao']: row['id'] for row in cursor.fetchall()}

    contatos = (
        ('Arthur', 456, grupos['Casa']),
        ('Paulo', 789, grupos['Casa']),
        ('Ângelo', 000, grupos['Trabalho']),
        ('Eduardo', 987, None),
        ('Yuri', 654, None),
        ('Leonardo', 321, None),
    )

    cursor.executemany(insert_contatos, contatos)
    cursor.execute(select_contatos)

    for contato in cursor:
        print(contato['contato'], contato['grupo'])        
except ProgrammingError as e:
    print(f'Erro: {e.msg}')
