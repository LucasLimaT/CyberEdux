N = int(input("Digite o valor de N: "))
for i in range(N):
    linha = ""
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1 or i == j or i + j == N - 1:
            linha += "*"
        else:
            linha += " "
    print(linha)
