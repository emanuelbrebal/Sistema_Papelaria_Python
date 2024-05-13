import sqlite3

#estabelece a conexão com o banco de dados
conexao = sqlite3.connect('papelaria_db.sqlite')
#cria o cursor, o intermédio entre o código e o banco de dados
cursor = conexao.cursor()

#CRIA A TABELA DE USUÁRIOS NO SQLITE
def create_table_user():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        user_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        username varchar(255) NOT NULL,
        password varchar(255) NOT NULL
        );
    """)
    
#CRIA A TABELA DE PRODUTOS NO SQLITE   
def create_table_prod():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
        prod_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        prod_name VARCHAR(255) NOT NULL UNIQUE,
        prod_price INTEGER(255) NOT NULL
        );
    """)

create_table_user()
create_table_prod()