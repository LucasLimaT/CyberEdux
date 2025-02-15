menu = int(1)
vitorias = int(0)
derrotas = int(0)
empates = int(0)

import random

while int(4) > menu and menu > int(-1):
    opcaoComputador = random.randint(1, 3)
    menu = int(input("Escolha uma das opcoes abaixo:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n[4] encerrar jogo\n"))
    if menu == 1:
        print("\nVocê escolheu pedra")
    elif menu == 2: 
        print("\nVocê escolheu papel")
    elif menu == 3:
        print("\nVocê escolheu tesoura")
    if opcaoComputador == 1:
        print("\nO computador escolheu pedra")
    elif opcaoComputador == 2:
        print("\nO computador escolheu papel")
    elif opcaoComputador == 3:
        print("\nO computador escolheu tesoura")
    if (menu == 1 and opcaoComputador == 2) or (menu == 2 and opcaoComputador == 3) or (menu == 3 and opcaoComputador == 1):
        print("\nVocê perdeu")
        derrotas += 1
    elif (menu == opcaoComputador):
        print("\nEmpatou")
        empates += 1
    else:
        print("\nVocê ganhou")
        vitorias += 1
    print(f"\n----------------------\nPlacar:\n----------------------\nVitorias: {vitorias}\nEmpates: {empates}\nDerrotas: {derrotas}\n----------------------")
        