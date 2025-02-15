def potencia(base, expoente):
    soma = float(1)
    if expoente == 0: return 1
    for i in range(1, expoente+1): soma *= base
    return soma

while True:
    print("O resultado será:", potencia(float(input("Digite a base: ")), int(input("Digite o expoente: "))))
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break