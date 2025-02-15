#quadrados = [x**2 for x in range(1, 11)]
#print(quadrados)

nomes = ["joao", "maria", "ana"]
idades = [25, 30, 22]

for i, c in enumerate(nomes):
    print(i+1,c)

for nome, idade, in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")