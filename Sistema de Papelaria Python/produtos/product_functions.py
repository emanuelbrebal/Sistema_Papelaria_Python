import sqlite3

conexao = sqlite3.connect('papelaria_db.sqlite')

cursor = conexao.cursor()

#CREATE PRODUCT
def insert_product(name, price):
    cursor.execute("""
        INSERT INTO products(prod_name, prod_price) VALUES (?, ?)
    """, [name, price])
    conexao.commit()

#UTILIZAR PARA ALIMENTAR A FUNÇÃO E CHAMAR NO ARQUIVO MAIN
#new_product = str(input("Digite seu email: "))
#new_price = float(input("Digite sua senha: "))
#insert_product(new_product, new_price)

#READ PRODUCT
def list_products():
    all_products = cursor.execute("""
        SELECT * FROM products
    """).fetchall()
    print(all_products)

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE LISTAR PRODUTOS 
#list_products()

#READ USER BY ID
def list_products_ByID(prod_ID):
    products_ByID= cursor.execute("""
        SELECT * FROM products WHERE prod_ID = ?
    """, [prod_ID]).fetchone()
    print(products_ByID)

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE LISTAR PRODUTOS
#new_ID = int(input("Digite o ID do produto que deseja visualizar: "))
#list_products_ByID(new_ID)

#UPDATE PRODUCTS BY ID
def update_product_ByID(prod_name, prod_price, prod_ID):
    new_product = cursor.execute("""
        UPDATE products SET prod_name = ?, prod_price = ? WHERE prod_ID = ?
    """, [prod_name, prod_price, prod_ID])
    conexao.commit()
    print(new_product)
    list_products()

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE ATUALIZAR PRODUTOS PELO ID
#new_ID = int(input("Digite o ID do produto que deseja alterar: ")) 
#new_name = str(input("Digite o novo nome do produto: "))  
#new_price = int(input("Digite o novo preço do produto: "))  
#update_product_ByID(new_name, new_price, new_ID)