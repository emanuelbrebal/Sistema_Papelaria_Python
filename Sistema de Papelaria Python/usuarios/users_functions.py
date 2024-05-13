import sqlite3

#estabelece a conexão com o banco de dados
conexao = sqlite3.connect('papelaria_db.sqlite')
#cria o cursor, o intermédio entre o código e o banco de dados
cursor = conexao.cursor()

#CREATE USER
def insert_user(email, password):
    cursor.execute("""
        INSERT INTO users(email, password) VALUES (?, ?)
    """, [email, password])
    conexao.commit()

#UTILIZAR PARA ALIMENTAR A FUNÇÃO E CHAMAR NO ARQUIVO MAIN
new_email = str(input("Digite seu email: "))
new_password = str(input("Digite sua senha: "))
insert_user(new_email, new_password)

#READ USER
def list_user():
    all_users = cursor.execute("""
        SELECT email FROM users
    """).fetchall()
    print(all_users)

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE LISTAR USUÁRIOS
list_user()

#READ USER BY ID
def list_user_ByID(user_ID):
    users_ByID= cursor.execute("""
        SELECT email FROM users WHERE user_ID = ?
    """, [user_ID]).fetchone()
    print(users_ByID)

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE LISTAR USUÁRIOS
new_ID = int(input("Digite o ID do usuário: "))
list_user_ByID(new_ID)

#FUNÇÃO RESPONSÁVEL PELO LOGIN
def login(email, password):
    sql = "SELECT * FROM users WHERE password = ? AND password = ?"
    return cursor.execute(sql, [email, password]).fetchone()