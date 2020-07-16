# Consultas com JOINs (versão 2)

from mysql.connector.errors import ProgrammingError
from bd import nova_conexao
from collections import defaultdict

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
            cursor = conexao.cursor(dictionary=True)        
            try:
                cursor.execute(sql)
                contatos = cursor.fetchall()
            finally:
                cursor.close()            
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')            
        else:
            agrupados = defaultdict(list) #Criando uma lista onde cada elemento possui um valor aleatório para uma chave
            for contato in contatos:                
                agrupados[contato['grupo']].append(contato['nome'])
            print(agrupados)            
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')            