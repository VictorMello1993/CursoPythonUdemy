#Select com input dos dados sem correr risco de SQL Injection
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome LIKE %s"

try:
    with nova_conexao() as conexao:
        try:
            entrada = input('Contato a localizar: ')
            args = (f'%{entrada}%',)
            datatable = conexao.cursor()
            datatable.execute(sql, args) #Passando as entradas geradas pelo usuário como parâmetro separadamente do comando SQL 
                                         #irá resolver o problema de risco de ataques de SQL Injection
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')        
        else:
            for row in datatable:
                print(row)                        
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')

