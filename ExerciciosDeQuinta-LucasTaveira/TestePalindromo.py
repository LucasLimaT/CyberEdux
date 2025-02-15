def teste_Palindromo(texto):
    if texto[::-1] == texto:
        print("A palavra é palindromo!")
    else:
        print("A palavra não é palindromo!")

while True:
    teste_Palindromo(input("Escreva uma palavras: "))
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break