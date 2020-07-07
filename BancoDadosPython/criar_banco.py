#Criando um esquema de banco de dados em Python

from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    password='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
)

cursor = conexao.cursor()

# CREATE DATABASE IF NOT EXISTS agenda
cursor.execute('CREATE DATABASE agenda') #Criando o esquema 'agenda'


