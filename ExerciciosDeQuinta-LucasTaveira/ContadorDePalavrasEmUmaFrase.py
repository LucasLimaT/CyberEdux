def contar_palavras(texto):
    texto = texto.strip()
    texto = texto.split(" ")
    return len(texto)

while True:
    print("Numero de palavras na frase: ", contar_palavras(input("Escreva um texto: ")))

    continuar = input("\nDeseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break