cambio = {"USD": 6.06, "EURO": 6.38}
menu = input("Você deseja converter para?\n[1] DOLAR\t[2] EURO\n")
reais = float(input("Forneca o valor em reais que deseja converter: "))
if menu == "1":
    convertido = reais/cambio.get("USD")
    print(f"Valor convertido: {convertido}")
elif menu == "2":
    convertido = reais/cambio.get("EURO")
    print(f"Valor convertido: {convertido}")
else:
    print("Opcao Invalida!")