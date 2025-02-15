def converter_data(data):
    novaData = ""
    mes = ""
    for i in range(len(data)):
        if i < 2:
            novaData = novaData + data[i]
        elif i == 2:
            novaData = novaData + " de "
        elif 2 < i and i < 5:
            mes = mes + data[i]
        elif i == 5:
            if mes == "01":
                novaData += "Janeiro de "
            if mes == "02":
                novaData += "Fevereiro de "
            if mes == "03":
                novaData += "Marco de "
            if mes == "04":
                novaData += "Abril de "
            if mes == "05":
                novaData += "Maio de "
            if mes == "06":
                novaData += "Junho de "
            if mes == "07":
                novaData += "Julho de "
            if mes == "08":
                novaData += "Agosto de "
            if mes == "09":
                novaData += "Setembro de "
            if mes == "10":
                novaData += "Outubro de "
            if mes == "11":
                novaData += "Novembro de "
            if mes == "12":
                novaData += "Dezembro de "
        else:
            novaData = novaData + data[i]
    return novaData

data = ""
while True:
    while len(data) != 10:
        data = input("Forneca uma data (DD/MM/AAAA): ")
    print(converter_data(data))
    
    continuar = input("\nDeseja continuar? (S/N)\n") 
    if continuar.upper() != "S" : break