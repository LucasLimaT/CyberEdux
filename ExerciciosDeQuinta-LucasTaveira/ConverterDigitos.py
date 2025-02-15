def contar_digitos(numero):
    quantidade_numeros = int(0)
    for i in range(len(numero)):
        if numero[i].isdigit() : quantidade_numeros += 1
    return quantidade_numeros

while True:
    print("A quantidade de digitos é:", contar_digitos(input("Digite um numero: ")))
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break