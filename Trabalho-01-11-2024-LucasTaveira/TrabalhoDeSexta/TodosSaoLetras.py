frase = input("Escreva uma frase: ")
fraseSemEspaco = frase.replace(" ", "")
print("True, todos os caracteres sao letras") if fraseSemEspaco.isalpha() else print("False, nem todos os caracteres sao letras")
print("\n\n*desconsiderando espacos!!!")