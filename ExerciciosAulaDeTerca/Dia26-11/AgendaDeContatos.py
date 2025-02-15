from ManipulacaoContatos import adicionarContatos

grupos = list()
telefones = list()
nomes = list()

while True:
    opcoes = input("[1] Adicionar contato\n[2] Buscar Nome\n[3] Buscar Telefone\n[4] Criar novo grupo")
    if opcoes == 1:
        if len(grupos) != 0:
            contatos = adicionarContatos(contatos, grupos)