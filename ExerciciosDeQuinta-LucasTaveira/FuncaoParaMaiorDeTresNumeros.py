def tresNumeros(n1, n2, n3):
    if n1 > n2 and n2 >= n3:
        return n1
    elif n2 > n3 and n3 >= n1:
        return n2
    elif n3 > n2 and n2 >= n1:
        return n3
    return n1

while True:
    print("O maior numero fornecido é:", tresNumeros(float(input("Digite o primeiro numero: ")), float(input("Digite o segundo numero: ")), float(input("Digite o segundo numero: "))))
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break