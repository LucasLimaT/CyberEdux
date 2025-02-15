produtos = [
    {"nome": "Notebook", "preco": 3000},
    {"nome": "Celular", "preco": 1500},
    {"nome": "Tablet", "preco": 2000}
]

maior_valor = float(0)
nome_maior_valor = None
for i in produtos:
    if maior_valor < i["preco"]:
        maior_valor = i["preco"]
        nome_maior_valor = i["nome"]
print(nome_maior_valor, maior_valor)