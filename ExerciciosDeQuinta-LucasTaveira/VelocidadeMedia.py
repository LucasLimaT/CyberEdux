def velocidade_media(distancia, tempo):
    return (distancia / tempo) * 3.6

while True:
    print(f"Velocidade media {velocidade_media(float(input("Forneca a distancia percorrida em Metros: ")),int(input("Forneca o tempo em segundos: "))):.2f} Km/h")
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break