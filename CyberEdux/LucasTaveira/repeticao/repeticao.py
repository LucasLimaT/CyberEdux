lista_num = list()
for i in range(0, 10):
    x = int(input(f"Digite o {i+1}º número: "))
    lista_num.append(x)
print(f"Soma: {sum(lista_num)}")
print(f"Media: {sum(lista_num)/len(lista_num)}")
print(f"Minimo: {min(lista_num)}")
print(f"Maximo: {max(lista_num)}")
