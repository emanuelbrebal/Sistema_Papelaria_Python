import sqlite3
from usuarios.users_functions import insert_user, login, list_user, list_user_ByID

#estabelece a conexão com o banco de dados
conexao = sqlite3.connect('papelaria_db.sqlite')
#cria o cursor, o intermédio entre o código e o banco de dados
cursor = conexao.cursor()


#fazer o menu com todas as opções
while(True):
    print("""
        1- Cadastrar Usuario
        2- Realizar o login 
        3- Mostrar todos os Usuários
        4- Mostrar Usuário por ID 
    """)
    opc = int(input("Digite a oção: "))
    if opc == 1: #cadastro de usuarios
        username = str(input("Digite o username: "))
        password = str(input("Digite a senha: "))
        insert_user(username, password)
    
    elif opc == 2: # entrar no sistema
        username = str(input("Digite o username: "))
        password = str(input("Digite a senha: "))
        autenticado = login(username, password)
        if autenticado:
            print("Usuário autenticado")
            break
        else:
            print("Usuário ou senha incorreto(s), por favor tente novamente.")

    elif opc == 3: #mostrar todos os usuários
        list_user()

    elif opc == 4: #mostrar usuário por ID
        new_ID = int(input("Digite o ID do usuário: "))
        list_user_ByID(new_ID)
        