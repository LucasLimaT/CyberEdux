def par_impar(numero):
    if numero % 2 == 0:
        return True
    return False

while True:
    n = int(input("Digite um numero: "))
    print("o numero", n, "é par") if par_impar(n) == True else print("o numero", n, "é impar")

    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break