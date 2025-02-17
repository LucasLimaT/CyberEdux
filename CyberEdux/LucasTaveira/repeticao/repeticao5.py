valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))
espacos = int(valor_a - 4)
i = int(1)
while i <= valor_b:
    if i == 1 or i == valor_b:
        print("*" * valor_a)
    else:
        print("*", " " * espacos, "*")
    i += 1
