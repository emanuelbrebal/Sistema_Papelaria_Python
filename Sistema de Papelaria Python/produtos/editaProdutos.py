def editaProdutos(produtos):
    print("\n---Tela de edicao de produtos---")
    indice = int(input("\nDigite o codigo do produto que deseja editar: "))
    
    if indice >= len(produtos):
        print("\nProduto nao encontrado")
        return
    
    if indice < 0:
        print("\nProduto invalido")
        return
    
    
    
    produto = produtos[indice]
    
    print("Produto: ", indice)
    print("Nome: ", produto["nome"])
    print("Preco: ", produto["preco"],"\n")
    
    nomeproduto=str(input("Digite o novo nome do produto: "))
    precoproduto=float(input("Digite o seu novo preco: "))
    
    novoProduto = {
        'nome': nomeproduto,
        'preco': precoproduto,
    }
    
    produtos[indice] = novoProduto