def contar_caracteres(texto, caracter):
    texto = texto.strip()
    texto = texto.split(caracter)
    return len(texto)-1

while True:
    texto = input("Escreva um texto: ").upper()
    print("Numero de letras na frase: ", contar_caracteres(texto, input("Qual caracter deseja contar: ").upper()))

    continuar = input("\nDeseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break