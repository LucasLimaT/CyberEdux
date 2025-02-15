import random

def jogar_dados():
    print("Dado 1: ", dado1 := random.randint(1, 6))
    print("Dado 2: ", dado2 := random.randint(1, 6))
    return dado1 + dado2

while True:
    print("A soma dos dados é: ", jogar_dados())
    continuar = input("Deseja lançar novamente? (S/N)\n") 
    if continuar.upper() != "S" : break