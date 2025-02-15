paises = {"BELGICA": "Bruxelas", "HOLANDA": "Amsterdam", "BRASIL": "Brasilia", "SUICA": "Berna", "PORTUGAL": "Lisboa"}
for keys in paises.items():
    print(f"{keys}")
pais = input("Digite o nome do seu pais: ").upper()
print(f"A capital do seu pais é: {paises[pais]}")
