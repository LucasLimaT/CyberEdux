def adicionar_jogador(jogadores):
    print("\n\tCADASTRO DE JOGADOR")
    while True:
        nome = str(input("Nome completo: ")).strip().lower()
        nome = nome.capitalize()
        if not encontrar_jogador(jogadores, nome):
            break
        print("\nJogador já cadastrado!")
    jogador = {
            "nome": nome,
            "pontuacao": 0
            }
    return jogador

def encontrar_jogador(jogadores, nome):
    try:
        for jogador in jogadores:
            if jogador["nome"] == nome:
                return jogador
        return None
    except Exception as e:
        print("Erro ao procurar jogador", e)

def mudar_pontuacao(jogadores):
    try:
        nome = input("Nome do jogador que deseja procurar: ")
        jogador = encontrar_jogador(jogadores, nome)
        if not jogador:
            print("Jogador não encontrado!")
            return
        nova_pontuacao = float(input(f"Nova pontuação do {nome}: "))
        jogador["pontuacao"] = nova_pontuacao
        atualiza_dados(jogadores, jogador)
    except:
        print("Erro ao mudar pontuação")

def mostrar_ranking(jogadores):
    print("\n\tRANKING DOS JOGADORES")
    jogadores_ordenados = sorted(jogadores, key=lambda x: x["pontuacao"], reverse=True)
    if not jogadores_ordenados:
        print("\tNenhum jogador cadastrado.")
        return
    print("_"*65)
    print("|\tColocação\t|\tjogador\t|\tpontuacao\t|")
    print("="*65)
    for i, jogador in enumerate(jogadores_ordenados, start=1):
        print(f"|\t{i}º\t\t|\t{jogador["nome"]}\t|\t{jogador["pontuacao"]} pontos\t|")
    print("="*65)

def atualiza_dados(jogadores, jogador): 
    for i in jogadores:
        if i["nome"] == jogador["nome"]:
            pos = jogadores.index(i)
            jogadores[pos] = jogador
            break
    return