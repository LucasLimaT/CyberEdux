frase = input("Escreva uma frase: ")
fraseSemEspaco = frase.replace(" ", "")
print("True, todos os caracteres sao numeros") if fraseSemEspaco.isdigit() else print("False, nem todos os caracteres sao numeros")
print("\n\n*desconsiderando espacos!!!")