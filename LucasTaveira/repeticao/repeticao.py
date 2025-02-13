lista_num = list()
for i in range(0, 10):
    x=int(input(f"Digite o {i+1}º número: "))
    lista_num.append(x)
print(sum(lista_num))
print(sum(lista_num)/len(lista_num))
print(min(lista_num))
print(max(lista_num))
