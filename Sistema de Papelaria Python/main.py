import sqlite3
from usuarios.users_functions import insert_user, login

#estabelece a conexão com o banco de dados
conexao = sqlite3.connect('papelaria_db.sqlite')
#cria o cursor, o intermédio entre o código e o banco de dados
cursor = conexao.cursor()


#fazer o menu com todas as opções
while(True):
    print("""
        1- Cadastrar Usuario
        2- Entrar no Sistema
    """)
    opc = int(input("Digite a oção: "))
    if opc == 1:
        username = str(input("Digite o email: "))
        password = str(input("Digite a senha: "))
        insert_user(username, password)
    
    elif opc == 2:
        username = str(input("Digite o email: "))
        password = str(input("Digite a senha: "))
        autenticado = login(username, password)
        if autenticado:
            print(autenticado)
            break
        