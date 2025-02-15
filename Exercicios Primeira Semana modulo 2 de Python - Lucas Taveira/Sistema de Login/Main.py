from Cadastro import cadastro
contas = []

def login(contas):
    while True:
        opcao = input(f"\n[1] Login\n[2] Cadastro\n")
        if opcao == "1":
            print("Login")
            usuario = input("Usuario: ").strip()
            senha = input("Senha: ").strip()
            for conta in contas:
                if conta["usuario"] == usuario and conta["senha"] == senha:
                    print(f"Bem-vindo(a), {conta["nome"]}!")
                    return conta
            print("\nUsuario ou senha incorretos!")
        elif opcao == "2":
            conta = cadastro(contas)
            contas.append(conta)

login(contas)
