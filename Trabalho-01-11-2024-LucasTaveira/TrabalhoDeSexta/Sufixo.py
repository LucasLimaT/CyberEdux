frase = input("Escreva uma frase: ")
palavra = input("Escreva o sufixo: ")
print("Sim, ela termina com o sufixo") if frase.endswith(palavra) else print("Não, ela não termina com o sufixo")