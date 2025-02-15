import Somas

while True:
    menu = input("O que deseja fazer:\n[1] Soma\n[2] Subtracao\n[3] Multiplicacao\n[4] Divisao\n[5] Potenciacao\n[6] Raiz Quadrada\n[7] Sair\n")
    if menu == '1':
        soma = Somas.mais(float(input("Digite o primeiro numero: ")), float(input("Digite o segundo numero: ")))
        print("\nO resultado é:", soma)
    elif menu == '2':
        subtracao = Somas.subtracao(float(input("Digite o primeiro numero: ")), float(input("Digite o segundo numero: ")))
        print("\nO resultado é:", subtracao)
    elif menu == '3':
        multiplicacao = Somas.multiplica(float(input("Digite o primeiro numero: ")), float(input("Digite o segundo numero: ")))
        print("\nO resultado é:", multiplicacao)
    elif menu == '4':
        divisao = Somas.divisao(float(input("Forneca o dividendo: ")), float(input("Forneca o divisor: ")))
        if divisao == "Erro, impossivel fazer divisao por 0!":
            print(divisao)
        else:
            print("\nO resultado é:", divisao)
    elif menu == '5':
        potencia = Somas.potencia(float(input("Digite a base: ")), float(input("Digite o expoente: ")))
        print("\nO resultado é:", potencia)
    elif menu == '6':
        raiz = Somas.raiz(int(input("Forneca um numero inteiro que queira achar a raiz: ")))
        print("\nO resultado é:", raiz)
    elif menu == '7':
        break
    else:
        print("\nOpcao Invalida!")