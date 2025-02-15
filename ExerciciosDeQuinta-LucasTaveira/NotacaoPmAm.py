def converter_para_12h(hora):
    if hora > 24 or hora < 0:
        return "Horario invalido!"
    elif hora > 12 : return str(hora - 12) + " PM"
    return hora + " AM"

while True:
    print(converter_para_12h(int(input("Escreva um horario: "))))
    continuar = input("Deseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break
