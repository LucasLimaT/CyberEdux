from Ranking import adicionar_jogador, encontrar_jogador, mostrar_ranking, mudar_pontuacao
jogadores = []

def menu(jogadores):
    while True:
        opcao = input(f"\n1. Mostrar ranking\n2. Adicionar novo jogador\n3. Mudar pontuação de jogador\n4. Procurar jogador\n5. Sair\n")
        if opcao == "1":
            mostrar_ranking(jogadores)
        elif opcao == "2":
            jogador = adicionar_jogador(jogadores)
            jogadores.append(jogador)
        elif opcao == "3":
            mudar_pontuacao(jogadores)
        elif opcao == "4":
            try:
                nome = input("\nNome do jogador que deseja procurar: ")
                jogador = encontrar_jogador(jogadores, nome)
                print(" _"*39)
                print("|\tjogador\t|\tpontuacao\t|")
                print(" ="*39)
                print(f"|\t{jogador["nome"]}\t|\t{jogador["pontuacao"]} pontos\t|")
                print(" ="*39)
            except:
                print("Erro ao procurar jogador!")
        elif opcao == "5":
            break
        else:
            print("Opcão Invalida!")

menu(jogadores)