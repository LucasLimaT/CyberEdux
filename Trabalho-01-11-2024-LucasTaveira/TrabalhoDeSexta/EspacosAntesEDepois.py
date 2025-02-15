frase = input("Escreva uma frase com espaços antes e depois dela: ")
removeEspacos = frase.strip()
print("Frase Normal:\n  ", frase, "\nCaracTeres:\n  ", len(frase),"\n\nFrase sem espacos antes e depois:\n  ", removeEspacos, "\nCaracteres:\n  ", len(removeEspacos))