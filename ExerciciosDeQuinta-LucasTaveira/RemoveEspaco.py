def remove_espaco(texto):
    return texto.replace(" ","")

while True:
    print(remove_espaco(input("Escreva um texto: ")))
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break