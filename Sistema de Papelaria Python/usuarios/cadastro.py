def cadastraUsuario(cadastro):
    print("\n---Tela de cadastro de novos usuários---")

    nome=str(input("Digite seu nome: "))
    telefone=int(input("Digite seu telefone: "))
    email=str(input("Digite seu e-mail: " ))
    senha=str(input("Digite sua senha: " ))

    cadastro.append({
        'nome':nome,
        'telefone':telefone,
        'email':email,
        'senha':senha
    })
    return cadastro