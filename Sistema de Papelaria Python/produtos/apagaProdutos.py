def apagaProdutos(produtos):
    print("\n---Tela de apagar produtos---")
    indice = int(input("Digite o indice do produto que deseja apagar: "))
    
    if indice >= len(produtos):
        print("Produto nao encontrado")
        return
    
    if indice < 0:
        print("Produto invalido")
        return
    
    produto = produtos[indice]
    
    print("Apagado o produto: ", indice)
    print("Nome: ", produto["nome"])
    print("Preco: R$", produto["preco"],"\n")
    
    produtos = produtos.remove(produto)