def equacao(lista_num):
    new_list_par = list()
    new_list_impar = list()
    new_list_negativo = list()
    new_list_maior_media = list()
    media = sum(lista_num)/len(lista_num)
    for num in lista_num:
        if num % 2 == 0:
            new_list_par.append(num)
        else:
            new_list_impar.append(num)
        if num < 0:
            new_list_negativo.append(num)
        if num > media:
            new_list_maior_media.append(num)
    return new_list_par, new_list_impar, new_list_negativo, new_list_maior_media

lista_num = list()
for i in range(0, 10):
    x=float(input(f"Digite o {i+1}º número: "))
    lista_num.append(x)
pares, impares, negativos, maiores_media = equacao(lista_num)
print(f"pares: {pares}")
print(f"impares: {impares}")
print(f"negativos: {negativos}")
print(f"maiores que a media: {maiores_media}")