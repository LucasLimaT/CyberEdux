frase = input("Escreva uma frase: ")
palavra = input("Escreva o prefixo da frase: ")
print("Sim, ela começa com o prefixo") if frase.startswith(palavra) else print("Não, ela não começa com o prefixo")