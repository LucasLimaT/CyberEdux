import random

def caca_nique(valor_entrada):
    valor1 = random.randint(1, 3)
    valor2 = random.randint(1, 3)
    valor3 = random.randint(1, 3)
    ganho = float(0)
    if valor1 == valor2 == valor3:
        ganho = valor_entrada*2
        print(f"Parabéns você ganhou R${ganho}!")
    else:
        print("Você perdeu!")
    return (valor1, valor2, valor3, ganho)

saldo = float(input("Quanto deseja colocar de saldo?\nR$"))
while True and saldo > 0:
    print("Saldo atual: R$", saldo)
    valor_apostado = float(1)
    while True:
        valor_apostado = float(input("Quanto quer apostar?\nR$"))
        if valor_apostado > saldo or valor_apostado <= 0:
            print("Digite um valor valido!\nSaldo atual: R$", saldo)
        else:
            saldo -= valor_apostado
            break
    lista = caca_nique(valor_apostado)
    saldo += lista[3]
    print("Os numeros sorteados foram: ", lista[0:3])
    continuar = input("Deseja jogar novamente? (S/N)\n") 
    print("\n")
    if continuar.upper() != "S" : break
print("Boa sorte na proxima!")