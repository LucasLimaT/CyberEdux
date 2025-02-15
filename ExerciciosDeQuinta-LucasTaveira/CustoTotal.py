def calcula_preco_final(valorProduto, quantidade, valorDoFrete):
    return float(valorProduto * quantidade + valorDoFrete)

while True:
    print(f"O custo total será de R${calcula_preco_final(float(input("Valor do produto: R$")), int(input("Quantidade do produto transportada: ")), float(input("Valor do frete: R$")))}")

    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break