def autenticacao(cadastro): 
    print("\n---Tela de login para usuários---")

    login = str(input("Digite seu e-mail de login: "))

    emails = [email['email'] for email in cadastro]

    try:
        index = emails.index(login)
    except:
        print("Usuario nao cadastrado")
        return

    senhaCorrespondente = cadastro[index]['senha']

    tentativaSenha = str(input("Digite sua senha: "))

    if tentativaSenha == senhaCorrespondente:
        print("\nAcesso liberado.\nSeja bem vindo(a)")
    else:
        print("\nAcesso negado. Encerrando o sistema.")

    return tentativaSenha == senhaCorrespondente
