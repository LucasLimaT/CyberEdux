numero = int(input("Digite o valor de N: "))
i = int(numero - 1)
y = int(numero)
while i >= 0:
    x = int(numero - i)
    print(" " * y, "* " * x)
    i -= 1
    y -= 1
