import sqlite3
from usuarios.users_functions import insert_user, login, list_user, list_user_ByID
from produtos.product_functions import list_products, list_products_ByID, insert_product, update_product_ByID

#estabelece a conexão com o banco de dados
conexao = sqlite3.connect('papelaria_db.sqlite')
#cria o cursor, o intermédio entre o código e o banco de dados
cursor = conexao.cursor()


#fazer o menu com todas as opções
while(True):
    print("""
        1- Cadastrar Usuario
        2- Realizar o login 
          --- ABA DOS USUÁRIOS ---
        3- Mostrar todos os Usuários
        4- Mostrar Usuário por ID 
        5- Atualizar Username WIP
        6- Atualizar Password WIP
        7- Excluir Usuário WIP
          --- ABA DOS PRODUTOS ---
        8- Cadastrar Produto
        9- Mostrar todos os Produtos
        10- Mostrar Produto por ID
        11- Atualizar Produto por ID
        12- Excluir Produto WIP
          
        0- Encerrar programa
          
    """)
    opc = int(input("Digite a opção: "))
    if opc == 1: #cadastro de usuarios
        username = str(input("Digite o username: "))
        password = str(input("Digite a senha: "))
        insert_user(username, password)
    
    elif opc == 2: #entrar no sistema
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
        new_ID = int(input("Digite o ID do usuário que quer visualizar: "))
        list_user_ByID(new_ID)

    elif opc == 8: #Cadastrar Produto
        new_product = str(input("Digite o nome do produto: "))
        new_price = float(input("Digite o preço do produto: "))
        insert_product(new_product, new_price)

    elif opc == 9: #Mostrar todos os produtos
        list_products()
    
    elif opc == 10: #Mostrar produto por ID
        new_ID = int(input("Digite o ID do produto que quer visualizar: "))
        list_products_ByID(new_ID)

    elif opc == 11: #Atualizar produto por ID
        list_products()
        new_ID = int(input("Digite o ID do produto que deseja alterar: ")) 
        new_name = str(input("Digite o novo nome do produto: "))  
        new_price = int(input("Digite o novo preço do produto: "))  
        update_product_ByID(new_name, new_price, new_ID)
        
    
    elif opc == 0:
        break

    else:
        print("Entrada Inválida. Tente novamente.")