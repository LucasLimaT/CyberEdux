def adicionarContatos(telefones, nomes, grupos):
    nome = input("\nDigite o nome do contato: ")
    while True:
        telefone = input(f"\nDigite o telefone do(a) {nome}:\nformato: (xx) xxxxx-xxxx\n")
        tamanhoTelefone = len(telefone)
        if telefone[0] == '(':
            for i in range(1, 3):
                telefone[i].isdigit()