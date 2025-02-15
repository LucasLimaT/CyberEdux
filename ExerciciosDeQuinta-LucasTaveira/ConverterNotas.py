def contar_numeros(real, dolar, euro):
    return (real / dolar), (real / euro)

while True:
    real = float(input("Digite um valor em reais: "))
    dolar, euro = contar_numeros(real, float(input("Valor atual do dolar: ")), float(input("Valor atual do euro: ")))
    print(f"O valor fornecido convertido dolar é: ${dolar:.2f}\nO valor fornecido convertido do euros é: €{euro:.2f}")

    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break