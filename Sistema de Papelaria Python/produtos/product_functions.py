import sqlite3

conexao = sqlite3.connect('papelaria_db.sqlite')

cursor = conexao.cursor()

#CREATE PRODUCT
def insert_product(name, price):
    cursor.execute("""
        INSERT INTO products(name, price) VALUES (?, ?)
    """, [name, price])
    conexao.commit()

#UTILIZAR PARA ALIMENTAR A FUNÇÃO E CHAMAR NO ARQUIVO MAIN
new_product = str(input("Digite seu email: "))
new_price = float(input("Digite sua senha: "))
insert_product(new_product, new_price)

#READ PRODUCT
def list_products():
    all_products = cursor.execute("""
        SELECT * FROM products
    """).fetchall()
    print(all_products)

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE LISTAR PRODUTOS 
list_products()

#READ USER BY ID
def list_products_ByID(user_ID):
    products_ByID= cursor.execute("""
        SELECT * FROM products WHERE prod_ID = ?
    """, [user_ID]).fetchone()
    print(products_ByID)

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE LISTAR USUÁRIOS
new_ID = int(input("Digite o ID do produto: "))
list_products_ByID(new_ID)