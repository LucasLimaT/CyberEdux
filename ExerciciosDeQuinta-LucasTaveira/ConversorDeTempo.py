def converter_Segundos(segundos):
    
    minutos = int(segundos/60)
    segundos -= int(minutos*60)

    horas = int(minutos/60)
    minutos -= int(horas*60)

    if horas != 1:
        textoHoras = str(horas) + " horas, "
    else:
        textoHoras = str(horas) + " hora, "

    if minutos != 1:
        textoMinutos = str(minutos) + " minutos e "
    else:
        textoMinutos = str(minutos) + " minuto e "

    if segundos != 1:
        textoSegundos = str(segundos) + " segundos"
    else:
        textoSegundos = str(segundos) + " segundo"

    textofinal = textoHoras + textoMinutos + textoSegundos

    return textofinal

while True:
    print(converter_Segundos(int(input("Digite os segundos que deseja converter: "))))
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break