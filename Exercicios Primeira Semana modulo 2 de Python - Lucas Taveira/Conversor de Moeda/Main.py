import Conversor

try:
    while True:
        print("Converter de:")
        opcoes = input(f"1. Real\n2. Dolar\n3. Euro\n4. Sair\n")
        if opcoes == "1":
            valor = float(input("\n\nValor em reais: "))
            print("Para:")
            opcoes = input(f"1. Dolar\n2. Euro\n")
            if opcoes == "1":
                Conversor.conversor_real_dolar(valor)
            elif opcoes == "2":
                Conversor.conversor_real_euro(valor)
            else:
                print("Opção Invalida")
        elif opcoes == "2":
            valor = float(input("\n\nValor em dolars: "))
            print("Para:")
            opcoes = input(f"1. Real\n2. Euro\n")
            if opcoes == "1":
                Conversor.conversor_dolar_real(valor)
            elif opcoes == "2":
                Conversor.conversor_dolar_euro(valor)
            else:
                print("Opção Invalida")
        elif opcoes == "3":
            valor = float(input("\n\nValor em euro: "))
            print("Para:")
            opcoes = input(f"1. Real\n2. Dolar\n")
            if opcoes == "1":
                Conversor.conversor_euro_real(valor)
            elif opcoes == "2":
                Conversor.conversor_euro_dolar(valor)
            else:
                print("Opção Invalida")
        elif opcoes == "4":
            break
        else:
            print("Opção Invalida")
except:
    print("Algo deu errado na conversão da moeda!")