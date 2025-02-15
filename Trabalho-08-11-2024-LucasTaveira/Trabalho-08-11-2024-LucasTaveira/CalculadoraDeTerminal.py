continuar = bool(True)
erro = bool(False)
while True:
    calculadora = input("Digite uma expressão (Coloque expressões de no maximo 3 números): ")
    calculadoraFormatada = calculadora.replace(" ", "")
    tamCalc = len(calculadoraFormatada)
    ordem = ""
    aux = ""
    i = int(0)
    numerosNaFila = int(0)
    soma = float(0)
    resultado = float(0)
    resultadoFinal = str()
    expressaoDentroDoParenteses = ""
    existeOcorrencia = bool(False)
    for j in range(tamCalc):
        if calculadoraFormatada[j] == "(":
            existeOcorrencia = True
    while i < tamCalc:
        if calculadoraFormatada[i].isdigit():
            ordem = ordem + calculadoraFormatada[i]
            next = i+1
            if tamCalc >= next:
                while next != tamCalc and calculadoraFormatada[next].isdigit():
                        ordem = ordem + calculadoraFormatada[next]
                        next = next+1
                ordem = ordem + "|"
                numerosNaFila += 1
            i = next
        elif calculadoraFormatada[i] == "(":
            ordem = '(' + ordem
            existeOcorrencia = True
            next = i+1
            if next < tamCalc:
                if (calculadoraFormatada[i+1].isdigit() == False) and (calculadoraFormatada[i+1] != "("):
                    print("Operacao Invalida")
                    i = tamCalc
            i = next
        elif (calculadoraFormatada[i] == "+") or (calculadoraFormatada[i] == "/") or (calculadoraFormatada[i] == "-") or (calculadoraFormatada[i] == "*"):
            if existeOcorrencia == False:
                aux = ordem
                if calculadoraFormatada[i] == "*":
                    ordem = "*|" + aux 
                elif calculadoraFormatada[i] == "/":
                    if ordem.find("*|") == -1:
                        ordem = "/|" + aux
                    else:
                        ordem = aux[0:aux.find("*|")] + "/|" + aux[aux.find("*|"):]
                elif calculadoraFormatada[i] == "+":
                    if ordem.find("*|") == -1 and ordem.find("/|") == -1:
                        ordem = "+|" + aux
                    elif ordem.find("/|") != -1:
                        ordem = aux[0:aux.find("/|")] + "+|" + aux[aux.find("/|"):]
                    else:
                        ordem = aux[0:ordem.find("*|")] + "+|" + aux[aux.find("*|"):]
                elif calculadoraFormatada[i] == "-":
                    if ordem.find("*|") == -1 and ordem.find("/|") == -1:
                        ordem = "-|" + aux
                    elif ordem.find("/|") != -1:
                        ordem = aux[0:aux.find("/|")] + "-|" + aux[aux.find("/|"):]
                    else:
                        ordem = aux[0:ordem.find("*|")] + "-|" + aux[aux.find("*|"):]
            elif existeOcorrencia == True: 
                aux = expressaoDentroDoParenteses
                if calculadoraFormatada[i] == "*":
                    expressaoDentroDoParenteses = "*|" + aux 
                elif calculadoraFormatada[i] == "/":
                    if expressaoDentroDoParenteses.find("*|") == -1:
                        expressaoDentroDoParenteses = "/|" + aux
                    else:
                        expressaoDentroDoParenteses = aux[0:aux.find("*|")] + "/|" + aux[aux.find("*|"):]
                elif calculadoraFormatada[i] == "+":
                    if expressaoDentroDoParenteses.find("*|") == -1 and expressaoDentroDoParenteses.find("/|") == -1:
                        expressaoDentroDoParenteses = "+|" + aux
                    elif expressaoDentroDoParenteses.find("/|") != -1:
                        expressaoDentroDoParenteses = aux[0:aux.find("/|")] + "+|" + aux[aux.find("/|"):]
                    else:
                        expressaoDentroDoParenteses = aux[0:expressaoDentroDoParenteses.find("*|")] + "+|" + aux[aux.find("*|"):]
                elif calculadoraFormatada[i] == "-":
                    if expressaoDentroDoParenteses.find("*|") == -1 and expressaoDentroDoParenteses.find("/|") == -1:
                        expressaoDentroDoParenteses = "-|" + aux
                    elif expressaoDentroDoParenteses.find("/|") != -1:
                        expressaoDentroDoParenteses = aux[0:aux.find("/|")] + "-|" + aux[aux.find("/|"):]
                    else:
                        expressaoDentroDoParenteses = aux[0:expressaoDentroDoParenteses.find("*|")] + "-|" + aux[aux.find("*|"):]
            aux = ""
            i = i+1
        elif calculadoraFormatada[i] == ")":
            ordem = ordem.replace("(", "")
            existeOcorrencia = False
            ordem = expressaoDentroDoParenteses + ordem
            i = i+1
        else:
            print("Erro!")
            i = tamCalc
            erro = True
        if numerosNaFila >= 2 and existeOcorrencia == False:
            equacao = ordem.split("|")
            equacao = equacao[0:len(equacao)-1]
            while len(equacao) > 1:
                soma = equacao[len(equacao)-2] + " " + equacao[0] + " " + equacao[len(equacao)-1]
                equacao = equacao[1:len(equacao)-1]
                soma = soma.split(" ")
                if soma[1] == "+":
                    resultado = float(soma[0]) + float(soma[2])
                elif soma[1] == "-":
                    resultado = float(soma[0]) - float(soma[2])
                elif soma[1] == "*":
                    resultado = float(soma[0]) * float(soma[2])
                elif soma[1] == "/":
                    if float(soma[2]) != 0:
                        resultado = float(soma[0]) / float(soma[2])
                    else:
                        print("Operacao Invalida")
                        erro = True
                equacao[len(equacao)-1] = str(resultado)
            ordem = equacao[0] + "|"
            numerosNaFila = 1
    if erro == False:
        print("O resultado da sua expressão é: " + ordem[0:len(ordem)-1])
    else:
        erro = False
    desejaContinuar = input("Deseja calcular outras expressões?\n[1] Sim [2] Nao\n")
    if desejaContinuar != 1:
        break