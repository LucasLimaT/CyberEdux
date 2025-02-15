def primo(n):
    raiz = int(n**0.5)
    if((n!=2) and ((n%2 == 0) or (n == 1))): 
        return False
    for i in range(3, raiz+1, 2):
        if(n % i == 0):
            return False
    return True

while True:
    n = int(input("Digite um numero: "))
    print("o numero", n, "é primo") if primo(n) == True else print("o numero", n, "não é primo")

    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break