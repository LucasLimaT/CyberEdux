produtos = list()

while True:
    menu = input("Selecione uma das seguintes opcoes:\n[1] Adicionar\n[2] Listar\n[3] Remover\n[4] Atualizar quantidades\n[5] Consultar estoque\n[6] Sair\n")
    if menu == "1":   
        produtos.append(
            {
                "nome": input("Nome do produto: "),
                "quantidade": input("Estoque: "),
                "preco": input("Preco: ")
            }
        )
    elif menu == "2":
        for produto in produtos:
            print(f"Nome: {produto["nome"]}")
            print(f"Estoque: {produto["quantidade"]}")
            print(f"Preco: {produto["preco"]}\n")
    elif menu == "3":
        seleciona = None
        remover = input("Digite o nome do produto que deseja remover: ")
        try:
            for produto in produtos:
                if produto["nome"] == remover:
                    produtos.remove(produto)
            print(f"{remover} removido com sucesso!")
        except:
            print("Erro ao remover!")
    elif menu == 4:
        produto_nome = input("Digite o nome do produto que deseja alterar o estoque: ")
        produto_nova_quantidade = input("Digite o novo estoque disponivel: ")
        try:
            for produto in produtos:
                if produto["nome"] == produto_nome:
                    produto["quantidade"] = produto_nova_quantidade
            print(f"Estoque alterado com sucesso!")
        except:
            print("Erro ao mudar estoque!")
    elif menu == 5:
        produto_nome = input("Digite o nome do produto que deseja consultar o estoque: ")
        try:
            for produto in produtos:
                if produto["nome"] == produto_nome:
                    print(f"Produto: {produto["nome"]}\nEstoque: {produto["quantidade"]}")
        except:
            print("Erro ao consultar estoque!")
    elif menu == 6:
        break