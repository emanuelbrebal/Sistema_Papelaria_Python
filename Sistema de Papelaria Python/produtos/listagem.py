def listaProdutos(produtos): 
    print("\nTela de Visualização de Produtos")
    
    index = 0
    for produto in produtos:
        print("Produto ", index)
        print("Nome: ", produto["nome"])
        print("Preco: ", produto["preco"],"\n")
        print("-------------------")
        index += 1