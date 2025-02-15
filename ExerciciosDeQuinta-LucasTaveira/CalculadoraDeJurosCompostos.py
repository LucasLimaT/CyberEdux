def calcular_juros_compostos(capitalInicial, taxaDeJuros, periodos):
    return float(capitalInicial)*(1+float(taxaDeJuros)/100)**int(periodos)

while True:
    print(calcular_juros_compostos(input("Digite o capital inicial: "), input("Digite a taxa de juros (em porcentagem): "), input("Digite o numero de periodos: ")))
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break