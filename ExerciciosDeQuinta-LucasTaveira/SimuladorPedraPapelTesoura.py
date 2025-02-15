def pedra_papel_tesoura(jogador1, jogador2):
    if (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
        return "jogador 2 ganhou"
    elif jogador1 == jogador2:
        return "Jogo empatou"
    return "jogador 1 ganhou"
    
while True:
    while True:
        jogador1 = int(input("Vez do jogador 1:\nEscolha uma dessas opcoes:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n"))
        if jogador1 > 0 and jogador1 < 4: break
    while True:
        jogador2 = int(input("Vez do jogador 2:\nEscolha uma dessas opcoes:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n"))
        if jogador2 > 0 and jogador2 < 4: break
    print(f"O {pedra_papel_tesoura(jogador1, jogador2)}")
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break