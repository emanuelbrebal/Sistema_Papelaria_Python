def cadastraProdutos(produtos):
    print("\n---Tela de cadastro de produtos---")
    nomeproduto=str(input("Digite o nome do produto: "))
    precoproduto=float(input("Digite o seu preço: "))
    
    novoProduto = {
        'nome': nomeproduto,
        'preco': precoproduto,
    }

    produtos.append(novoProduto)
    print("\n")
    print(novoProduto)

    return produtos