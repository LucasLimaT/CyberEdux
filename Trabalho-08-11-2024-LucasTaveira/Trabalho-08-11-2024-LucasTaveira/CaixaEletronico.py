menu = (1)
contaExiste = bool(False)
saldo = float(0)
deposito = float(0)
sacar = float(0)
while 4 > menu and menu > 0:
    if contaExiste == False:
        print("Cadastro:")
        usuario = input("Usuario: ").strip()
        senha = input("Senha: ").strip()
        contaExiste = True
    else:
        menu = int(input("\nEscolha uma das seguintes opcoes:\n[1] Depositar\n[2] Sacar\n[3] Consultar Saldo\n[4] Sair\n"))
        if menu == 1:
            while deposito <= 0:
                deposito = float(input("\nQuantidade que deseja depositar: R$"))
            if usuario == input("\nDigite seu nome de usuario: ") and senha == input("Digite sua senha: "):
                saldo += deposito
                print("Operacao realizada com sucesso!")
            else:
                print("Usuario ou senha incorretos!")
        elif menu == 2:
            sacar = float(input("Quantidade que deseja sacar: R$"))
            if sacar > saldo:
                print("Saldo insuficiente!")
            else:
                if usuario == input("\nDigite seu nome de usuario: ") and senha == input("Digite sua senha: "):
                    saldo -= sacar
                    print("Operacao realizada com sucesso!")
                else:
                    print("Usuario ou senha incorretos!")
        elif menu == 3:
            if usuario == input("\nDigite seu nome de usuario: ") and senha == input("Digite sua senha: "):
                print("\nSeu saldo atual é de: R$", saldo, "\n")
            else:
                print("Usuario ou senha incorretos!")