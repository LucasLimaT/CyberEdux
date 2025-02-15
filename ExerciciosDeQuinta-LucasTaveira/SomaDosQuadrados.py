def soma_dos_quadrados(n):
    soma = float(0)
    for i in range(1, n+1):
        soma += i**2
        print(soma)
    return soma

while True:
    n = int(input("Digite um numero: "))
    print("A soma dos quadrados de 1 a", n, "é =", soma_dos_quadrados(n))

    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break