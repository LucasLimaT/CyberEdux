valor_n = int(input("Digite o valor de N: "))
i = int(1)
while i <= valor_n:
    if i == 1 or i == valor_n:
        print("*" * valor_n)
    elif i > 3 and i <= (valor_n - 3) and i != valor_n / 2:
        print("*", " " * 0, "*", " " * 0, "*", " " * 0, "*")
    elif i >= valor_n / 2 and i < (valor_n - 3):
        print("*", " " * 1, "**", " " * 1, "*")
        if valor_n % 2 == 0:
            print("*", " " * 1, "**", " " * 1, "*")
        i += 1
    elif (i == 2 and i != valor_n) or (i == valor_n - 1 and i != valor_n):
        print("**", " " * (valor_n - 6), "**")
    elif (i == 3 and i != valor_n) or (i == valor_n - 2 and i != valor_n):
        print("* *", " " * (valor_n - 8), "* *")
    i += 1
