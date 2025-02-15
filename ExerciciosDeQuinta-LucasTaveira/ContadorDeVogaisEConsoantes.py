def contar_letras(texto):
    tamTexto = len(texto)
    vogais = int(0)
    consoantes = int(0)
    texto = texto.upper()
    for i in range(tamTexto):
        if texto[i] == "A" or texto[i] == "E" or texto[i] == "I" or texto[i] == "O" or texto[i] == "U":
            vogais += 1
        elif texto[i].isalpha(): 
            consoantes += 1
    return vogais, consoantes

while True:
    vogais, consoantes = contar_letras(input("Escreva um texto: "))
    print("\nQuantidade de vogais: ", vogais, "\nQuantidade de consoantes: ", consoantes)
    continuar = input("\nDeseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break