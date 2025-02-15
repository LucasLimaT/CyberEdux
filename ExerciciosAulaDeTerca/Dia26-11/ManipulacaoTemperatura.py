def inserirTemperatura(temperatura, i):
    temperaturaDia = float(input(f"Insira a temperatura do dia {i+1}: "))
    temperatura.append(temperaturaDia)

def maiorEMenorTemperatura(temperatura):
    return min(temperatura), max(temperatura)

def temperaturaMedia(temperatura):
    return ((sum(temperatura))/7)

def quantidadeAcimaDaMedia(temperatura):
    contador = int(0)
    for i in range(len(temperatura)):
        if (temperatura[i] > temperaturaMedia(temperatura)):
            contador += 1
    return contador
    