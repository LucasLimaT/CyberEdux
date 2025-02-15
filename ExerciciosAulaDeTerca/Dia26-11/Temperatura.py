from ManipulacaoTemperatura import inserirTemperatura, maiorEMenorTemperatura, quantidadeAcimaDaMedia, temperaturaMedia

temperatura = list()
while True:
    for i in range(0,7):
        inserirTemperatura(temperatura, i)
    min, max = maiorEMenorTemperatura(temperatura)
    media = temperaturaMedia(temperatura)
    acimaDaMedia = quantidadeAcimaDaMedia(temperatura)
    print("\n")
    for i in range(len(temperatura)):
        print(f"dia {i+1}: {'*'*int(temperatura[i])} {temperatura[i]}º")
    print(f"\nMenor Temperatura: {min}º\nMaior Temperatura: {max}º\nTemperatura Media: {media:.2f}º\nDias acima da media: {acimaDaMedia}")
    break