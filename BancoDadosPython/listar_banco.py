from mysql.connector import connect

conexao = connect(
   host = 'localhost',
   port=3306,
   user='root',
   password='@211993vsm'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

#Listando todas as bases de dados criados
for i, database in enumerate(cursor, start=1):
    print(f'Banco de dados {i}: {database[0]}')